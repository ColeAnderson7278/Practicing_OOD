import math


class Gear:
    def __init__(self, chainring, cog, wheel):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel

    def diameter(self):
        return self.wheel.rim + (self.wheel.tire * 2)

    def ratio(self):
        return self.chainring / self.cog

    def gear_inches(self):
        return self.ratio() * self.diameter()

    def circumference(self):
        return self.diameter() * math.pi


class Wheel(Gear):
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire
