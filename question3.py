n=int(input("enter number:"))
result=0
even=0
odd=0
for i in range(1,11):
    result=n*i
    print(n,"*",i,"=",result,"-",end="")
    if result%2==0:
        even+=1
        print("even")
    else:
        odd+=1
        print("odd")
print("Even Results:",even)
print("Odd Results:",odd)