def arithmetic(a,b,c):
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    elif c == '/':
        return a/b
    else:
        return 'Неизвестная операция'


print(arithmetic(1,2,'/'))