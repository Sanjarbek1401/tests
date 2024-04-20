#3-version
import re
# Email qatnashgan tekst kiriting
text_with_emails = "Iltimos qandaydir yordam kerak bo'ladigan bo'lsa sanjarbahodirov@gmail.com bilan bog'laning "
# Regular expression yordamida elektron pochta xabarlarini olib tashlang
pattern = r'\S+@\S+'
text_without_emails = re.sub(pattern, '', text_with_emails)
print(text_without_emails)