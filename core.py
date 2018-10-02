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
