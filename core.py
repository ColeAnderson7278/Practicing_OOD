import math


class Gear:
    def __init__(self, chainring, cog, wheel):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel

    def ratio(self):
        return self.chainring / self.cog

    def gear_inches(self):
        return self.ratio() * self.wheel.diameter()

    def circumference(self):
        return self.diameter() * math.pi


class Wheel(Gear):
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    def diameter(self):
        return self.rim + (self.tire * 2)


class Trip:
    def __init__(self, bicycles, customers, vehicle):
        self.bicycles = bicycles
        self.customers = customers
        self.vehicle = vehicle

    def prepare(self,preparers):
        for preparer in preparers:
            if isinstance(preparer, Mechanic):
                preparer.prepare_bicycles(self.bicycles)
            else if isinstance(preparer,TripCoordinator):
                preparer.buy_food(self.customers)
            else if isinstance(preparer,Driver):
                preparer.gas_up(self.vehicle)
                preparer.fill_water_tank(self.vehicle)

class Mechanic:
    def __init__(self, bicycles):
        self.bicycles = bicycles

    def prepare_bicycles(self):
        fixed_bikes = []
        for bike in self.bicycles:
            fixed_bikes.append(self.prepare_bicycle(bike))
        return fixed_bikes

    def prepare_bicycle(self):
        return None


class TripCoordinator:
    def __init__(self, customers):
        self.customers = customers

    def buy_food(self):
        return None


class Driver:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def gas_up(self):
        return None
    
    def fill_water_tank(self):
        return None
