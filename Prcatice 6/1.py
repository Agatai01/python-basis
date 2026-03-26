a=int(input())
b=list(map(int, input().split()))
c=True 
for i in b: 
    if i<0: 
        c=False
        break
    else: 
        c=True
if c: 
    print("Yes") 
else: 
    print("No")