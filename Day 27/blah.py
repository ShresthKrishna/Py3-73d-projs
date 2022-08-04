# using unlimited argument
# def add(*add):
#     sum = 0
#     for n in add:
#         sum+=n
#     return sum
# print(add(1,2,3,4,5,6,7,8,9))


# using keywords argument
def calculate(n,**kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

class Car:

    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make= "Nissan", model= "GT-R")
print(my_car.model)