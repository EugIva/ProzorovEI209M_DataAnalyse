import vk_api
import json

access_token = ''
# сюда вставить вк токен, свой я не дам

# Создание сессии VK API с использованием access_token
vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()

def get_friends(user_id):
    try:
        friends = vk.friends.get(user_id=user_id, fields='first_name,last_name')
        return friends['items']
    except vk_api.ApiError as e:
        print(f"Error for user {user_id}: {e}")
        return []
    except vk_api.exceptions.Captcha as captcha:
        # Обработка капчи, если она понадобится
        captcha_key = handle_captcha(captcha)
        friends = vk.friends.get(user_id=user_id, fields='first_name,last_name', captcha_sid=captcha.sid, captcha_key=captcha_key)
        return friends['items']

def handle_captcha(captcha):
    # Отобразить изображение капчи и запросить у пользователя ввод кода
    print("Captcha needed. Please solve the captcha at the following URL:")
    print(captcha.get_url())
    captcha_key = input("Enter the captcha code: ")
    return captcha_key

def create_json_file(user_id, friends):
    data = {
        'user_id': user_id,
        'friends': [{'id': friend['id'], 'first_name': friend['first_name'], 'last_name': friend['last_name']} for friend in friends]
    }
    with open(f'friends_{user_id}.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Список ID пользователей, для которых нужно получить друзей
user_ids = [1931147, 176183602, 290530655, 207227130, 24435047, 138042735, 172244589, 168420440, 711398942, 65657314, 50933461, 198216820, 268235974] #Брежнев, Прозоров, Алимов,

# Получение списка друзей для каждого пользователя и создание JSON файла
for user_id in user_ids:
    friends = get_friends(user_id)
    create_json_file(user_id, friends)
    print(f"Friends for user {user_id}:")
    for friend in friends:
        print(f"ID: {friend['id']}, Name: {friend['first_name']} {friend['last_name']}")
