# put your python code here
num1 = int(input())
num2 = int(input())
num3 = int(input())

desk1 = num1 % 2 + (num1 - num1 % 2) / 2
desk2 = num2 % 2 + (num2 - num2 % 2) / 2
desk3 = num3 % 2 + (num3 - num3 % 2) / 2

print(int(desk1 + desk2 + desk3))
