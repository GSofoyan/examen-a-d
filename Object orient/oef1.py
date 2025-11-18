from enum import Enum


class SoccerPlayer:
    # The position a player can play on the pitch.
    position = Enum("position", ["GK",  # Goalkeeper
                                 "DF",  # Defender
                                 "MF",  # Midfield
                                 "FW"  # Forward
                                 ])

    def __init__(self, first_name, last_name, age, position):
        """
        SoccerPlayer constructor.

        :param first_name: the first name of the player
        :param last_name: the last name of the player
        :param age: the player's age
        :param position: the position on the pitch
        """
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.position = position

    def __lt__(self, other):
        """
        Compare two SoccerPlayer objects based on their names.

        :param other: the other SoccerPlayer object to compare
        :return: True if their names are equal, False otherwise
        """
        return self.get_name().casefold() == other.get_name().casefold()

    def __eq__(self, other):
        """
        Check if two SoccerPlayer objects are equal.

        :param other: the other object to compare
        :return: True if self is equal to other, False otherwise
        """
        if self is other:
            return True
        if not isinstance(other, SoccerPlayer):
            return False
        return (
                self.age == other.age and
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.position == other.position
        )

    def get_age(self):
        """
        Get the age of the player.

        :return: the age
        """
        return self.age

    def get_name(self):
        """
        Get the full name of the player.

        :return: the full name
        """
        return f'{self.first_name} {self.last_name}'

    def get_position(self):
        """
        Get the position of the player.

        :return: the position
        """
        return self.position

    def __hash__(self):
        """
        Compute the hash value of the SoccerPlayer object.

        :return: the hash value
        """
        return hash((self.age, self.first_name, self.last_name, self.position))

    def __str__(self):
        return self.get_name()


class SoccerTeam:
    SIZE = 11

    ## JOU CODE KOMT HIER

    def __init__(self, name: str):


        self.name = name
        self.players = []  # Lijst om spelers op te slaan

    def add_player(self, player: 'SoccerPlayer') -> bool:

        #Voeg een speler toe aan het team als er plaats is en de speler nog niet in het team zit.


        if len(self.players) < self.SIZE and player not in self.players:
            self.players.append(player)
            return True
        return False

    def get_average_age(self) -> float:
        #0.0 als er geen spelers zijn.

        if not self.players:
            return 0.0
        total_age = sum(player.get_age() for player in self.players) #neem som van de ages voor elke element in list
        return float(f"{total_age / len(self.players):.2f}")           #delen door lengte

    def get_formation(self) -> str:


        defenders = sum(player.get_position() == SoccerPlayer.position.DF for player in self.players)   #tel (sum van de TRues) hoeveel positie van elke element in list == "DF"
                                                                                                        # (kon ook met "count" werken)                            maar ipv zo te noteren moeten we == SoccerPlayer.position.DF DIT HEEFT TE MAKEN MET "ENUM" die bovenaan in code gebruikt werd
        midfielders = sum(player.get_position() == SoccerPlayer.position.MF for player in self.players)
        forwards = sum(player.get_position() == SoccerPlayer.position.FW for player in self.players)
        return f"{defenders}-{midfielders}-{forwards}"

    def get_name(self) -> str:

        return self.name

    def get_players(self) -> list:
        if len(self.players) == 0:
            return [None, None, None, None, None, None, None, None, None, None, None]   #voor verbetering ipv lege list
        return self.players

    def get_players_at(self, position: 'SoccerPlayer.position') -> list:

        return [player for player in self.players if player.get_position() == position]  #geef een lijst met spelers in self.players als hun posiite matched

                                                                                         #kon ook lijst=[] dan
                                                                                        #for player in list, if positie== append aan lijst[]

    def substitute(self, player_out: 'SoccerPlayer', player_in: 'SoccerPlayer') -> bool:

        if player_out not in self.players or player_in in self.players:
            return False
        if (player_out.get_position() == SoccerPlayer.position.GK and player_in.get_position() != SoccerPlayer.position.GK) or \
        (player_out.get_position() != SoccerPlayer.position.GK and player_in.get_position() == SoccerPlayer.position.GK):   #ook hier ==SoccerPlayer.position.GK ipv =="GK"
            return False
        self.players.remove(player_out)
        self.players.append(player_in)
        return True






