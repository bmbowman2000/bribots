import matplotlib.pyplot as pyplot
import numpy as np

backLegSensorValues = np.load("data/sensor_values.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
targetAngles = np.load("data/targetAngles.npy")

#pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=5)
#pyplot.plot(frontLegSensorValues, label="Front Leg")
#pyplot.legend()

pyplot.plot(targetAngles, label="targetAngles")
pyplot.title("Motor Commands")
pyplot.show()
