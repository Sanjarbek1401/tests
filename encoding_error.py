import chardet

def fix_encoding(text):
    try:
        # Attempt to decode the text as UTF-8
        decoded_text = text.encode('latin-1').decode('utf-8')
    except UnicodeDecodeError:
        # If UnicodeDecodeError occurs, try to detect the encoding
        encoding = chardet.detect(text)['encoding']
        try:
            # Try to decode the text using the detected encoding
            decoded_text = text.encode('latin-1').decode(encoding)
        except:
            decoded_text = 'Cannot decode with detected encoding'

    return decoded_text

# Example text with potential encoding issues
text_with_encoding_issues = "This text has non-ASCII characters â€“ café"

# Attempt to fix the encoding issues in the text
fixed_text = fix_encoding(text_with_encoding_issues)

# Output the original and fixed text
print("Original text:")
print(text_with_encoding_issues)
print("\nText after fixing encoding issues:")
print(fixed_text)

'''Kodlash muammolari matnni qayta ishlash jarayonida o'qilmaydigan belgilar
yoki xatolarga olib kelishi mumkin. Matnning to'g'ri kodlanganligini 
 ta'minlash (masalan, UTF-8) belgilarni kodlash bilan bog'liq muammolarni oldini olish uchun juda muhimdir.'''