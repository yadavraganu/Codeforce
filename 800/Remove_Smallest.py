for i in range(int(input())):
    length=int(input())
    array=sorted(list(map(int,input().split())))
    temp='YES'
    for i in range(0,length-1):
        if array[i+1]-array[i]>1:
            temp='NO'
            break
        else:
            temp='YES'
    print(temp)        