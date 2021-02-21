for i in range(int(input())):
    str1=input()
    str2=input()
    cnt=0
    for i in str1:
        if i in str2:
            cnt+=1
            break
    if cnt==0:
        print('NO')
    else:
        print('YES')                