from generator import *
import random
from train import train_units


units = generate_random_unit(200, [0, 1, 2, 3, 4, 5, 6], 3 ** 5, 7)
train_units(units, 30, 20, 0.5, 100, 200, 3 ** 5, 7, 20)
