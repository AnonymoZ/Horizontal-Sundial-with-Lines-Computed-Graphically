# Angles in Astropy units

import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import Angle as angle

# (        h.sinT                     h.cosT           )
# ( ---------------------, --------------------------- )
# ( cosT.cosL - tanD.sinL  sinL(cosT.cosL - tanD.sinL) )

def AccumulateAndPlot(what, colour, thickness):
	## Numerical Computation for the Domain (Expanse) of Each Hyperbole,
	## Based on the Width You Specify for Your Analemma
	# Initial Value of T
	T = np.deg2rad(angle('0d'))
	# 'stud' is a random number to begin the iteration
	stud = np.deg2rad(angle('30d'))
	# Final Value of T (use a symbol other than 'T')
	mark = np.arccos((h*np.sin(stud) + l*np.tan(what)*np.sin(L))/(l*np.cos(L)))

	while abs(mark - stud) > angle('0.1d'):
		stud = mark
		mark = np.arccos((h*np.sin(stud) + l*np.tan(what)*np.sin(L))/(l*np.cos(L)))

	# Accumulate Coordinates for Your Declination	
	while T < mark:

		xCoord = h * np.sin(T) / ( np.cos(T)*np.cos(L) - np.tan(what)*np.sin(L) )
		x.append(xCoord)

		yCoord = h * np.cos(T) / (np.sin(L)*( np.cos(T)*np.cos(L) - np.tan(what)*np.sin(L) ))
		y.append(yCoord)

		T = T + np.deg2rad(angle('1d'))
	# Plot a Line Joining the Coordinates Calculated
	plt.plot(x, y, colour, linewidth=thickness)



# h, the height of Gnomon, in metres
# h = 0.050
# h = length of the base of Gnomon * np.tan(angle('20d16m43.6s'))
h = (0.049)*np.tan(angle('20d16m43.6s'))
# l, width hyperbolae extend to
l = 0.6
# Jayvin's declination; a hyperbole the day Jayvin will test his sundial
JayvinDeclination = [angle('21d31m')]

# Latitude at Phoenix
L = angle('20d16m43.6s')

# First of each month, January to December
# Declinations used are Average values, though errors do not exceed 9'
Declinations = [
	angle('-23d4m'), angle('-17d20m'), angle('-7d49m'), 
	angle('4d18m'), angle('14d54m'), angle('21d58m'), 
	angle('23d9m'), angle('18d10m'), angle('8d30m'), 
	angle('-2d57m'), angle('-14d14m'), angle('-21d43m')
	]

# Special declinations; Mar 21. Sep 23.
SpecialDeclinations = [
	0, 
	np.deg2rad(23.5), 
	np.deg2rad(-23.5),
	]



# Horizontal Reference Line
x = [0, 0.5]
y = [0, 0]
plt.plot(x, y, linewidth='0.12')

# Determination of Coordinates

x = []
y = []

AccumulateAndPlot(JayvinDeclination[0], '#003049', '0.1')

d = 0 

while d < 3:

	x = []
	y = []

	AccumulateAndPlot(SpecialDeclinations[d], '#d62828', '0.1')

	d = d + 1

d = 0 

while d < 12:

	x = []
	y = []

	AccumulateAndPlot(Declinations[d], '#b1a7a6', '0.1')

	d = d + 1


# Output Distance of Equinox line from Horizontal through Origin
# (This is the yCoord when T = 0° and D = 0°).
Distance = h * np.cos(0) / (np.sin(L)*( np.cos(0)*np.cos(L) - np.tan(0)*np.sin(L) ))
print('The Distance of the Equinox line from Horizontal through Origin is ' 
	+ str(Distance) + ' metres.')

# Plot
plt.axis('square')
plt.axis('off')
plt.savefig("test.svg")
plt.show()

