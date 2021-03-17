from .Class import Auto



class SuperCar:

    def __init__(self,cost):
        self.cost = cost

    def start_engine(self):
        print("VRRRRRRRRRROOOOOOMMMMM!")


class Car(Auto,SuperCar):

    def __init__(self,type_of,mileage):
        self.type = type_of
        self.mileage = mileage

    def start(self):
        print("Vroom")