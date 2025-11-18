def display_average_hours(weekly_hours_table):
    averages = []

    # Stap 2: Itereer door de werknemers (rijen in de tabel)
    for i, hours in enumerate(weekly_hours_table):
        # Bereken het gemiddelde voor de huidige werknemer
        average_hours = sum(hours) / len(hours)
        # Voeg het werknemer-ID en gemiddelde toe aan de lijst
        averages.append((i + 1, average_hours))
    sorted_averages = sorted(averages, key=lambda x: (x[1],x[0]), reverse=True) #key is om aan te duiden op welke index je wilt sorteren: wij willen averages dus 2e is [1] dan sorteren op [0]
                                                                        #reverse om van hoog naar laag                        ^aangezien we 2 gegevens hebben per element
    # Print de header
    print("Employee, Average Daily Hours")
    print("---------------------------------")

    # Print elke werknemer met hun gemiddelde uren
    for employee, avg_hours in sorted_averages:
        print(f"Employee {employee}\t{avg_hours:.2f} hours")         #employee is eerste gegeven WN-ID
