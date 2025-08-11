'''
score=int(input("enter the score"))
if score>=90:	
	print("grade='A'")
	print("excellent")
elif score>=80:	
	print("grade='B'")
	print("good job")
elif score>=70:	
	print("grade='C'")
	print("satisfactory")
elif score>=60:	
	print("grade='D'")
	print("needs improvement")
else:	
	print("grade='E'")
	print("please study more")
'''

score=int(input("enter the score"))
grades={
    'A':"excellent",
    'B':"good job",
    'C':"satisfactory",
    'D':"needs improvement",
    'E':"please study more"}
if score>=90:    
    grade='A'
elif score>=80:    
    grade='B'
elif score>=70:    
    grade='C'
elif score>=60:    
    grade='D'
else:    
    grade='E'
print("student grade is:",grade,grades[grade])
