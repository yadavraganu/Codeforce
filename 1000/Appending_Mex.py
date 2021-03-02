n=int(input())
arr=list(map(int,input().split()))
step=0
mx=0
for i in range(n):
    if arr[0]==0:
        if arr[i]-mx>1:
            print(step+1)
            break
        else:
            step+=1
    else:
        print(1)
        break
    mx=max(arr[i],mx)  
if step==n:
    print(-1)