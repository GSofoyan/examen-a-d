lijst=[]
count=0
for i in range(0,10):
    getal= int(input())

    if getal%3==0:
        count+=1

    lijst.append(getal)
maximum = int(max(lijst))
minim = int(min(lijst))
print(f'''grootste: {maximum}
kleinste: {minim}
drievouden: {count}''')
