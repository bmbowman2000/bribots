import constants as c
import copy
from solution import SOLUTION

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation("DIRECT")

    def Evolve_For_One_Generation(self, directOrGUI):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(directOrGUI)
        self.Print()
        self.Select()

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
