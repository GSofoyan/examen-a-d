
def sort(lijst: list):
    sort_helper(lijst,0,len(lijst)-1)


def sort_helper(lijst,first,last):
    if last>=first:
        pivotindex=partition(lijst,first,last)
        sort_helper(lijst,first,pivotindex-1)
        sort_helper(lijst,pivotindex+1,last)

def partition(lijst,first,last):
    pivot=lijst[first]
    low= first+1
    high=last
    while high>low:
        while low<=high and lijst[low]<=pivot:
            low+=1

        while high>=low and lijst[high]>pivot:
            high-=1

        if low<high:
            lijst[high],lijst[low]=lijst[low],lijst[high]
    while first<high and lijst[high]>=pivot:
        high-=1

    if pivot>lijst[high]:
        lijst[first]=lijst[high]
        lijst[high]=pivot
        return high
    else:
        return first

