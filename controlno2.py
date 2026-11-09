a = []
count = 0
count_neg = 0
sum = 0
smallest = 1000
num = int(input("Enter a number: "))
a.append(num)
if num ==0:
    print("No data")
else:
    while(num != 0):
        num = int(input("Enter a number: "))
        a.append(num)
        if(num < 0):
            sum += num
            count_neg += 1
for i in range(len(a)-1):
    if a[i]<smallest :
        smallest = a[i]
    if a[i]<a[i+1] :
        count += 1
print("The smallest number is: ", smallest)
print("The count of the numbers that are less than their successor is: ", count)
percent = (count_neg/len(a))*100
print("The percentage of the negative numbers is: ", percent, "%")