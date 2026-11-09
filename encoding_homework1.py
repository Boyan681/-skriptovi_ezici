text = str(input("Enter the text: "))
result = ""
symbol = ''
count =0
for s in text:
    if s == symbol:
        count += 1
    else:
        if count>0:
            result += symbol + str(count)
        symbol = s
        count = 1
result += symbol + str(count)
print(result)