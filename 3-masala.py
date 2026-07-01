from collections import namedtuple
car = namedtuple("Car", ["brand", "model", "year", "mileage"])

cars = []
for i in range(5):
    brand = input('brand kiriting please')
    model  = input('model kiriting please')
    year = int(input('year kiriting please'))
    mileage = int(input('miliage kiriting please'))
    cars = car(brand, model, year, mileage)
kichigi = min(cars, key=lambda x: x.mileage)
print(kichigi)