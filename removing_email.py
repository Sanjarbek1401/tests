#1-version
"""import re

def clean_custom_patterns(text):
    # Example: Replace email addresses with a placeholder
    clean_text = re.sub(r'\S+@\S+', '[email]', text)
    return clean_text
text = "Mening ismim Sanjar va mening email pochtam:sanjarbahodirov9901@gmail.com"
clean_text = clean_custom_patterns(text)
print("Emaildan tozalanmagan text")
print(text)
print("Emaildan tozalangan text")
print(clean_text)"""

#2-version
"""
import re

def remove_emails(text):
    # Elektron pochta manzillariga mos keladigan regex patterni aniqlang
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Elektron pochta manzillarini bo'sh satr bilan almashtirish uchun re modulidagi sub() funksiyasidan foydalaning
    text_without_emails = re.sub(pattern, '', text)
    
    return text_without_emails

# Example input text containing email addresses
input_text = "Iltimos ko'proq ma'lumot olish uchun sanjarbaxodirov9901@gmail.com ga bog'laning"

# Elektron pochta manzillarini o'chirish uchun remove_emails funksiyasiga murojaat qiling
cleaned_text = remove_emails(input_text)

print(cleaned_text)
""" 
