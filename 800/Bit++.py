import sys 
a=sys.stdin.readline()
operation=[]
result=0
for i in range(int(a)):
    a=sys.stdin.readline()
    x,y=a.split('X')[0].strip(),a.split('X')[1].strip()
    if x=='++' or y=='++':
        result+=1
    if x=='--' or y=='--':
        result-=1    
print(result)