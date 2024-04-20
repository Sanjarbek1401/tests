import re

def remove_html_tags(text):
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text

# Sample text with HTML tags
html_text = "<h1>Hello, <strong>World!</strong></h1>"
clean_text = remove_html_tags(html_text)

print("HTML teglari bilan asl matn:")
print(html_text)
print("\nHTML teglarini olib tashlaganingizdan keyin matn:")
print(clean_text)
