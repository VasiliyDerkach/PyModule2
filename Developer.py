class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor):
        if 1<= new_floor<= self.number_of_floors:
            for i in range(1,new_floor+1):
                print('Этаж ', i)
        else:
            print("Такого этажа не существует")

home1= House('ЖК Эльбрус', 30)
home1.go_to(5)
home1.go_to(35)
h2 = House('Домик в деревне', 2)
h2.go_to(5)


