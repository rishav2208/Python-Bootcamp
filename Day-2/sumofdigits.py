#simple py script to sum the digits of a number

num=input("Enter any number:")
sum=0
for i in range(len(num)):
    sum=sum + int(num[i])

print("sum of digits=", sum)