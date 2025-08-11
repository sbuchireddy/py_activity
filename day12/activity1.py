user_input = input("enter something:")
result1=("given number is even","given number is odd")[int(user_input)%2]or false
result2=("length of the float number",len(str(user_input)))or false
result3=("given string is palindrome","given string is not a palindrome")[user_input != user_input[::-1]] or false
final_output=result1 or result2 or result3 or "not valid"
print(final_output)


#print((("given string is palindrome","given string is not a palindrome")[user_input != user_input[::-1]]*user_input.isalpha()) or (("given number is even","given number is odd")[int(user_input)%2]*user_input.isdigit()) or "not valid")



