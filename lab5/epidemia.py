#!/usr/bin/python

from matplotlib import pyplot as plt
import numpy as np
import subprocess as p


def main():
  # compile()
  cleanup_results()
  # experiment1()


def compile():
  p.call([
      '/usr/bin/g++', '-fdiagnostics-color=always', '-lgsl', '-std=c++20',
      '-lstdc++', '-Wc++11-extensions', '-g', 'epidemia.cpp', '-o', 'epidemia'
  ])


def cleanup_results():
  p.call([
      'rm', 'mapa.txt', 'ozdrowiali_kazdego_dnia.txt',
      'podatni_kazdego_dnia.txt', 'chorzy_kazdego_dnia.txt'
  ])


def simulate(scale=1, days=10, beta=0.5, gamma=0.25, experiments=3):
  p.call([
      './epidemia',
      str(scale),
      str(days),
      str(beta),
      str(gamma),
      str(experiments)
  ])


def plot_map(plt=plt, show=False):
  matrix = np.loadtxt('./mapa.txt', unpack=True)

  side = range(len(matrix[0]))
  X, Y = np.meshgrid(side, side)
  Z = [[int(r) for r in row] for row in matrix]

  plt.pcolormesh(X, Y, Z)
  if show:
    plt.show()


def experiment1():
  figure, axis = plt.subplots(2, 2)
  plt.tight_layout(h_pad=2)

  for day, ax in zip([0, 10, 20, 30],
                     [axis[0, 0], axis[0, 1], axis[1, 0], axis[1, 1]]):
    simulate(scale=10, days=day)
    plot_map(ax)
    ax.set_title(f'Day {day}')

  plt.show()


if __name__ == '__main__':
  main()