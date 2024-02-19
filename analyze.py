import matplotlib.pyplot as pyplot
import numpy as np

backLegSensorValues = np.load("data/sensor_values.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
targetAngles = np.load("data/targetAngles.npy")
backLegTargetAngles = np.load("data/backLegTargetAngles.npy")
frontLegTargetAngles = np.load("data/frontLegTargetAngles.npy")

#pyplot.plot(backLegSensorValues, label="backLeg Target Angles", linewidth=5)
#pyplot.plot(frontLegSensorValues, label="frontLeg Target Angles")
#pyplot.legend()

pyplot.plot(backLegTargetAngles, label="Back Leg", linewidth=5)
pyplot.plot(frontLegTargetAngles, label="Front Leg")
pyplot.legend()
pyplot.show()
