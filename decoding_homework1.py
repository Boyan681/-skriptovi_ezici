text = str(input("Enter the text: "))
result = ""
for i in range (0,len(text), 2):
    char = text[i]
    count = int(text[i+1])
    result += char * count
print(result)