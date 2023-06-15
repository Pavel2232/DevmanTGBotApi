import time

import requests

from telegram import Bot

from environs import Env

from Dataclassapi import Response


def main():
    link = 'https://dvmn.org/api/long_polling/'
    while True:
        try:
            playload = {}
            response = requests.get(link, headers=headers, params=playload)
            response.raise_for_status()
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            time.sleep(30)
            continue
        response_json_status = response.json().get('status')
        if response_json_status == 'timeout':
            playload['timestamp'] = response.json().get('timestamp_to_request')
        else:
            results: Response = Response(**response.json())
            for result in results.new_attempts:
                if result.is_negative is False:
                    verification_result = 'Преподавателю всё понравилось можно приступать к следующему уроку!'
                else:
                    verification_result = 'К сожалению, в работе нашлись ошибки'
                bot.send_message(text=f"""у вас проверили работу '{result.lesson_title}'"""
                                      f"""{result.lesson_url}"""
                                      f"""{verification_result}""", chat_id=env('TG_CHAT_ID'))



if __name__ == '__main__':
    env = Env()
    env.read_env('.env')
    bot = Bot(env('TG_BOT_KEY'))

    headers = {'Authorization': 'Token {}'.format(env('DEVMAN_API_KEY'))}
    link = 'https://dvmn.org/api/long_polling/'
    main()
