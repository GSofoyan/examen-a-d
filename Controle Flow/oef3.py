import random

random.seed(1)
lotto= random.randint(0,99)
guess= int(input("Enter your lottery pick (two digits):"))
d1_g= guess//10
d2_g= guess%10
d1_l= lotto//10
d2_l= lotto%10
print("The lottery number is",lotto)
if  guess==lotto:
    print("Exact match: you win 10.000 €")
elif d1_g==d2_l and d2_g==d1_l:
    print("Match all digits: you win 3.000 €")
elif d1_g==d1_l and d2_g!=d2_l:
    print("Match one digit: you win 1,000 €")
elif d1_g==d2_l and d2_g!=d1_l:
    print("Match one digit: you win 1,000 €")
elif d2_g==d1_l and d1_g!=d2_l:
    print("Match one digit: you win 1,000 €")
elif d2_g==d2_l and d1_g!=d1_l:
    print("Match one digit: you win 1,000 €")
else:
    print("Sorry, no match")