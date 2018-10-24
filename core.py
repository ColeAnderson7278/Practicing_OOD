import math

# class Gear:
#     def __init__(self, chainring, cog, wheel):
#         self.chainring = chainring
#         self.cog = cog
#         self.wheel = wheel

#     def ratio(self):
#         return self.chainring / self.cog

#     def gear_inches(self):
#         return self.ratio() * self.wheel.diameter()

#     def circumference(self):
#         return self.diameter() * math.pi

# class Wheel(Gear):
#     def __init__(self, rim, tire):
#         self.rim = rim
#         self.tire = tire

#     def diameter(self):
#         return self.rim + (self.tire * 2)

# class Trip:
#     def __init__(self, bicycles, customers, vehicle):
#         self.bicycles = bicycles
#         self.customers = customers
#         self.vehicle = vehicle

#     def prepare(self, preparers):
#         for preparer in preparers:
#             preparer.prepare_trip()

# class Mechanic:
#     def __init__(self, bicycles):
#         self.bicycles = bicycles

#     def prepare_trip(self, trip):
#         for bike in trip.bicycles:
#             bike.prepare_bicycle()

#     def prepare_bicycle(self):
#         return None

# class TripCoordinator:
#     def __init__(self, customers):
#         self.customers = customers

#     def prepare_trip(self, trip):
#         return None

# class Driver:
#     def __init__(self, vehicle):
#         self.vehicle = vehicle

#     def prepare_trip(self, trip):
#         vehicle = trip.vehicle
#         gas_up(vehicle)
#         fill_water_tank(vehicle)

# class Bicycle:
#     def __init__(self, size, chain, tire_size):
#         self.size = size
#         self.chain = chain
#         self.tire_size = tire_size

#     def spares(self):
#         self.chain = "10-speed"
#         self.tire_size = "23"

# class MountainBike(Bicycle):
#     def __init__(self, front_shock, back_shock):
#         self.front_shock = front_shock
#         self.back_shock = back_shock
#         self.tire_size = "23"

# class RoadBike(Bicycle):
#     def __init__(self, tape_color):
#         self.tape_color = tape_color
#         self.tire_size = "2.1"

#     def spares(self):
#         self.tape_color = tape_color

# class RecumbentBike(Bicycle):
#     def __init__(self, flag):
#         self.flag = flag

#     def spares(self):
#         self.flag = flag


class Schedule():
    def scheduled(self, schedulabel, start_date, end_date):
        return f"This {schedulabel.class} is not scheduled\n" + f"between {start_date} and {end_date}"


class Bicycle():
    def __init__(self, schedule, size, chain, tire_size):
        self.schedule = Schedule()

    def schedulabel(self, start_date, end_date):
        return False and scheduled(start_date, end_date)

    def scheduled(self, start_date, end_date):
        schedule.scheduled(start_date, end_date)

    def lead_days(self):
        return 1
