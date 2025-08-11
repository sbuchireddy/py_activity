students={'Alice','Bob','Charlie'}
new_entries=['Charlie_ash','Diana','Eve','Bob_weasley','Frank']
students.update(['Charlie_ash','Diana','Eve','Bob_weasley','Frank'])
print(students)

students={'Alice','Bob','Charlie'}
before=len(students)
new_entries=['Charlie','Diana','Eve','Bob','Frank']
students.update(new_entries)
after=len(students)
print(students)
print(after-before)