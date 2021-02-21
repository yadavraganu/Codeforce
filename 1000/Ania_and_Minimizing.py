arr=list(map(int,input().split()))
n=arr[0]
k=arr[1]
number=list(map(int,list(input())))
min1=number
for i in range(0,len(number)):
    if k>0:
        if len(number)==1:
            min1[0]=0
        elif i==0 and number[i]>1:
            min1[i]=1
            k-=1
        elif i>0 and number[i]>0:    
            min1[i]=0
            k-=1
print(''.join(map(str,min1)))