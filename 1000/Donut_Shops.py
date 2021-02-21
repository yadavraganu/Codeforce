for i in range(int(input())):
    arr=list(map(int,input().split()))
    a=arr[0]
    b=arr[1]
    c=arr[2]
    if a<c:
        a1="1"
    else:
        a1="-1"    
    if c<a*b:
        b1=b
    else:
        b1='-1'
    print(str(a1)+" "+str(b1))    