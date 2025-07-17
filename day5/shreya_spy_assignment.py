codes=input().split(' ')
selected = codes[1::3]
selected_reversed = selected[::-1]
message = ''.join(chr(int(code)) for code in selected_reversed)
print(message)