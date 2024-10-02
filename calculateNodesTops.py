# рассчитать в графе количество вершин и рёбер.
# в папке friends есть набор json файлов friends_***, где *** - это user id, главная вершина графа. внутри файлов есть перечень их
# друзей, к которым надо построить рёбра из главной вершины. Далее взять следующий, проверить, есть ли уже среди друзей
# прошлых вершин текущий user id, и продолжить построение по такой же схеме, чтобы не было повторений. Надо посчитать
# количество вершин графа и всех связей в нём, чтобы оценить граф, и записать результат в новый файлик.

import json
import os
from tqdm import tqdm

def load_json_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        return json.load(file)

def build_graph(friends_dir):
    vertices = set()
    edges = set()

    for filename in tqdm(os.listdir(friends_dir)):
        if filename.startswith('friends_') and filename.endswith('.json'):
            file_path = os.path.join(friends_dir, filename)
            data = load_json_file(file_path)
            user_id = data['user_id']
            vertices.add(user_id)

            for friend in data['friends']:
                friend_id = friend['id']
                if friend_id not in vertices:
                    vertices.add(friend_id)
                edge = tuple(sorted((user_id, friend_id)))
                edges.add(edge)

    return vertices, edges

def main():
    friends_dir = 'friends'
    vertices, edges = build_graph(friends_dir)
    num_vertices = len(vertices)
    num_edges = len(edges)

    print(f"Количество вершин: {num_vertices}")
    print(f"Количество ребер: {num_edges}")

    # Запись результатов в новый файл
    with open('graph_stats.txt', 'w', encoding='utf-8') as file:
        file.write(f"Количество вершин: {num_vertices}\n")
        file.write(f"Количество ребер: {num_edges}")

if __name__ == "__main__":
    main()
