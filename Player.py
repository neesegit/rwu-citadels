import District
import random

class Player:
    def __init__(self, name):
        self._name = name
        self._treasure = 0
        self._nbDistrict = 0
        self._city = []
        self._hand = []
        self._possessedCrown = False

    @property
    def Name(self):
        return self._name
    
    @property
    def Treasure(self):
        return self._treasure
    
    @property
    def NbDistrict(self):
        return self._nbDistrict
    
    @property
    def City(self):
        return self._city
    
    @property
    def Hand(self):
        return self._hand
    
    def NbDistrictInHand(self):
        return len(self._hand)
    
    @property
    def PossessedCrown(self):
        return self._possessedCrown
    
    @PossessedCrown.setter
    def PossessedCrown(self, crown):
        self._possessedCrown = bool(crown)
    
    def AddCoins(self, nbCoins):
        if nbCoins > 0 :
            self._treasure += nbCoins
    
    def RemoveCoins(self, nbCoins):
        if 0 < nbCoins <= self._treasure:
            self._treasure -= nbCoins

    def AddDistrictInCity(self, district):
        if len(self._city) < 8 :
            self._city.append(district)
            self._nbDistrict += 1

    def DistrictPresentInCity(self, name):
        for district in self._city:
            if district.Name == name :
                return True
        return False

    def RemoveDistrictFromCity(self, name):
        for district in self._city:
            if district.Name == name:
                self._city.remove(district)
                return district
        return None
    
    def AddDistrictInHand(self, district):
        self._hand.append(district)
    
    def RemoveDistrictFromHand(self):
        if self.NbDistrictInHand != 0 :
            self._hand.remove(self._hand[random.randint(0,self.NbDistrictInHand -1)])

    def Reset(self):
        self.RemoveCoins(self._treasure)
        while self.NbDistrictInHand != 0 :
            self._hand.remove[0]
        while len(self._city) != 0:
            self._hand.remove[0]
        self._nbDistrict = 0