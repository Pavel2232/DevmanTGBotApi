import requests

from telegram import Bot

from environs import Env

from dataclasses import Response
from functions import convert_the_response

env = Env()
env.read_env('.env')

bot = Bot(env('TG_BOT_KEY'))

headers = {'Authorization': 'Token {}'.format(env('DEWMAN_KEY'))}
link = 'https://dvmn.org/api/long_polling/'


def main():
    link = 'https://dvmn.org/api/long_polling/'
    while True:
        try:
            response = requests.get(link, headers=headers)
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            continue
        if response.json().get('status') == 'timeout':
            link += "?timestamp={}".format(response.json().get('timestamp_to_request'))
        else:
            results: Response = Response(**response.json())
            for result in results.new_attempts:
                bot.send_message(text=f"""у вас проверили работу '{result.lesson_title}'\n"""
                                      f"""{result.lesson_url}\n"""
                                      f"""{convert_the_response(result.is_negative)}""", chat_id=env('CHAT_ID'))
                continue


if __name__ == '__main__':
    main()
