# 209m_DataAnalyse_VkGetFriends
Групповая лаба VkGetFriends для дисциплины "методы обработки и анализа данных"

Участники работы из группы 209:        
Прозоров Евгений          
Брежнев Вячеслав        
Пешков Максим        
Кравцов Кирилл        
Кирьянов Павел          


Использован питон, vk_api и библиотека создания графов pyvis. id одногруппников были взяты из таблицы, созданной в нашей группе https://docs.google.com/spreadsheets/d/10UbVq80A7I1Ww6v-28yRCRo2CscFhSWC/edit?gid=528477936#gid=528477936 .            
Код для генерации файлов предсатвлен в getFriends.py. Получаемые файлы имеют структуру такого вида:                        
{                  
"user_id": 22473173,                  
"friends": [                  
                  {                  
                  "id": 757207,                  
                  "first_name": "Мария",                  
                  "last_name": "Залуцкая"                  
                  }                  
            ]                  
}                  

Код для отрисовки графа представлен в GraphBuilder.py. Граф друзей студентов группы 209 представлен в файле friends_network.html, для просмотра необходимо открыть его в браузере.
      
![image](https://github.com/user-attachments/assets/ebabc3d4-ba3c-4537-9110-0aaea40a0cc9)
![image](https://github.com/user-attachments/assets/6e32fefa-1b63-412c-ad9b-ee5f498de8ec)


Далее мы начали делать граф друзей друзей. Код для вытаскивания этих файлов представлен в getFriendsFriend.py. Получилось 14700 файлов, общим весом 2.5 гигабайта. Файлы создавались несколько часов, с 17:23 до 1:47.    

 ![image](https://github.com/user-attachments/assets/4a278f6d-273c-4996-8902-abbd706dd8bf)      
![image](https://github.com/user-attachments/assets/a87dd0d0-07f1-44d7-bb99-76446d19729d)

Граф друзей друзей с помощью библиотеки pyvis строился больше двух суток, назван friends_friend_network. Открыть полученный граф невозможно, не хватает памяти для его отображения. Вес файла 250мб, загрузить в гитхаб невозможно
![image](https://github.com/user-attachments/assets/ebd8cd4a-f90b-4f51-9635-427e43ed659a)
![image](https://github.com/user-attachments/assets/959f882c-6e8f-438d-8ef2-c5d135fed1cc)


      
      
      
Следующим этапом будет произведена оценка центральности по посредничеству, по близости, собственного вектора для группы 209.      

