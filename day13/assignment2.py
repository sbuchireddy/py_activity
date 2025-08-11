marks=int(input("Enter Marks:"))
cutoff=int(input("Enter pass marks:"))
diff=marks-cutoff
flag=(diff+abs(diff))//(abs(diff)+1)
if flag:
    print("pass")
else:
    print("fail")