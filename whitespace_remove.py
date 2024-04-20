# 1-version
"""def remove_whitespace(text):
    cleaned_text = ' '.join(text.split())
    return cleaned_text
text = " Matnni           tozalash tabiiy tilni qayta ishlash (NLP) vazifalarida muhim dastlabki ishlov berish bosqichi sanalib, bunda matn maʼlumotlarining sifati va izchilligini taʼminlash uchun maxsus belgilar, kulgichlar(emojis),         raqamlar, tinish belgilari va qoʻshimcha           boʻshliqlar, elektron pochta manzillari, HTML teglari hamda URL(Uniform Resource Locator) manzillari olib tashlanadi.         Ushbu tizim ma’lumotlar sifatini yaxshilash, ma’lumotlarni qayta ishlash samaradorligini oshirish va ma’lumotlarni tahlil qilishni osonlashtirish kabi turli afzalliklarni taqdim etadi. Bundan tashqari, u matn formatlarini standartlashtirishga yordam beradi, ma’lumotlarni yanada qulayroq va tushunarli qiladi.              Biroq, matnni tozalash tizimi bilan bog‘liq ba’zi kamchiliklar ham mavjud. Asosiy kamchiliklardan      biri shundaki, u ko‘p vaqt va resurslarni       talab qilishi mumkin, ayniqsa katta hajmdagi ma’lumotlar bilan ishlashda. "
result =remove_whitespace(text)
print(result)  """
# 2- version
"""
s = "       O'zbek tiliga davlat      tili maqomini berilishi, o'zbek tiliga    bo'lgan e'tiborni yanada yuksaltirdi  "
s = s.lstrip()
print(s)
"""

#3-version
"""
s = "     O'zbek tiliga davlat      tili maqomini berilishi, o'zbek tiliga    bo'lgan e'tiborni yanada yuksaltirdi"
s = s.replace(" ", "")
print(s)
"""
#4-version

import re
 
s = "     O'zbek tiliga davlat      tili maqomini berilishi, o'zbek tiliga    bo'lgan e'tiborni yanada yuksaltirdi "
s = re.sub(" +", " ", s)
print(s)
     
 
"""
def count_word_occurrences(text, word):
    words = text.split()
    count = 0
    for w in words:
        # To'g'ri solishtirish uchun kichik-katta harf farqini o'rib tashlaymiz
        if w.lower() == word.lower():  
            count += 1
    return count

text = "A boy is playing there. There is a playground. An aeroplane is in the sky. The sky is pink. Alphabets and numbers are allowed in the password. A boy is playing there. There is a playground. An aeroplane is in the sky. The sky is pink. Alphabets and numbers are allowed in the password."
word = "is"
result = count_word_occurrences(text, word)
print(f'The word "{word}" appears {result} times in the text.')
"""