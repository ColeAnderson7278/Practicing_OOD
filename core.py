class Gear:
    def __init__(self, chainring, cog, rim, tire):
        self.chainring = chainring
        self.cog = cog
        self.rim = rim
        self.tire = tire

    def ratio(self):
        return self.chainring / self.cog

    def gear_inches(self):
        return (self.ratio() * (self.rim + (self.tire * 2)))
