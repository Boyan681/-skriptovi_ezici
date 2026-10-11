text = str(input("Enter the text: "))
result = ""
if len(text)>0:
    current_char = text[0]
    count = 1
    for i in range (1,len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result += current_char + str(count)
            current_char = text[i]
            count = 1
    result += current_char + str(count)
print(result)