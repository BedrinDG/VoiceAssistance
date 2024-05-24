import googlesearch
import requests
from bs4 import BeautifulSoup


def search(query):
    try:
        # Используем библиотеку google для выполнения поискового запроса
        search_results = list(googlesearch.search(query, num=1))
        if search_results:
            return search_results[0]
        else:
            return "Ничего не найдено"
    except Exception as e:
        return f"Произошла ошибка при выполнении поиска: {e}"

def read_search_result(url):
    try:
        # Отправляем GET-запрос к странице результатов поиска
        response = requests.get(url)
        # Преобразуем HTML-код страницы в объект BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Находим все абзацы (тег <p>) на странице и объединяем текст в одну строку
        # paragraphs = soup.find_all('p')
        text = soup.find('p').get_text()
        return text
    except Exception as e:
        return f"Произошла ошибка при чтении результатов поиска: {e}"

def main(query):
    search_result = search(query)
    return read_search_result(search_result)
