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

    def prepare(self, preparers):
        for preparer in preparers:
            preparer.prepare_trip()


class Mechanic:
    def __init__(self, bicycles):
        self.bicycles = bicycles

    def prepare_trip(self, trip):
        for bike in trip.bicycles:
            bike.prepare_bicycle()

    def prepare_bicycle(self):
        return None


class TripCoordinator:
    def __init__(self, customers):
        self.customers = customers

    def prepare_trip(self, trip):
        return None


class Driver:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def prepare_trip(self, trip):
        vehicle = trip.vehicle
        gas_up(vehicle)
        fill_water_tank(vehicle)


class Bicycle:
    def __init__(self, style, size, tape_color, front_shock, rear_shock):
        self.style = style
        self.size = size
        self.tape_color = tape_color
        self.front_shock = front_shock
        self.rear_shock = rear_shock

    # def spares(self):
    #     if self.style == "road":
    #         self.spares =
    #         {chain: "10-speed";
    #         tire_size: "23";
    #         tape_color: tape_color;}
    #     else:
    #         self.spares = {chain: "10-speed";
    #         tire_size: "2.1";
    #         rear_shock: rear_shock;}
