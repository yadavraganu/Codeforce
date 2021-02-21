n=int(input())
List=[1,5,10,20,100]
def Num(n,List):
    d=List[-1]
    if n%d==0:
        return n//d
    List.pop()
    z=(n//d)+Num((n%d),List)
    return z
print(Num(n,List))