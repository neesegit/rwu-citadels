import District, Player
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, rank, characteristics):
        self._name = name
        self._rank = rank
        self._characteristics = characteristics
        self._player = None
        self._assassinated = False
        self._stolen = False

    @property
    def Name(self):
        return self._name
    
    @property
    def Rank(self):
        return self._rank
    
    @property
    def Charateristics(self):
        return self._characteristics
    
    @property
    def Player(self):
        return self._player
    
    @Player.setter
    def Player(self, player):
        self._player = player
    
    @property
    def Assassinated(self):
        return self._assassinated
    
    def SetAssassinated(self):
        self._assassinated = True
    
    @property
    def Stolen(self):
        return self._stolen
    
    def SetStolen(self):
        self._stolen = True

    def AddCoins(self):
        if self._player != None and self._assassinated == False:
            self._player.AddCoins(2)

    def AddDistrict(self, newDistrict):
        if self._player != None and self._assassinated == False:
            self._player.AddDistrictInHand(newDistrict)

    def Build(self, newDistrict):
        if self._player != None and self._assassinated == False:
            self._player.AddDistrictInCity(newDistrict)

    def ReceiveSpecificResources(self):
        print("No specific resources received.")

    @abstractmethod
    def UseAbility(self):
        pass

    def Reset(self):
        self._player = None
        self._assassinated = False
        self._stolen = False