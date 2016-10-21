import math

def horz(height):
	"""Returns the distance to horizon (in meters) based on persion height."""
	earthRadius = 6371000
	horzTheta = math.degrees(math.acos(earthRadius*1.0/(earthRadius+height)))
	groundDist = 2*math.pi*earthRadius*(horzTheta/360.0)
	pythDirect = math.sqrt((earthRadius+height)**2 - earthRadius**2)
	return groundDist,pythDirect,groundDist-pythDirect
print horz(1.8)
