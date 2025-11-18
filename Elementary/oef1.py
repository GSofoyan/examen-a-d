massa_in_kg = int(input("Massa?"))
lichaamslengte_in_cm = int(input("Lichaamslengte?"))
leeftijd_in_jaren = int(input("Leeftijd?"))
BMR_M = 66.4730+(13.7516 * massa_in_kg)+(5.0033 * lichaamslengte_in_cm)-(6.7550 * leeftijd_in_jaren)
BMR_V = 655.0955 + (9.5634 * massa_in_kg) + (1.8496 * lichaamslengte_in_cm) - (4.6756 * leeftijd_in_jaren)

print("Een man moet dagelijks",BMR_M/230,  "chocoladerepen eten om zijn gewicht te behouden.")
print("Een vrouw moet dagelijks",BMR_V/230,  "chocoladerepen eten om haar gewicht te behouden.")