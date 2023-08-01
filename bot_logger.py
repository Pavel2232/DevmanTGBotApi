import logging


class TelegramLogger(logging.Handler):

    def __init__(self, bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = bot

    def emit(self, record):
        log = self.format(record)
        send_message = self.tg_bot.send_message(chat_id=self.chat_id, text=log)
