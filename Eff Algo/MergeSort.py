def mergesort(lst):
    if len(lst) > 1:    #blijf splitsen tot len 1 is van elke deel

        first = lst[:len(lst) // 2]
        second = lst[len(lst) // 2:]
        mergesort(first)
        mergesort(second)

        merge(first, second, lst)

    return lst

def merge( l1, l2, temp):
    current1, current2,current3 = 0, 0,0

    while current1 < len(l1) and current2 < len(l2):
        if l1[current1] < l2[current2]:
            temp[current3] = l1[current1]
            current1 += 1
            current3 += 1
        else:
            temp[current3] = l2[current2]
            current2 += 1
            current3 += 1

    while current1 < len(l1):       #dus l2 niet meer en zit dus volledig in temp, dus moeten we gwn rest van l1 invullen
        temp[current3] = l1[current1]
        current1 += 1
        current3 += 1

    while current2 < len(l2):         #als l1 er al fully inzit
        temp[current3] = l2[current2]
        current2 += 1
        current3 += 1

