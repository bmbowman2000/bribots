import pybullet as p
import pybullet_data
import time


SLEEP_TIME = 1 / 120

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

p.loadSDF("world.sdf")

for i in range(0, 1001):
    p.stepSimulation()
    time.sleep(SLEEP_TIME)
    print(i)

p.disconnect()
