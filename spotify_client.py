import random
import string
import urllib
import requests


class SpotifyClient(object):
    def __init__(self, api_key):
        # Инициализация клиента Spotify с ключом API
        self.api_key = api_key

    def get_random_tracks(self):
        # Генерация случайной буквы для wildcard-запроса
        wildcard = f'%{random.choice(string.ascii_lowercase)}%'

        # Кодирование запроса для URL
        query = urllib.parse.quote(wildcard)

        # Случайное смещение (offset) для результатов поиска
        offset = random.randint(0, 2000)

        # Формирование URL для поиска треков на Spotify
        url = f'https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track'

        # Выполнение GET-запроса к API Spotify с необходимыми заголовками (тип данных и авторизация)
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
        )

        # Преобразование ответа в JSON-формат
        response_json = response.json()

        # Извлечение треков из результата поиска
        tracks = [track for track in response_json['tracks']['items']]

        # Вывод информации о количестве найденных треков
        print(f'Found {len(tracks)} from your search')

        # Возвращение списка найденных треков
        return tracks

    def add_tracks_to_library(self, track_ids):
        # Формирование URL для добавления треков в библиотеку пользователя
        url = 'https://api.spotify.com/v1/me/tracks'

        # Выполнение PUT-запроса к API Spotify с заголовками и передаваемыми идентификаторами треков
        response = requests.put(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            },
            json={
                'ids': track_ids
            }
        )

        # Возвращение результата успешности запроса (True или False)
        return response.ok

