from hillclimber import HILL_CLIMBER
import os

"""
for i in range(5):
    os.system("python3 generate.py")
    os.system("python3 simulate.py")
"""

hc = HILL_CLIMBER()
hc.Evolve()
