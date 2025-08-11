def safe_division():
    numerator = int(input("Enter numerator: "))
    
    while True:
        try:
            denominator = int(input("Enter denominator: "))
            result = numerator / denominator
            print("Result:", result)
            break
        except ZeroDivisionError:
            print("Cannot divide by zero!")
print(safe_division())