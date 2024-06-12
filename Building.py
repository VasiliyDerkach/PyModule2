class Building:
    def __init__(self, floor, vtype):
        self.numberOfFloors= floor
        self.buildingType= vtype
    def __eq__(self, other):
        return self.buildingType==other.buildingType and self.numberOfFloors==other.numberOfFloors

Khrush= Building(5,'Хрущевка')
Brezhn= Building(12,'Брежневка')
print(Khrush == Brezhn)

Khrush= Building(5,'Хрущевка')
Brezhn= Building(5,'Хрущевка')
print(Khrush == Brezhn)
