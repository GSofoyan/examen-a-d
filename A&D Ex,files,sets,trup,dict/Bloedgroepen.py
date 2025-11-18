ABO_combos = {                      #tabellen zetten in dict (als ik A A heb weet ik dat dat A geeft)
    ('A', 'A'): 'A',                #                               =key
    ('A', 'B'): 'AB',
    ('B', 'A'): 'AB',
    ('A', 'O'): 'A',
    ('O', 'A'): 'A',
    ('B', 'B'): 'B',
    ('B', 'O'): 'B',
    ('O', 'B'): 'B',
    ('O', 'O'): 'O'
}

Rhesus_combos = {
    ('+', '+'): '+',
    ('+', '-'): '+',
    ('-', '+'): '+',
    ('-', '-'): '-'
}


ABO_optie = {                      #als vader bv A is heeft hij mogelijke optie A of O om door te geven
    'A': ['A', 'O'],
    'B': ['B', 'O'],
    'AB': ['A', 'B'],
    'O': ['O', 'O']
}

Rhesus_optie = {
    '+': ['+', '-'],
    '-': ['-']
}

def bloedgroep_kind(vader, moeder):

    resultaten= set()

    vader_opties= ABO_optie[vader[:-1]]   #van begin tot en zonder laatste (voor bv AB-)
    vader_optiesR= Rhesus_optie[vader[-1]]
    moeder_opties=ABO_optie[moeder[:-1]]
    moeder_optiesR= Rhesus_optie[moeder[-1]]

           #nu hebben we geg. omgezet in mogelijke opties per persoon, nu checken mogelijke te maken combos

    for x in vader_opties:
        for y in moeder_opties:
            bloedgroep_combo= ABO_combos.get((x, y))
            for i in vader_optiesR:
                for j in moeder_optiesR:
                    bloedgroep_R= Rhesus_combos.get((i,j))
                    resultaten.add(bloedgroep_combo + bloedgroep_R)

    return resultaten

def bloedgroep_ouder(ouder, kind):

    mogelijk= set()
    alle_bgn= ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

    for bg in alle_bgn:
        if kind in bloedgroep_kind(bg, ouder):     #we stellen dat vader een bg heeft, als die bg en moeder de bg van de kind kunnen maken : is dit een mogelijke bg voor de vader
            mogelijk.add(bg)

    return mogelijk