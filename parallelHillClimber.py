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
        self.Evaluate(self.parent)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation("DIRECT")

    def Evaluate(self, solutions):
        for solution in solutions.values():
            solution.Start_Simulation("DIRECT")

        for solution in solutions.values():
            solution.Wait_For_Simulation_To_End()

    def Evolve_For_One_Generation(self, directOrGUI):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children) 
        self.Print()
        self.Select()

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Print(self):
        for key in self.parent.keys():
            print(f"\n\nparent fitness: {self.parent[key].fitness:.4f}, child fitness: {self.children[key].fitness:.4f}\n")

    def Select(self):
        for key in self.parent.keys():
            parent_fitness = self.parent[key].fitness
            child_fitness = self.children[key].fitness

            if parent_fitness > child_fitness:
                self.parent[key] = self.children[key]

    def Show_Best(self):
        best_parent = None
        lowest = 100
        for key in self.parent.keys():
            if self.parent[key].fitness < lowest:
                lowest = self.parent[key].fitness
                best_parent = self.parent[key]

        best_parent.Evaluate("GUI")

    def Spawn(self):
        self.children = {}
        for key in self.parent.keys():
            self.children[key] = copy.deepcopy(self.parent[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
