
def bank(a, years):
    arr = []
    b=years
    while b :
        arr.append(b)
        b=b-1

    for i in arr:
        a+=a/100*3
    print(a)

bank(4000,10)