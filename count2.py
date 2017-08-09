import sys
st = sys.argv[1]

l = st.split()
c = 0
for i in l:
    if i.isalnum():
        c+=1

print(c)