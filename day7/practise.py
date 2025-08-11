tuple1=(1,2,3,[8,10])
tuple1[3][0]=45
print(tuple1)

num=int(input("enter a number:"))
print(("jugs"*(num%3==0)) or num)


num=(input("enter a number:"))
print((num.isdigit() and "jugs") or (input("enter correct int:").isdigit() and "jugs") or "please enter correct int")

val = int((num := input("Enter the number: ")).isdigit() and num or input("Enter numeric value: "))
print((val % 3 == 0 and "jugs") or val)