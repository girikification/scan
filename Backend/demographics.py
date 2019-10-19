from location import location

class demographics:
    def __init__(self, location):
        self.location = location
        self.total = getTotal()
        self.calamityToll = 0
        self.ageGroups = []
        self.hospital = 0

    def getTotal():
        return worldPop(location)

    def worldPop(location):
        return location.coord
