import constants as c
import copy
import os
from solution import SOLUTION

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")

        self.nextAvailableID = 0
        self.parent = {}
        for i in range(c.populationSize):
            self.parent[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        for parent in self.parent.values():
            parent.Start_Simulation("DIRECT")

        for parent in self.parent.values():
            parent.Wait_For_Simulation_To_End()

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation("DIRECT")

    def Evolve_For_One_Generation(self, directOrGUI):
        pass
        """
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(directOrGUI)
        self.Print()
        self.Select()
        """

    def Mutate(self):
        self.child.Mutate()

    def Print(self):
        print(f"\n\nparent fitness: {self.parent.fitness:.4f}, child fitness: {self.child.fitness:.4f}\n")

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Show_Best(self):
        self.parent.Evaluate("GUI")

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1
