from skyfield.api import load
import math

def calculatePosition(sun, planet, t):
    position = sun.at(t).observe(earth)
    ra, dec, distance = position.radec()
    
    return ra, dec, distance

ts = load.timescale()
t = ts.now()
# t = ts.utc(2022, 4, 7)

eph = load('de421.bsp')  # ephemeris DE421

sun = eph['sun']
mercury, venus, earth, mars = {eph['mercury barycenter'], eph['venus barycenter'], eph['earth barycenter'], eph['mars barycenter']}

ra, dec, distance = calculatePosition(sun, mercury, t)


