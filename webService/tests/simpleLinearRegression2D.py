# tests/simpleLinearRegression2D.py
import random

# Randomly generate 30 points [x, y]
# x in range [0, 100], y = 2x + some noise
# noise on (-10, 10) uniform
simpleData2D = [[x, 2 * x + random.uniform(-10, 10)] for x in random.sample(range(100), 30)]
