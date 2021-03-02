arr=input().split()
n,k=int(arr[0]),int(arr[1])
arr1=input().split()
same=0
m=1
for i in range(n-1):
    if arr1[i]!=arr1[i+1]:
        same+=1
        m=max(m,same+1)
    elif arr1[i]==arr1[i+1]:
         same=0   
if n==1:
    print(1)
else:
    print(m)             