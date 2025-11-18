def som_delers(n):
    sum=1
    deler=2
    while deler <n:
        if n%deler==0:
            sum+=deler
        deler+=1
    return sum
def getalsoort(n):
    if n == som_delers(n):
        return (f'perfect')
    elif n > som_delers(n):
        return (f'gebrekkig')
    else:
        return (f'overvloedig')

