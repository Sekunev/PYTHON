class Car:

    # Default Attributes:
    current_speed = 0

    # Constructor:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def run(self):
        print('Car runned.')
        return True

    def get_speed(self):
        print('Current speed is:', self.current_speed)
        return self.current_speed

    def set_speed(self, new_speed):
        self.current_speed = new_speed
        print('Speed changed. New is:', self.current_speed)
        return True


# create instance:
my_car = Car('Ford', 'Mustang', 'Red') 
my_car.run()
my_car.color

my_car.set_speed(60)
my_car.get_speed()

# -----------------------

# inheritance:
class ChildCar(Car):

    max_limit = 90 # Default

    def set_max_speed(self, limit):
        self.max_limit = limit
        print('Limit changed. New is:', self.max_limit)
        return True

    def get_max_speed(self):
        print('Current limit is:', self.max_limit)
        return self.max_limit

    # Polymorphism.Override
    def set_speed(self, new_speed):
        if (new_speed <= self.max_limit):
            self.current_speed = new_speed
            print('Speed changed. New is:', self.current_speed)
            return True
        else:
            print('Speed unchanged. Its not in limit.')
            return False

my_car = ChildCar('Ford', 'Mustang', 'Red')

my_car.get_max_speed()
my_car.set_speed(60)
my_car.get_speed()

my_car.set_max_speed(110)
my_car.get_max_speed()
my_car.set_speed(120)
my_car.get_speed()