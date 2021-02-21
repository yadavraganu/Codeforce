for i in range(int(input())):
    string=input().strip()
    final_string=''
    Flag=True
    for k in string:
        if Flag and ord(k)>ord('a'):
            final_string+='a'
            Flag=False
        elif Flag and ord(k)==ord('a'):
            final_string+=chr(ord(k)+1)
            Flag=False
        elif not (Flag) and ord(k)<ord('z'):
            final_string+='z'
            Flag=True
        elif not (Flag) and ord(k)==ord('z'):
            final_string+=chr(ord(k)-1)
            Flag=True
    print(final_string)



