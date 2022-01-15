import re
import matplotlib.pyplot as plt
import numpy as np

with open("out.txt", "r") as file:

  lines = file.readlines()

  X = []
  Y = []

  for line in lines:
    if "T " in line:
      X.append(float(line.split()[-1]))
    if "Srednia Magnetyzacja" in line:
      Y.append(float(line.split()[-1]))

plt.plot(X, Y)
plt.show()