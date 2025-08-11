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