import requests
import json

class climateAnalysis:
  def __init__(self):
    self.coord = []

  def getCoord():
    request = requests.get("https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?api_key=gbZEcVePozgwaMfpr29gbmZL0LkCdZE8IVLr7dr4")
    print(request.status_code)
    request_json = request.json()
    request_json = request_json['events']


  getCoord()


