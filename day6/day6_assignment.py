data= (1,"aadhaar","pan_card","IFSC",20000)
transfer_amt = int(input("the amount to be transferred is:"))
data= (data[0],data[1],data[3],data[4]+2000)
print(data)


data= (1,"aadhaar","pan_card","IFSC",[20000,input()700,500])
data[4][0]=22000
print(data)