import math

def horz(height):
	earthRadius = 6371000
	horzTheta = math.degrees(math.acos(earthRadius*1.0/(earthRadius+height)))
	groundDist = 2*math.pi*earthRadius*(horzTheta/360.0)
	pythDirect = math.sqrt((earthRadius+height)**2 - earthRadius**2)
	return groundDist,pythDirect,groundDist-pythDirect
print horz(101.8)