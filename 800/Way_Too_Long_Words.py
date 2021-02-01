import sys 
lnr=int(sys.stdin.readline())
wordlst=[]
for lines in range(lnr):
    word=sys.stdin.readline().strip()
    wordlst.append(word)
for word in wordlst:    
    if len(word)>10:
        print(word[0]+str(len(word)-2)+word[-1])
    else:
        print(word)