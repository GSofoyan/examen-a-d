merknaam = input()
stad = input()
merknaamcheck = merknaam.lower()
stadcheck = stad.lower()
i_m = 0
i_s = 0
x=""
while i_m < len(merknaamcheck):
    if stadcheck[i_s] == merknaamcheck[i_m] and i_s <len(stadcheck):
        x+=f"[{merknaam[i_m]}]"
        i_m += 1
        i_s += 1
    else:
        x += f"{merknaam[i_m]}"
        i_m += 1
x=x.replace("][","")
print(x)