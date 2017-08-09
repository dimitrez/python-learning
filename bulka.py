import sys
st = sys.argv[1].split(',')

last = st.pop()

print(', '.join(st).capitalize()+' и',last+'.')