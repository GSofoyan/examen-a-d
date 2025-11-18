woord= str(input("Enter a string:"))
s= woord.lower()
def palindroom(s):
    i=0
    l=-1
    Ispal = True #gaan vanuit dat het zo is en we gaan bij elke letter dan zien of het correct is
    for i in range(0,int(len(s)/2)-1): #helft van woord checken (-1 omdat index vanaf 0)
        if s[i]!=s[l]:
            Ispal = False
            break #moet rest niet meer checken
        l -= 1 #als ze wel gelijk zijn, i+1 checken en moet l -1, als het afloopt en alles is gelijk blijft Ispal als True
    if Ispal == True:
        print(f"The string {woord} is a palindrome.")
    else:
        print(f"The string {woord} is not a palindrome.")
palindroom(s)



