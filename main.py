import pyttsx3
import speech_recognition as sr

import weather
import webSearch
import youtubeVideo
import translateText

stop_reading = False

# Функция для распознавания речи с помощью SpeechRecognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Устранение фонового шума
        audio = recognizer.listen(source)
    try:
        # Запись запроса в переменную query
        query = recognizer.recognize_google(audio, language="ru-RU")
        return query.lower()
    except sr.RequestError as e:
        print(f"Произошла ошибка при отправке запроса к сервису распознавания речи: {e}")
        return ""

# Функция для синтеза речи с помощью pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Устанавливаем скорость произношения
    engine.say(text)
    engine.runAndWait()

#Функция для распознавания погоды
def weatherCity():
    speak("Хорошо, где вы хотите узнать погоду")
    city = recognize_speech()
    speak(weather.mainWeather(city))

def videoOnYoutube():
    speak("Подскажите название видео")
    video = recognize_speech()
    speak(youtubeVideo.main(video))

def translate():
    speak("Подскажите текст, который необходимо перевести")
    text = recognize_speech()
    speak("На какой язык необходимо перевести?")
    lang = recognize_speech()
    speak(f"{translateText.main(text, lang)}")

def searchInGoogle():
    speak("Что необходимо найти?")
    query = recognize_speech()
    speak("Выполняю поиск")
    result = webSearch.main(query)
    speak("Результат поиска")
    speak(result)

#Хэш-таблица с возможными командами
function_table = {
    "подскажи погоду": weatherCity,
    "включи видео": videoOnYoutube,
    "переведи текст": translate,
    "поиск в интернете": searchInGoogle
}

# Главная функция
def main():
    try:
        while True:
            command = recognize_speech()
            print(command)
            if command in function_table:
                function_table[command]()
            elif "конец работы" in command:
                speak("До свидания!")
                break
            elif "что ты умеешь" in command:
                speak("Я выполняю следующие команды:")
                for func in function_table.keys():
                    speak(func)
    except sr.UnknownValueError:
        return main()

if __name__ == "__main__":
    speak("Привет! Чем я могу вам помочь?")
    main()
