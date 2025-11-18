def calculate_current_ratio(activa,vord,schuld,passiva):
    current_ratio = round((activa-vord)/(schuld+passiva),2)
    return "De current ratio van de onderneming bedraagt: " + str(current_ratio)

def calculate_acid_test_ratio(activa,vord,schuld,voorraad):
    acid_test_ratio = round((activa-vord-voorraad)/schuld,2)
    return "De acid test ratio van de onderneming bedraagt: " + str(acid_test_ratio)


