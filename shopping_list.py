l1 = open('shopping_list_1.txt')
l2 = open('shopping_list_2.txt')
l3 = open('shopping_list_3.txt')

ll = l1.read()+l2.read()+l3.read()

ll = ll.split('\n')
l2 = []
for i in ll:
    if i not in l2:
        l2.append(i)
l2.sort()
ll = '\n'.join(l2[1:])+"\n"

f = open('shopping_list.txt','w')
f.write(ll)