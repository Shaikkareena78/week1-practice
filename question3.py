n=int(input("enter number:"))
result=0
for i in range(1,11):
    result=n*i
    print(n,"*",i,"=",result,"-",end="")
    if result%2==0:
        print("even")
    else:
        print("odd")
print()