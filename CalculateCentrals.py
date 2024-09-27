# Необходимо оценить центральность: по посредничеству, по близости, собственного вектора.
import json
import networkx as nx
import os
from tqdm import tqdm


def load_json_files(directory):
    graph = nx.Graph()
    for filename in tqdm(os.listdir(directory)):
        if filename.startswith('friends_') and filename.endswith('.json'):
            filename_parts = filename.split('_')
            user_id = filename_parts[1].split('.')
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                data = json.load(file)
                graph.add_node(user_id[0])
                for friend in data['friends']:
                    friend_id = str(friend['id'])
                    graph.add_node(friend_id)
                    graph.add_edge(user_id[0], friend_id)
    return graph


def calculate_centrality_measures(graph):
    betweenness_centrality = nx.betweenness_centrality(graph)
    closeness_centrality = nx.closeness_centrality(graph)

    # параметры центрального положения собственного вектора для обеспечения сходимости
    eigenvector_centrality = nx.eigenvector_centrality(graph, max_iter=1000, tol=1e-03)
    # Параметры сходимости: max_iter и tol параметры в nx.eigenvector_centrality скорректированы таким образом, чтобы
    # увеличить количество итераций и снизить допуск соответственно, чтобы способствовать сходимости метода степенных итераций.

    return betweenness_centrality, closeness_centrality, eigenvector_centrality


def save_results(centrality_measures, output_filename):
    with open(output_filename, 'w', encoding='utf-8') as file:
        for measure_name, measure in centrality_measures.items():
            file.write(f"{measure_name} Centrality:\n")
            for node, value in measure.items():
                file.write(f"  {node}: {value}\n")
            file.write("\n")


def main():
    directory = '.'
    output_filename = 'centrality_measures.txt'

    graph = load_json_files(directory)

    # проверка на связность графа. Если график не связан, код вычисляет показатели центральности для каждого
    # подключенного компонента отдельно и сохраняет результаты в отдельных файлах.
    if not nx.is_connected(graph):
        print("График не связан. Вычисление центральности для каждого связанного компонента.")
        components = list(nx.connected_components(graph))
        for i, component in enumerate(components):
            subgraph = graph.subgraph(component)
            betweenness_centrality, closeness_centrality, eigenvector_centrality = calculate_centrality_measures(
                subgraph)
            centrality_measures = {
                'Степень посредничества': betweenness_centrality,
                'Степень близости': closeness_centrality,
                'По собственному вектору': eigenvector_centrality
            }
            save_results(centrality_measures, f'centrality_measures_{i}.txt')
    else:
        betweenness_centrality, closeness_centrality, eigenvector_centrality = calculate_centrality_measures(graph)
        centrality_measures = {
            'Степень посредничества': betweenness_centrality,
            'Степень близости': closeness_centrality,
            'По собственному вектору': eigenvector_centrality
        }
        save_results(centrality_measures, output_filename)


if __name__ == "__main__":
    main()
