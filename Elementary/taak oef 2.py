total= float(input("Enter the total amount:"))
tip= float(input("Enter the tip percentage you wish to give:"))

total_tip= total+(tip/100*total)
afgerond= int(total_tip*100)/100
print("Total amount including tip: €"+str(afgerond))