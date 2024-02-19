import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
import time


SLEEP_TIME = 1 / 240

BackLeg_amplitude = np.pi / 4
BackLeg_frequency = 7.5
BackLeg_phaseOffset = 0
FrontLeg_amplitude = np.pi / 4
FrontLeg_frequency = 2.5
FrontLeg_phaseOffset = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

BackLeg_targetAngles = np.linspace(0, np.pi*2, 1000)
BackLeg_targetAngles = BackLeg_amplitude * np.sin(BackLeg_frequency * BackLeg_targetAngles + BackLeg_phaseOffset)
FrontLeg_targetAngles = np.linspace(0, np.pi*2, 1000)
FrontLeg_targetAngles = FrontLeg_amplitude * np.sin(FrontLeg_frequency * FrontLeg_targetAngles + FrontLeg_phaseOffset)

#np.save("/Users/brianbowman/Desktop/robotics/data/backLegtargetAngles.npy", BackLeg_targetAngles)
#np.save("/Users/brianbowman/Desktop/robotics/data/frontLegtargetAngles.npy", FrontLeg_targetAngles)

pyrosim.Prepare_To_Simulate(robotId)
for i in range(0, 1000):
    p.stepSimulation()
    
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = 1, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = BackLeg_targetAngles[i], maxForce = 50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = 1, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = FrontLeg_targetAngles[i], maxForce = 50)

    time.sleep(SLEEP_TIME)

p.disconnect()
np.save("/Users/brianbowman/Desktop/robotics/data/sensor_values.npy", backLegSensorValues)
np.save("/Users/brianbowman/Desktop/robotics/data/frontLegSensorValues.npy", frontLegSensorValues)
