import sys
l = sys.argv[1:]

a=l[0]

for i in range(len(l)):
    if int(a) < int(l[i]):
        a = l[i]

print(a)