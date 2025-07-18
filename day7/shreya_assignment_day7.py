num = int((num := input("enter the number:")).isdigit() and num or input("enter numeric value:"))
print((num%7==0 and num%5==0 and num%3==0 and "jugs mugs bugs") or (num%5==0 and num%3==0 and "jugs mugs") or (num%5==0 and num%7==0 and "mugs bugs")
or (num%3==0 and num%7==0 and "jugs bugs") or (num%7==0 and "bugs") or (num%5==0 and "mugs") or (num%3==0 and "jugs") or num)