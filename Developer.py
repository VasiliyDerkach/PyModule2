class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor):
        if 1<= new_floor<= self.number_of_floors:
            print('Этаж ', new_floor)
        else:
            print("Такого этажа не существует")

home1= House('ЖК Эльбрус', 30)
home1.go_to(2)
home1.go_to(35)


