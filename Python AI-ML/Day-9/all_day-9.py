#object oriented programming

# class ClassName:   ( class name starts with capital letter)
#     statements(attributes, methods)

#-------------------------------------------------------------#

#creating a class

class Student:

    #if any function is defined inside a class then the function is called method
    def __init__(self,name,roll,address):    #def _init_ is used to define constructor function which is requied to automatically call the class
        self.name= name
        self.roll= roll
        self.address= address
        print(self)

    def student_info(self):
            print(f"Name: {self.name} | Roll: {self.roll} | Address: {self.address}")
s1=Student("shrish","812872","brt")

# s1.student_info()
print(s1.name, s1.address, s1.roll)
print (s1)
# s2=Student()
# s3=Student()
# s4=Student()

# class Parent:
#     hair= "curly"

# class Child(Parent):
#     pass

# child1=Child()
# print(child1.hair)

#----------------------------#

class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    
    def introduce(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll
    def student_info(self):
        print (f" I am {self.name} and I am {self.age}years old. MY roll is {self.roll}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject= subject
    def teach(self):
        print(f"I am {self.name}, of {self.age} and teach {self.subject} ")

individual= Person("Suman","18")
teach=Teacher("Sks","55","organic and dadagiri")
std=Student("Shrish","17","812872")

teach.teach()
individual.introduce()
std.student_info()

# car class with properties brand, model number, whether the car is EV or diesel car with methods:
# starts, stops, breaks, and car info to print the attributes of the car
class Car:
    def __init__(self, brand, model_number, is_ev):
        self.brand= brand
        self.model_number= model_number
        self.is_ev= is_ev

    def start(self):
        print(f"The {self.brand} car has started.")

    def stop(self):
        print(f"The {self.brand} car has stopped.")

    def brake(self):
        print(f"The {self.brand} car is braking.")

    def car_info(self):
        ev_status = "Electric Vehicle" if self.is_ev else "Diesel Car"
        print(f"Car Brand: {self.brand}, Model Number: {self.model_number}, Type: {ev_status}")
my_car = Car("Tesla", "Model S", True)
my_car.start()
my_car.car_info()
my_car.brake()
my_car.stop()
 
