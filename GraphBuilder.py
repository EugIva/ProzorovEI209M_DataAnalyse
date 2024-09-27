from pyvis.network import Network
import json
import os
from collections import defaultdict

node_frequencies = defaultdict(int)

# JSON files
for filename in os.listdir("."):
    if filename.startswith("friends_") and filename.endswith(".json"):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            friends = data["friends"]
            for friend in friends:
                print('Сохранение из JSON')
                print(friend['last_name'])
                node_frequencies[friend["id"]] += 1

net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

# итерация всех JSON
for filename in os.listdir("."):
    if filename.startswith("friends_") and filename.endswith(".json"):

        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            user_id = data["user_id"]
            friends = data["friends"]

            # красная user_id нода
            net.add_node(user_id, label=str(user_id), title=str(user_id), color="red")

            # друзья этого userId
            for friend in friends:
                print('Отрисовка')
                print(friend['last_name'])

                friend_id = friend["id"]
                # цвета
                if node_frequencies[friend_id] > 1:
                    color = "green"
                else:
                    color = "#97c2fc"  # остальные

                net.add_node(friend_id, label=friend['last_name'], title=f"{friend['first_name']} {friend['last_name']}", color=color)
                net.add_edge(user_id, friend_id)

# HTML сохранение
net.save_graph("friends_friend_network.html")