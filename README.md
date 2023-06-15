# Бот отправления уведомления о проверке работ для Devman Api
Telegram bot для уведомлений о результатах  проверки домашней работы  от Devman 
![Пример работы](https://raw.githubusercontent.com/Pavel2232/DevmanTGBotApi/master/Screenshot_20230615_135206.jpg)
### Как запустить проект.
1. ``` git clone https://github.com/Pavel2232/DevmanTGBotApi```

2. Установите необходимые библиотеки  ```poetry init```

3. Создайте файл .env и заполните следующие значения:
* DEVMAN_API_KEY= девман апи ключ 
* TG_BOT_KEY=ключ телеграм бота 
* TG_CHAT_ID= ваш чат айди(Чтобы получить свой chat_id, напишите в Telegram специальному боту: @userinfobot)

4. Для запуска через docker выполните команды:
- ```docker build -t my_image_tag . ```
- ```docker run — env_file .env my_image_tag  ```


5. Для запуска программы  без использования docker:
```python main.py```