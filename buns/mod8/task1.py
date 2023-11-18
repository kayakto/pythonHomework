class Transport():
    def __init__(self, *args, **kwargs):
        self._coordinates = (args[0], args[1])
        self._speed = args[2]
        self._brand = args[3]
        self._year = args[4]
        self._number = args[5]

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        if not isinstance(coordinates[0], int) or not isinstance(coordinates[1], int):
            raise TypeError('TypeError: coordinates values must be int!')
        self._coordinates = coordinates

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if not isinstance(speed, int):
            raise TypeError("TypeError: speed value must be int!")
        elif speed < 0:
            raise ValueError("ValueError: speed value must be greater than or equal to zero!")
        self._speed = speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if not isinstance(brand, str):
            raise TypeError("TypeError: brand value must be str!")
        self._brand = brand

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError("TypeError: year value must be int!")
        elif year < 0:
            raise ValueError("ValueError: year value must be greater than or equal to zero!")
        self._year = year

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if not isinstance(number, int):
            raise TypeError("TypeError: number value must be int!")
        elif number < 0:
            raise ValueError("ValueError: number value must be greater than or equal to zero!")
        self._number = number

    def __str__(self):
        return f'Transport \n Coordinates = {self.coordinates} \n Speed = {self.speed} \n Brand = {self.brand} \n Year = {self.year} \n Number = {self.number}'

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        return (pos_x < self.coordinates[0] < (pos_x + length)) and (pos_y < self.coordinates[1] < (pos_y + width))


class Passenger():
    def __init__(self, *args, **kwargs):
        self.__passengers_capacity = args[0]
        self.__number_of_passengers = args[1]

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if not isinstance(passengers_capacity, int):
            raise TypeError("TypeError: passengers_capacity value must be int!")
        elif passengers_capacity <= 0:
            raise ValueError("ValueError: passengers_capacity value must be greater than zero!")
        self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if not isinstance(number_of_passengers, int):
            raise TypeError("TypeError: number_of_passengers value must be int!")
        elif number_of_passengers < 0:
            raise ValueError("ValueError: number_of_passengers value must be greater than or equal to zero!")
        self.__number_of_passengers = number_of_passengers

    def __str__(self):
        return f'Passenger \n Capacity = {self.passengers_capacity} \n Number = {self.number_of_passengers}'


class Cargo():
    def __init__(self, *args, **kwargs):
        self.carrying = args[0]

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if not isinstance(carrying, int):
            raise TypeError("TypeError: carrying value must be int!")
        elif carrying <= 0:
            raise ValueError("ValueError: carrying value must be greater than zero!")
        self.__carrying = carrying


class Plane(Transport):
    def __init__(self, *args):
        self._height = args[0]
        super().__init__(*args[1::])

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("TypeError: height value must be int!")
        elif height <= 0:
            raise ValueError("ValueError: height value must be greater than zero!")
        self._height = height




class Auto(Transport):

    def __init__(self, *args, **kwargs):
        self._factory = args[0]
        super().__init__(*args[1::])

    @property
    def factory(self):
        return self._factory

    @factory.setter
    def factory(self, factory):
        if not isinstance(factory, str):
            raise TypeError("TypeError: factory value must be str!")
        self._factory = factory


class Ship(Transport):
    def __init__(self, *args, **kwargs):
        self._port = args[0]
        super().__init__(*args[1::])

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        if not isinstance(port, str):
            raise TypeError("TypeError: port value must be str!")
        self._port = port


class Car(Auto):
    def __init__(self, model, *args):
        self._model = model
        super().__init__(*args)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError("TypeError: model value must be str!")
        self._model = model


class Bus(Auto, Passenger):
    def __init__(self, model, passengers_capacity, number_of_passengers, *auto_args):
        self._model = model
        Passenger.__init__(self, passengers_capacity, number_of_passengers)
        Auto.__init__(self, *auto_args)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError("TypeError: model value must be str!")
        self._model = model


class CargoAuto(Auto, Cargo):
    def __init__(self, model, carrying, *auto_args):
        self._model = model
        Cargo.__init__(self, carrying)
        Auto.__init__(self, *auto_args)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError("TypeError: model value must be str!")
        self._model = model


class Boat(Ship):
    def __init__(self, model, *ship_args):
        self._model = model
        super().__init__(*ship_args)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError("TypeError: model value must be str!")
        self._model = model


class PassengerShip(Ship, Passenger):
    def __init__(self, model, passengers_capacity, number_of_passengers, *ship_args):
        self._model = model
        Passenger.__init__(self, passengers_capacity, number_of_passengers)
        Ship.__init__(self, *ship_args)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError("TypeError: model value must be str!")
        self._model = model


class CargoShip(Ship, Cargo):
    def __init__(self, model, carrying, *ship_args):
        self._model = model
        Cargo.__init__(self, carrying)
        Ship.__init__(self, *ship_args)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError("TypeError: model value must be str!")
        self._model = model


class Airplane(Plane):
    def __init__(self, model, *plane_args):
        self._model = model
        super().__init__(*plane_args)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError("TypeError: model value must be str!")
        self._model = model


class PassengerPlane(Plane, Passenger):
    def __init__(self, model, passengers_capacity, number_of_passengers, *plane_args):
        self._model = model
        Passenger.__init__(self, passengers_capacity, number_of_passengers)
        Plane.__init__(self, *plane_args)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError("TypeError: model value must be str!")
        self._model = model


class CargoPlane(Plane, Cargo):
    def __init__(self, model, carrying, *plane_args):
        self._model = model
        Cargo.__init__(self, carrying)
        Plane.__init__(self, *plane_args)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError("TypeError: model value must be str!")
        self._model = model


class Seaplane(Plane, Ship):
    def __init__(self, model, port, height, *args):
        self._model = model
        Ship._port = port
        Plane._height = height
        Transport.__init__(self, *args)

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError("TypeError: model value must be str!")
        self._model = model


seaplane = Seaplane('Short Sunderland', 'PORT_644_US', 10, 138, 139, 336, 'Short Brothers', 1937, 7777777)
print(seaplane)
print(seaplane.height)
print(seaplane.port)

# Transport
#  Coordinates = (138, 139)
#  Speed = 336
#  Brand = Short Brothers
#  Year = 1937 
#  Number = 7777777
# 10
# PORT_644_US