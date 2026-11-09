n = int(input("Enter the number of numbers: "))
count = 0
sum = 0
positive = 0
if n<=0:
    print("Invalid input for n!")
else:
    for i in range(n):
        num = int(input("Enter a number: "))
        if (num%3==0):
            count += 1
        if (num >0):
            sum += num
            positive = 1
print("The count of the numbers that are divisible by 3 is: ", count)
avg = sum/n
if positive == 1:
    print("The average of the positive numbers is: ", avg)
else:
    print("No positive numbers were entered.")