from langdetect import detect

def detect_language(text):
    try:
        language = detect(text)
    except:
        language = 'unknown'
    return language

text = "Hello, how are you?"
language = detect_language(text)
print(language)
