#!/usr/bin/python

from matplotlib import pyplot as plt
import numpy as np


def print(filename):
  x, y = np.loadtxt(filename, unpack=True)
  plt.xlim([-4, 4])

  plt.hist(x, bins=100, density=True)
  plt.hist(y, bins=100, density=True)

  plt.xlabel('Wartość')
  plt.ylabel('Dystrybuanta')
  plt.legend(loc='best')
  plt.show()


def main():
  print('lab3/zad2_box_muller.txt')
  print('lab3/zad2_marsaglii_braya.txt')


if __name__ == '__main__':
  main()