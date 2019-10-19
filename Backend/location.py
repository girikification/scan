
class location:
  def __init__(self, coord):
    self.coord = coord
    self.coord = [[28.7041, 77.1025], [17.3850, 78.4867]]
    self.publicCentres = getPublicCentres(self.coord)

  def getPublicCentres(coord):
    coord

  def getPoints(coord):
    lat_dif = (max(coord[0][0], coord[1][0]) - min(coord[0][0], coord[1][0]))/10
    lon_dif = (max(coord[0][1], coord[1][1]) - min(coord[0][1], coord[1][1]))/10
    points = []
    for i in range (min(coord[0][0], coord[1][0]), max(coord[0][0], coord[1][0]), lat_dif):
      for j in range (min(coord[0][0], coord[1][0]), max(coord[0][0], coord[1][0]), lon_dif):
        new = [i,j]
        points.append(new)
    return points








