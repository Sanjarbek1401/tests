"""import re

def remove_special_characters(text):
    clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return clean_text

# Maxsus belgilar bilan matn namunasi
text_with_special_chars = "O'zbekiston  # Respublikasi $ @ poytaxti % Toshkent shahri&*![]"
clean_text = remove_special_characters(text_with_special_chars)

print("Maxsus belgilar bilan asl matn:")
print(text_with_special_chars)
print("\nMaxsus belgilarni olib tashlaganingizdan so'ng matn:")
print(clean_text)"""
import re
def remove_special_characters(text):
    return ''.join(char for char in text if char.isalnum() or char.isspace())

text = "Salom! Ahvollaringiz # yaxshimi?😁👩‍👩‍👦‍👦👨🏾‍🤝‍👨🏻©®:-)?"
cleaned_text = remove_special_characters(text)
print(cleaned_text)

