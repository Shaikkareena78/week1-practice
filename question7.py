values = [10, 10, 20, 20, 20, 30, 10, 10, 40]
result=[]
for i in range(len(values)-1):
        if values[i]!=values[i+1]:
            result.append(values[i])
result.append(values[-1])
print(result)
            