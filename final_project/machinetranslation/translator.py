from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    translator = MyMemoryTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    return english_text
    
# from googletrans import Translator

# def english_to_french(english_text):
#     translator = Translator()
#     translation = translator.translate(english_text, src='en', dest='fr')
#     french_text = translation.text
#     return french_text

# def french_to_english(french_text):
#     translator = Translator()
#     translation = translator.translate(french_text, src='fr', dest='en')
#     english_text = translation.text
#     return english_text
