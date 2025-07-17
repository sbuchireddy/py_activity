text="amazing python language"
text=text.replace(" ","")
text.upper()
text=text.replace('A','XXX')
print(text[::3][::-1])