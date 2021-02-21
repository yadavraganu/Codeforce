number=int(input())
event=list(map(int,input().strip().split()))
crime=0
recruit=0
untreated=0
for i in event:
    if i>0 & recruit<10:
        recruit+=i
        crime=0
    elif i<0:
        crime+=1
        recruit-=1
    if recruit<0:
        untreated+=1
        recruit=0    
print(untreated)           

