for i in range(int(input())):
    k=int(input())
    if k<10 and k>0:
        print('1')
        print(k)
    elif int(str(k)[::-1])==int(str(k)[0]):
        print('1')
        print(k)
    else:
        a=[str(int(str(k)[g])*10**(len(str(k))-g-1)) for g in range(0,len(str(k))) if str(int(str(k)[g])*10**(len(str(k))-g-1))!='0']
        print(len(a))
        print(' '.join(a))
                