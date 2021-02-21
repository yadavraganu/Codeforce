inp=list(map(int,input().split()))
x,y,z=inp[0],inp[1],inp[2]
if (x%z+y%z)//z>=1:
    if x%z>y%z:
        n=z-(x%z)
    elif y%z>x%z:
        n=z-(y%z)
    else:
        n=z-x%z    
else:
    n=0        
if x%z==0 and y%z==0:
    print(str((x+y)//z)+' 0')
else:
    print(str((x+y)//z)+' '+str(n))
