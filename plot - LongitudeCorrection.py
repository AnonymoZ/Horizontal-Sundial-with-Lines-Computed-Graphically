# Assumed Correction is Exactly 10mins.

import matplotlib.pyplot as plt
import numpy as np

# tan D = tan(τ)[sin(ϕ)]

# ensure theta (angle of deviation) goes not beyond 45°
# tau's limits here arbitrary, so figure has comparable height along positive and width
# the latitude used is at Phoenix, 20°16'43.6"
# the corresponding longitude is 57°30'7"
tau = -110
minutesBetweenLines = 1
lineWidth = '0.1'
plt.axis('square')
# (15/60)° represents one minute away from Noon

# This value got from an iteration of a variant of this script, 'LatitudeCorrection'
# Its negative was taken since at tau = -110, xComponent is negative
xComponent = -0.20010283231263087

bothLoopsComplete = 0
while bothLoopsComplete < 2:

	while abs(tau) < 45:
		x = [0]
		y = [0, 1]
	
		xComponent = np.tan(np.deg2rad(tau)) * np.sin(np.deg2rad(20.27878))
		x.append(xComponent)
		# These 'if-else' are simply 'checks' that give colour 
		# to your already-obtained lines.
		if ( tau - 10 * (15/60) ) % (15) == 0:
			# print 'red'
			plt.plot(x, y, '#d62828', linewidth='0.33')
		elif ( tau - 10 * (15/60) ) % (7.5) == 0.0:
			# print 'blue'
			plt.plot(x, y, '#003049', linewidth=lineWidth)
		elif ( tau - 10 * (15/60) ) % (3.75) == 0.0:
			# print 'yellow'
			plt.plot(x, y, '#fcbf49', linewidth=lineWidth)
		else:
			# print 'background'. Formerly #b1a7a6.
			plt.plot(x, y, '#dee2e6', linewidth=lineWidth)
		tau = tau + (minutesBetweenLines * (15/60))
	
	while abs(tau) >= 45 and abs(tau) <= 110:
		x = [0, xComponent]
		y = [0]
		
		yComponent = xComponent / (np.tan(np.deg2rad(tau)) * np.sin(np.deg2rad(20.27878)))
		y.append(yComponent)
		if ( tau - 10 * (15/60) ) % (15) == 0:
			# print 'red'
			plt.plot(x, y, '#d62828', linewidth='0.33')
		elif ( tau - 10 * (15/60) ) % (7.5) == 0.0:
			# print 'blue'
			plt.plot(x, y, '#003049', linewidth=lineWidth)
		elif ( tau - 10 * (15/60) ) % (3.75) == 0.0:
			# print 'yellow'
			plt.plot(x, y, '#fcbf49', linewidth=lineWidth)
		else:
			# print 'background'
			plt.plot(x, y, '#dee2e6', linewidth=lineWidth)
		tau = tau + (minutesBetweenLines * (15/60))

	bothLoopsComplete = bothLoopsComplete + 1


plt.axis('off')
plt.savefig("test.svg")
plt.show()