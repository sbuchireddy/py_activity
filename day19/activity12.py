with open("original.txt", "r") as file:
    lines = file.readlines()

lines.reverse()

with open("reversed.txt", "w") as file:
    file.writelines(lines)