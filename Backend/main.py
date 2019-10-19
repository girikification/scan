from climateAnalysis import climateAnalysis
from demographics import demographics
from evacRoute import evacRoute
from location import location

class scan:
    def __init__(self, coord):
        self.location = location(coord)
        self.evacRoute = evacRoute(location)
        self.demographs = demographics(location)
        self.climate = climateAnalysis(location)

