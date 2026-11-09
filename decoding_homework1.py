text = str(input("Enter the text: "))
result = ""
for i, symbol in enumerate(text):
    if i.isalpha():
        symbol = text[i]
        count = int(text[i+1])
        result += symbol * count
print(result)