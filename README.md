# Бот отправления уведомления о проверке работ для Devman Api
Telegram bot для уведомлений о результатах  проверки домашней работы  от Devman 
![alt text](https://s164vla.storage.yandex.net/rdisk/c99f1b04ae9e6ca4a0f42bbf3e75c4ea2db1e86ec6887ef8df3c25b7fcf801c7/648b284a/yjISQgrXm8ieWICpfEzSDn8S0CCvgU_IFXGKtDGQpFQ5Hl1VnXeFNvB3VpUXRu278ra8b9mIBGnTI5-jO9qshw==?uid=0&filename=Screenshot_20230615_135206.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=815557&hid=e58cf0d4e32ab2f8f8648ad6eb99940b&media_type=image&tknv=v2&etag=f670c485121abf8f902806a0f2394acc&rtoken=LyVXze3AcRUl&force_default=no&ycrid=na-1cd707f101a40fd649786e51638daf62-downloader13f&ts=5fe2c5f832680&s=92d6d8ee2d8d96ef6afff29724f28343781639c76ebaa56d4d9b1d31df5e7397&pb=U2FsdGVkX1_Meeclx_j7n4xdbssforK5lurLAocSRJ9thrmWTK12JDx0iLEATj7aG_GzeHh60zVuQJ-gGRbHPn64TWoxhGlNo_GC4T-Bm6o)
### Как запустить проект.
1. ``` git clone https://github.com/Pavel2232/DevmanTGBotApi```

2. Установите необходимые библиотеки  ```poetry init```

3. Создайте файл .env и заполните следующие значения:
* DEWMAN_API_KEY= девман апи ключ 
* TG_BOT_KEY=ключ телеграм бота 
* TG_CHAT_ID= ваш чат айди(Чтобы получить свой chat_id, напишите в Telegram специальному боту: @userinfobot)

4. Для запуска через docker выполните команды:
- ```docker build . ```
- ```docker run ```


5. Для запуска программы  без использования docker:
```python main.py```