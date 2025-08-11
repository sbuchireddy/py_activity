#passwordchecker
password = input("Enter password: ")
 
has_upper = False
has_lower = False
has_digit = False
has_special = False
 
if len(password) < 8:
    print("Weak")
else:
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True
 
    count = 0
    if has_upper:
        count += 1
    if has_lower:
        count += 1
    if has_digit:
        count += 1
    if has_special:
        count += 1
 
    if count <= 2:
        print("Weak")
    elif count == 3:
        print("Moderate")
    else:
        print("Strong")