

#count number on text
words=0
letter=0
digits=0
text=input("enter your text")
for x in text:
    if x>="a" and x<="z":
        letter=letter+1
    elif x>="0" and x<="9":
        digits=digits+1
    elif x=='':
        words=words+1
print("totall letter",letter)
print("totall words",words+1)
print("totall digits",digits)
