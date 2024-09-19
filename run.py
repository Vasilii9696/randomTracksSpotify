import os
from spotify_client import SpotifyClient


def run():
    # Получение токена авторизации для Spotify из переменных окружения
    spotify_client = SpotifyClient(os.getenv('SPOTYFY_AUTH_TOKEN'))

    # Получение случайных треков из Spotify
    random_tracks = spotify_client.get_random_tracks()

    # Извлечение ID треков из полученных случайных треков
    track_ids = [track['id'] for track in random_tracks]

    # Добавление полученных треков в библиотеку пользователя
    was_added_to_library = spotify_client.add_tracks_to_library(track_ids)

    # Если треки успешно добавлены в библиотеку, выводим сообщение для каждого трека
    if was_added_to_library:
        for track in random_tracks:
            print(f'Added {track["name"]} to your library')


# Запуск функции run() при запуске скрипта
if __name__ == '__main__':
    run()
