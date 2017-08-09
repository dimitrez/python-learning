import sys
st = sys.argv[1]
m = 0
w = 0
for i in range(len(st)):
    if st[i] == 'w':
        w+=1
    elif st[i] == 'm':
        m+=1
    else:
        continue
sk1 = '('
sk2 = ')'

print('m ('+str(m)+')', '*' * m)
print('w ('+str(w)+')', '*' * w)