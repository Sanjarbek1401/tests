def remove_duplicates(texts):
    unique_texts = list(set(texts))
    return unique_texts

# Sample list of texts with duplicates
texts = ["Mening ismim Sanjar", "Va men 1997- yil tug'ilganman.", "Mening ismim Sanjar"]
unique_texts = remove_duplicates(texts)

print("Original list of texts with duplicates:")
print(texts)
print("\nList of unique texts after removing duplicates:")
print(unique_texts)
