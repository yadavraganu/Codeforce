for i in range(int(input())):
    number=int(input())
    if number%2==0:
        print(str(number//2)+' '+str(number//2))
    else:
        print(str(number-1)+' 1')    