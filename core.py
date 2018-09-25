class Gear:
    def __init__(self, chainring, cog):
        self.chainring = chainring
        self.cog = cog

    def ratio(self):
        return self.chainring / self.cog
