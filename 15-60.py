def age(list_age):
    for i in list_age:
        print("for age", i, "need age", i/2+7)

def array():
    arr = []
    for i in range(15,60):
        arr.append(i)
    return arr

age(array())