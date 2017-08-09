f = open("queue.txt", 'r')

s=f.read()
s=s.split()
m = max(s)
s.remove(max(s))
s.insert(0,m)
print(' '.join(s))