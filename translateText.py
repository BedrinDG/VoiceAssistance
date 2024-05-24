from translate import Translator

# Словарь поддерживаемых языков с их кодами
LANGUAGES = {
    'английский': 'en',
    'испанский': 'es',
    'французский': 'fr',
    'немецкий': 'de',
    'итальянский': 'it',
    'китайский': 'zh-CN',
    'японский': 'ja',
    'португальский': 'pt',
    'хинди': 'hi',
    'бенгальский': 'bn',
    'арабский': 'ar',
    'турецкий': 'tr',
    'корейский': 'ko',
    'фарси': 'fa',
    'украинский': 'uk',
    'польский': 'pl',
    'тайский': 'th',
    'нидерландский': 'nl',
    'индонезийский': 'id',
    'чешский': 'cs',
    'румынский': 'ro',
    'греческий': 'el',
    'белорусский': 'be',
    'болгарский': 'bg',
    'сербский': 'sr',
    'хорватский': 'hr',
    'сингальский': 'si',
    'словацкий': 'sk',
    'словенский': 'sl',
    'урду': 'ur',
    'башкирский': 'ba',
    'азербайджанский': 'az'
}

def translate(text, dest_lang, source_lang='ru'):
    translator = Translator(from_lang=source_lang, to_lang=dest_lang)
    translated_text = translator.translate(text)
    return translated_text

def main(text, language):
    if language.lower() not in LANGUAGES:
        return "Некорректный код языка или же его нет в списке поддерживаемых языков"
    else:
        result = translate(text, LANGUAGES[language.lower()])
        return f"Переведённый текст: {result}"