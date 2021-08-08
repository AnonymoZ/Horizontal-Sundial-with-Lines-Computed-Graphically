import matplotlib.pyplot as plt
import numpy as np

# tan D = tan(τ)[sin(ϕ)]

# ensure theta (angle of deviation) goes not beyond 45°
# tau's limits here arbitrary, so figure has comparable height along positive and width
# the latitude used is at Phoenix, 20°16'43.6"
# the corresponding longitude is 57°30'7"
tau = 0
minutesBetweenLines = 60
lineWidth = '0.1'
plt.axis('square')
# (15/60)° represents one minute away from Noon
while tau < 45:
	x = [0]
	y = [0, 1]
	
	xComponent = np.tan(np.deg2rad(tau)) * np.sin(np.deg2rad(20.27878))
	x.append(xComponent)
	if tau % (15) == 0:
		# print 'red'
		plt.plot(x, y, '#d62828', linewidth='0.33')
	elif tau % (7.5) == 0.0:
		# print 'blue'
		plt.plot(x, y, '#003049', linewidth=lineWidth)
	elif tau % (3.75) == 0.0:
		# print 'yellow'
		plt.plot(x, y, '#fcbf49', linewidth=lineWidth)
	else:
		# print 'background'. Formerly #b1a7a6.
		plt.plot(x, y, '#dee2e6', linewidth=lineWidth)
	tau = tau + (minutesBetweenLines * (15/60))


while tau <= 110:
	x = [0, xComponent]
	y = [0]
	
	yComponent = xComponent / (np.tan(np.deg2rad(tau)) * np.sin(np.deg2rad(20.27878)))
	y.append(yComponent)
	if tau % (15) == 0:
		# print 'red'
		plt.plot(x, y, '#d62828', linewidth='0.33')
	elif tau % (7.5) == 0.0:
		# print 'blue'
		plt.plot(x, y, '#003049', linewidth=lineWidth)
	elif tau % (3.75) == 0.0:
		# print 'yellow'
		plt.plot(x, y, '#fcbf49', linewidth=lineWidth)
	else:
		# print 'background'
		plt.plot(x, y, '#dee2e6', linewidth=lineWidth)
	tau = tau + (minutesBetweenLines * (15/60))
	print(xComponent)

plt.axis('off')
plt.savefig("test.svg")
plt.show()