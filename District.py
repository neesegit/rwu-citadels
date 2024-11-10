class District:
    DISTRICTS_TYPE = {"RELIGIOUS", "MILITARY", "NOBLE", "MERCHANT", "WONDER"}

    def __init__(self, name="", type="", constructionCost=0, features=""):
        self._name = name
        self._type = type
        self._constructionCost = constructionCost
        self._features = features

    @property
    def Name(self):
        return self._name
    
    @Name.setter
    def Name(self, name):
        self._name = name
    
    @property
    def Type(self):
        return self._type
    
    @Type.setter
    def Type(self, type):
        if type in District.DISTRICTS_TYPE:
            self._type = type
        else:
            self._type = ""

    @property
    def ConstructionCost(self):
        return self._constructionCost
    
    @ConstructionCost.setter
    def ConstructionCost(self, cost):
        if 1 <= cost <= 6:
            self._constructionCost = cost
        else:
            self._constructionCost = 0
    
    @property
    def Features(self):
        return self._features
    
    @Features.setter
    def Features(self, features):
        self._features = features