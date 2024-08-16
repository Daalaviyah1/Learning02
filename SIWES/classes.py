# how to class in python using OOP
# class point():
#     def __init__(self, input1, input2):
#         self.X = input1
#         self.Y = input2

# p = point(2, 8)
# print(p.X)
# print(p.Y)

# How to use the example of class and create airline using OOP
class Flight():
    def __init__(self, capacity):
        self.capacity =  capacity
        self.passengers = []

    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
        
    def open_seats(self):
        return self.capacity - len(self.passengers) 

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flight.add_passengers(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")