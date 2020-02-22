class Car():
    model = "None"
    year = "None"
    color = "None"
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color


class Passenger_Car(Car):
    def Limit(self):
        print("Speed limit is 90")


class Truck(Car):
    def Limit(self):
        print("Speed limit is 70")


if __name__ == '__main__':
    taxi = Passenger_Car("Lada Priora", "2013", "black")
    track = Truck("MAN", "2016", "red")
    track.Limit()
    taxi.Limit()