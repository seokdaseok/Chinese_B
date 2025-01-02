from googletrans import Translator
#import googletrans

translator = Translator()

# translate a spanish text to english text (by default)
translation = translator.translate("你好")
#print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

#print(translation)

def translate_chinese_word(chinese_word):
    translation = translator.translate(chinese_word)

    return translation.text