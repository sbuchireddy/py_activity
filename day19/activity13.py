try:
    with open("guests.txt", "r") as file:
        print("Current guests:")
        print(file.read())
except FileNotFoundError:
    print("Guest list is empty.")

new_guest = input("Enter a new guest's name: ")

with open("guests.txt", "a") as file:
    file.write(new_guest + "\n")
 
print(f"{new_guest} has been added.")