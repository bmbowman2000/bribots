import constants as c
import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = np.linspace(0, np.pi*2, 100)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.BackLeg_amplitude
        if self.jointName == "Torso_BackLeg":
            self.frequency = c.BackLeg_amplitude
        else:
            self.frequency = c.BackLeg_amplitude / 2
        self.offset = c.BackLeg_phaseOffset
        self.motorValues = self.amplitude * np.sin(self.frequency * self.motorValues + self.offset)

    def Set_Value(self, t, robot):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot.robotId, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[t], maxForce = 50)


    def Save_Values(self):
        np.save("/Users/brianbowman/Desktop/robotics/data/targetAngles.npy", self.motorValues)
