'''
Write a  program or function that validates user password with the following requirements:
Password ≠ username
Password ≠ first name or last name
At least 10 characters
Must be alphanumeric (letters and numbers)
Must include both uppercase and lowercase letters
'''
username=input("enter username:")
password=input("enter password:")
first_name=input("enter first name:")
last_name=input("enter the last name:")
if password==username:
	print("password and username should not be same:")
elif password==first_name:
	print("password should not be same as first name:")

elif password==last_name:
	print("password should not be same as last name:")
elif len(password)>=10:
	print("password should be atleast 10 chars:")
elif not password.isalnum():
	print("password must contai both letters and numbers")
elif not any(password.isalpha()):
	print("password must contai at least one letter")
elif not any(password.isdigit()):
	print("password must contai atleast one number")
elif not any(password.isupper()):
	print("password must contain atleast one upper case letter:")
elif not any(password.islower()):
	print("password must contain atleast one lower case:")
else:
	print("password is valid!")
 