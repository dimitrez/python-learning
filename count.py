import sys
st = sys.argv[1]
ch = sys.argv[2]
a = 0

for i in range(len(st)):
    if st[i] == ch:
        a+=1
    else:
        continue
print(a)