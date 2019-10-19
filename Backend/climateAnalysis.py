import requests
from location import location

class climateAnalysis:
    def __init__(self):
        self.coord = self.getCoord()
        self.location = []
        for i in self.coord:
          location.append(location(i))
          print(i)

    def getCoord():
        request = requests.get("https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?api_key"
                               "=gbZEcVePozgwaMfpr29gbmZL0LkCdZE8IVLr7dr4")
        print(request.status_code)
        request_json = request.json()
        request_json = request_json.get('events')
        coord = []
        for i in request_json:
            if i.get('categories')[0].get('id') == 10:
              point3 = []
              print(i.get('geometries'))
              point = i.get('geometries')[0].get('coordinates')
              point2 = []
              for j in i.get('geometries'):
                point2 = j.get('coordinates')
              point3.append(point)
              point3.append(point2)
              coord.append(point3)
        return coord
