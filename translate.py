from deep_translator import GoogleTranslator

# from deep_translator import ChatGptTranslator


while 1:

	text = input('input the text:')

	lang = input('translate to:')

	translated = GoogleTranslator(source = 'auto' , target = lang)

	translated.translate(text = text)