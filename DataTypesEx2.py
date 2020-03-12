Num = [56, 78, 34, 21, 56, 34, 125, 45, 89, 75, 12, 12, 56]
Sum = [56+78+34+21+56+34+124+45+89+75+12+56]
print(Sum)
Num = [56, 78, 34, 21, 56, 34, 125, 45, 89, 75, 12, 12, 56]
Num.sort()
print(Num)
print("Smallest element is:", min(Num))
print("Largest element is:", max(Num))
Num = list(dict.fromkeys(Num))
print(Num)

strName = input("Please enter your First name")
strSurname = input("Please enter your surname")
print(strName + " " + strSurname)
number1 = int(input("Please enter a number"))
number2 = int(input("please enter a other number"))
answer = number1 + number2
print(answer)