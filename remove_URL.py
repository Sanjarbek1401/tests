import re

def remove_url(text):
    # URL manzillarini aniqlash 
    url_pattern = r'https?://\S+|www\.\S+'
    
    # URL manzillarini matndan olib tashlang
    text_without_urls = re.sub(url_pattern, '', text)
    
    return text_without_urls

# Example usage
text = "Qo'shimcha ma'lumot olish uchun  https://www.example.com saytiga tashrif buyuring"
clean_text = remove_url(text)
print(clean_text)

#Output:  Qo'shimcha ma'lumot olish uchun   saytiga tashrif buyuring