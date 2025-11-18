import random
def kaartspel(seed):
    random.seed(seed)
    suits= ["Spades","Hearts", "Diamonds","Clubs"]
    ranks= ["Ace", "2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    deck=[x for x in range(0,52)]
    random.shuffle(deck)
    for i in range(4):
        suit=suits[deck[i]//13]
        rank=ranks[deck[i]%13]
        print(f"Card number {deck[i]} is {rank} of {suit}")



