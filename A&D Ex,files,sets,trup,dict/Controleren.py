try:
    numlist = [100, 101, 0, "103", 104]

    i1 = int(input("Give an index: "))
    print("100 /", numlist[i1], "=", 100 / numlist[i1])

except ZeroDivisionError as ex:         #op dit manier geeft hij zelf gwn error uitleg bij type
    print("Fout: ",ex)

except TypeError as ex:
    print("Fout: ", ex)

except IndexError as ex:
    print("Fout: ", ex)

except ValueError as ex:
    print("Fout: ", ex)




