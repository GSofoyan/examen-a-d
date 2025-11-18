class Galgje:
    def __init__(self, woord,beurten=6):
        self.woord = woord
        self.beurten = beurten
        self.geraden=["."]
        self.geraden = self.geraden * len(self.woord)   #maak lijst met punten met legnte van woord
        self.geprobeerd=""                              #om bij te houden welke allemaal geprobeerd zijn

    def raadLetter(self,letter):
        if self.beurten==0 or "." not in self.geraden:      #als beurten al op zijn of je hebt geraden moet deze methode niet meer runnen
            print("Sorry, het spel is reeds voorbij.")
            return None

        assert isinstance(letter,str), "argument is geen letter"
        assert len(letter)==1,"argument is geen letter"
        assert letter not in self.geprobeerd,"letter is al eens geprobeerd"



        self.geprobeerd+=str(letter)                            #als alle checks passeren is het letter geprobeerd
        if letter in self.woord.lower():
            for i in range(len(self.woord)):
                if self.woord.lower()[i] == letter:
                    self.geraden[i]=self.woord[i]
            print(f"Correct: letter {letter} komt {self.woord.lower().count(letter)} keer voor in het woord.")
            if "." in self.geraden:     #als je nog niet alles hebt
                if self.beurten==1:
                    print(f"Je hebt nog {self.beurten} beurt.")                 #opsplitsing want "beurt" of "beurten"
                    for x in self.geraden:
                        print(x,end="")
                    print()
                else:
                    print(f"Je hebt nog {self.beurten} beurten.")
                    for x in self.geraden:
                        print(x, end="")
                    print()

            else:                                               #je hebt wel al alles
                print("Proficiat! Je hebt het woord geraden!")
                print(self.woord)

        else:                                                     #het was fout
            print(f"Fout: letter {letter} komt niet voor in het woord.")
            self.beurten-=1
            if self.beurten==0:
                print("Ai, je bent opgehangen.")
                print(self.woord)
            else:                               #je hebt nog beurten en spel is nog niet gedaan
                if self.beurten==1:
                    print(f"Je hebt nog {self.beurten} beurt.")
                    for x in self.geraden:
                        print(x, end="")
                    print()
                else:
                    print(f"Je hebt nog {self.beurten} beurten.")
                    for x in self.geraden:
                        print(x, end="")
                    print()
    def __str__(self):
        geraden_woord =""
        for x in self.geraden:          #om bij return te kunnen droppen als woord (daar mag geen print van elke element
            geraden_woord += x

        if "." in self.geraden:
            if self.beurten!=0:
                if self.beurten==1:
                    return f"Je hebt nog {self.beurten} beurt." + "\n" + geraden_woord
                else:
                    return f"Je hebt nog {self.beurten} beurten." + "\n" + geraden_woord

            else:
                return f"Ai, je bent opgehangen." + "\n" + self.woord


        else:
            return f"Proficiat! Je hebt het woord geraden!" + "\n" + self.woord











