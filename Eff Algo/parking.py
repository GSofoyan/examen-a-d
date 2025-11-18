import heapq


class PriorityQueue:
    def __init__(self):
        self.content = []

    def add(self, item):
        heapq.heappush(self.content, item)

    def peek(self):
        return self.content[0]

    def poll(self):
        return heapq.heappop(self.content) if len(self.content) > 0 else None

    def is_empty(self):
        return len(self.content) == 0

    def __str__(self):
        return str(heapq.nsmallest(len(self.content), self.content))


def simuleer_parking(plaatsen, bloktijd, klanten):
    # zet klanten in priority queue

    pq = PriorityQueue()
    for klant in klanten:
        pq.add(klant)

    parking = [[True, 0, 0] for x in range(
        plaatsen)]  # elke parking geeft aan of het vrij is,op welke tijdstip de laatste klant erin was en hoelang hij erin blijft
    tijd = 0  # gebruik voor lijst in lijst NIET [x,y,z] * 10 (is gwn 10x zelde lijst, alsje eentje aanpast, past alles aan)

    while len(pq.content) > 0:

        for i in range(plaatsen):

            if tijd - parking[i][1] >= parking[i][
                2]:  # als tijd-entry groter is dan tijd dat gene erin zat, is deze plaats weer vrij (eerder voor verdere iteraties)
                parking[i][0] = True

        for i in range(plaatsen):
            if parking[i][0]:
                parking[i][1] = tijd  # zet entry tijd parking op tijd
                parking[i][2] = pq.peek()[1]  # zet tijd dat gene in parking op shoptime klant (1ste in proprity
                parking[i][0] = False  # zet parking op false
                pq.poll()  # pop 1ste priority uit lijst
                break
            elif i == plaatsen - 1:  # je hebt laatste plaats gechecked en het was niet TRUE
                gone = pq.poll()  # zet priotity van dit klant op aankomst +bloktijd --> schuift op
                pq.add((gone[0] + bloktijd, gone[1]))

        # tijd = aankomsttijd volgende in queue, Tenzij het laatste is dan is het huidige tijd + shoptijd laatste (om te weten wie laatste blijft , neem je gwn max van tijd+ shoptijd van idereen die er op einde nog is)
        if len(pq.content) > 0:
            tijd = pq.peek()[0]
        else:
            tijd = max(parking[i][1] + parking[i][2] for i in range(plaatsen))

    return tijd
