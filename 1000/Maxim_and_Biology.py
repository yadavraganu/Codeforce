n=int(input())
string=input()
gnome=[ord('A'),ord('C'),ord('T'),ord('G')]
result=[]
for i in range(len(string)-3):
    gnome_new=[ord(string[i]),ord(string[i+1]),ord(string[i+2]),ord(string[i+3])]
    a=list(map(lambda x:(26-abs(x[0]-x[1])) if abs(x[0]-x[1])>13 else abs(x[0]-x[1]),zip(gnome_new,gnome)))
    result.append(sum([1 if x==25 else x for x in a]))
print(min(result))