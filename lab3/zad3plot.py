#!/usr/bin/python

from matplotlib import pyplot as plt
import numpy as np


def teoretical_function(x):
  return 5 / 12 * (1 + (x - 1)**4)


def plot(filename):
  experiment = np.loadtxt(filename, unpack=True)
  x = np.linspace(0, 2, num=100000)
  teoretical = [teoretical_function(i) for i in x]

  plt.figure()
  plt.xlim([0, 2])
  plt.hist(experiment, bins=100, density=True, label='Wartość testowa')
  plt.plot(x, teoretical, 'r-', label='Wartość teoretyczna')
  plt.legend()


def main():
  plot('lab3/zad3_elimination.txt')
  plt.title('Metoda eliminacji')
  plot('lab3/zad3_superposition.txt')
  plt.title('Metoda superpozycji')
  plt.show()


if __name__ == '__main__':
  main()