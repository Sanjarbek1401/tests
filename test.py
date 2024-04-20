'''lists = [[1,2,3], [4,5,6], [10,11,12],[7,8,9]]

max_sum = 0
max_list = []

for num in lists:
    if sum(num) > max_sum:
        max_sum = sum(num)
        max_list = num

print(max_list)'''


def count_word (text, word):
    words = text.split()
    count = 0
    for w in words:
        if w.lower() == word.lower():
            count +=1
    return count
text = "A boy is playing there. There is a playground. An aeroplane is in the sky. The sky is pink. Alphabets and numbers are allowed in the password. A boy is playing there. There is a playground. An aeroplane is in the sky. The sky is pink. Alphabets and numbers are allowed in the password."        
word = "is"
result = count_word(text, word)
print(f'"{word}" matn tarkibida {result} marta kelgan ')



 
