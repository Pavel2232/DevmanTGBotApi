def convert_the_response(response: bool) -> str:
    if response is False:
        return 'Преподавателю всё понравилось можно приступать к следующему уроку!'
    else:
        return 'К сожалению, в работе нашлись ошибки'
