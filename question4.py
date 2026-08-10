text=input("Enter text:")
upper=0
lower=0
digits=0
spaces=0
others=0
for i in range(len(text)):
    if text[i].isupper():
        upper+=1
    elif text[i].islower():
        lower+=1
    elif text[i].isdigit():
        digits+=1
    elif text[i]==" ":
        spaces+=1
    else:
        others+=1
print("Uppercase Letters:",upper)
print("Lowercase Letters:",lower)
print("Digits:",digits)
print("spaces:",spaces)
print("Others Charachters:",others)