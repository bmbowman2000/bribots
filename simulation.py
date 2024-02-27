import constants as c
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from robot import ROBOT
import time
from world import WORLD

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate(self.robot.robotId)

    def Run(self):
        backLegSensorValues = np.zeros(1000)
        frontLegSensorValues = np.zeros(1000)

        BackLeg_targetAngles = np.linspace(0, np.pi*2, 1000)
        BackLeg_targetAngles = c.BackLeg_amplitude * np.sin(c.BackLeg_frequency * BackLeg_targetAngles + c.BackLeg_phaseOffset)
        FrontLeg_targetAngles = np.linspace(0, np.pi*2, 1000)
        FrontLeg_targetAngles = c.FrontLeg_amplitude * np.sin(c.FrontLeg_frequency * FrontLeg_targetAngles + c.FrontLeg_phaseOffset)

        for i in range(0, 1000):
            p.stepSimulation()

            #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            #frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            #pyrosim.Set_Motor_For_Joint(bodyIndex = 1, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = BackLeg_targetAngles[i], maxForce = 50)
            #pyrosim.Set_Motor_For_Joint(bodyIndex = 1, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = FrontLeg_targetAngles[i], maxForce = 50)

            time.sleep(c.SLEEP_TIME)

        p.disconnect()
