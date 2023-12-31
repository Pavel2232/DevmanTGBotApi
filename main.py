import logging
import textwrap
import time

import requests

from telegram import Bot

from environs import Env

from Dataclassapi import Response
from bot_logger import TelegramLogger

logger = logging.getLogger('tg_bot')


def main():
    logging.basicConfig(level=logging.INFO, format="%(process)d %(levelname)s %(message)s")
    env = Env()
    env.read_env('.env')
    bot = Bot(env('TG_BOT_KEY'))
    logger.addHandler(TelegramLogger(bot, env('TG_CHAT_ID')))
    headers = {'Authorization': 'Token {}'.format(env('DEWMAN_API_KEY'))}
    link = 'https://dvmn.org/api/long_polling/'
    logger.info('Бот запущен')
    while True:

        try:
            playload = {}
            response = requests.get(link, headers=headers, params=playload)
            response.raise_for_status()
            results: Response = Response(**response.json())
        except requests.exceptions.ConnectionError:
            time.sleep(30)
            continue
        except requests.exceptions.ReadTimeout:
            continue
        except Exception as e:
            logger.exception(e)

        if results.status == 'timeout':
            playload['timestamp'] = results.timestamp_to_request
        else:
            for result in results.new_attempts:
                if result.is_negative is False:
                    verification_result = 'Преподавателю всё понравилось можно приступать к следующему уроку!'
                else:
                    verification_result = 'К сожалению, в работе нашлись ошибки'
                bot.send_message(text=textwrap.dedent(f'''
                                      у вас проверили работу '{result.lesson_title}'
                                      {result.lesson_url}
                                      {verification_result}'''), chat_id=env('TG_CHAT_ID'))


if __name__ == '__main__':
    main()
