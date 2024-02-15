import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
import time


SLEEP_TIME = 1 / 120

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

backLegSensorValues = np.zeros(100)
frontLegSensorValues = np.zeros(100)
pyrosim.Prepare_To_Simulate(robotId)
for i in range(0, 100):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = 1, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = random.uniform(-3.14/2.0, 3.14/2.0), maxForce = 50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = 1, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = random.uniform(-3.14/2.0, 3.14/2.0), maxForce = 50)
    time.sleep(SLEEP_TIME)

p.disconnect()
np.save("/Users/brianbowman/Desktop/robotics/data/sensor_values.npy", backLegSensorValues)
np.save("/Users/brianbowman/Desktop/robotics/data/frontLegSensorValues.npy", frontLegSensorValues)
