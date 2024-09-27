# 209m_DataAnalyse_VkGetFriends
Групповая лаба VkGetFriends для дисциплины "методы обработки и анализа данных"

Участники работы из группы 209:        
Прозоров Евгений          
Брежнев Вячеслав        
Пешков Максим        
Кравцов Кирилл        
Кирьянов Павел          


Использован питон, vk_api и библиотека создания графов pyvis. 

Граф друзей студентов группы 209 представлен в файле friends_network.html, для просмотра необходимо открыть его в браузере. Код для генерации файлов в getFriends.py, отрисовка в GraphBuilder.
      
![image](https://github.com/user-attachments/assets/ebabc3d4-ba3c-4537-9110-0aaea40a0cc9)
![image](https://github.com/user-attachments/assets/6e32fefa-1b63-412c-ad9b-ee5f498de8ec)


Далее мы начали делать граф друзей друзей. Код для вытаскивания этих файлов представлен в getFriendsFriend.py. Получилось 14700 файлов, общим весом 2.5 гигабайта. Файлы создавались с 17:23 до 1:47.    

 ![image](https://github.com/user-attachments/assets/4a278f6d-273c-4996-8902-abbd706dd8bf)      
![image](https://github.com/user-attachments/assets/a87dd0d0-07f1-44d7-bb99-76446d19729d)


Граф с помощью библиотеки pyvis строился уже больше двух суток, и поэтому пока ожидается генерация файла. Позже он будет назван friends_friend_network      


