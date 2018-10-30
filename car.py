class Car:
    _all = []

    def __init__(self, make, model, year, owner):
        Car._all.append(self)
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner
        #remember to associate a car with its owner

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make):
        self._make = make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def year(self):
        return self._year

    @model.setter
    def year(self, year):
        self._year = year

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner
