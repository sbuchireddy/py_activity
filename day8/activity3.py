students={
"Anitha":{"Math":95,"Science":89},
"Ravi":{"Math":80,"Science":92},
"Pavi":{"Math":88,"Science":85}
}

name=input("enter student name:")
subject=input("enter subject:")
print(students.get(name,{}).get(subject,"invalid input"))
