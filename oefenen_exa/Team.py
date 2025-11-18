class Team:
    def __init__(self, name,points=0):
        self.__name = name
        self.__points = points
        self.__members = []
    def get_members(self):
        return self.__members
    def get_name(self):
        return self.__name
    def get_points(self):
        return self.__points
    def add_points(self, amount):
        self.__points += amount
    def set_name(self, newName):
        self.__name = newName
    def add_member(self, name:str):
        self.__members.append(name)
    def contains_member(self, name:str):
        return name in self.__members
    def remove_member(self, name:str):
        self.__members.remove(name)

