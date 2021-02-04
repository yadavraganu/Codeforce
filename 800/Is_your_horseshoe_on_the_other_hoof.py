import sys
word=sys.stdin.readline().strip().split()
print(4-len(set(word)))
