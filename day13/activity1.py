'''
marks=int(input("Enter Marks:"))
cutoff=int(input("Enter pass marks:"))
if (marks>=cutoff):
   print("pass")
else:
   print("fail")
'''

'''
#sol2:
marks=int(input("Enter Marks:"))
cutoff=int(input("Enter pass marks:"))
if str(marks-cutoff)[0] not in ['-']
print("pass")
'''

'''
marks=int(input("Enter Marks:"))
cutoff=int(input("Enter pass marks:"))
diff = marks-cutoff
x=max(0,diff)
if x:
   print("pass")
else:
   print("fail")
'''

marks=int(input("Enter Marks:"))
cutoff=int(input("Enter pass marks:"))
diff = cuttoff-marks
x=diff+abs(diff)
if not x:
	print("pass")
