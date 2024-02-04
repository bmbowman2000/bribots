import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

pyrosim.Start_SDF("boxes.sdf")

for i in range(5):
    for j in range(5):
        for k in range(5):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
            z += 1
            length = 0.9 * length
            width = 0.9 * width
            height = 0.9 * height
        length = 1
        width = 1
        height = 1
        z = 0.5
        x += 2
    x = 0
    y += 2

pyrosim.End()
