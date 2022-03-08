from skyfield.api import load

ts = load.timescale()
t = ts.now()

planets = load('de421.bsp')  # ephemeris DE421
sun, mercury, venus, earth, mars = planets['sun'], planets['mercury'], planets['venus'], planets['earth'], planets['mars']


