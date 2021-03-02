for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    find_1=arr.index(1)
    find_2=arr.index(1)
    check_clock=True
    check_anticlock=True
    for i in range(n-1):
        if arr[find_1]+1==arr[(find_1+1)%n]:
            check_clock=True
        else:
            check_clock=False
            break
        find_1=(find_1+1)%n
    for j in range(n-1): 
        if arr[find_2]+1==arr[(find_2-1)%n]:
            check_anticlock=True
        else:
            check_anticlock=False
            break
        find_2=(find_2-1)%n
    if check_anticlock or check_clock:
        print('YES')
    else:
        print('NO')             