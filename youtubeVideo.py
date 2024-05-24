import requests
import webbrowser


def search(query):
    youtube_api_key = 'AIzaSyDr0O13KEkhwM8E6sRf7fWAMY6CVpK8HsM'
    youtube_url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={query}&key={youtube_api_key}'

    try:
        # Отправляем GET-запрос к YouTube Data API
        response = requests.get(youtube_url)
        data = response.json()
        # Получаем ссылку на первое найденное видео
        video_id = data['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        return video_url
    except Exception as e:
        return f"Произошла ошибка при выполнении поиска на YouTube: {e}"


# Проигрывание видео в браузере
def play_video(video_url):
    webbrowser.open(video_url)

def main(query):
    video_url = search(query)
    if video_url:
        play_video(video_url)
        return f"Запускаю видео по вашему запросу: {query}"
    else:
        return "К сожалению, видео не найдено"