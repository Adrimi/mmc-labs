#!/usr/bin/python

from matplotlib import pyplot as plt
import numpy as np
import subprocess as p


def main():
  # compile()
  cleanup_results()
  experiment2()


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


def simulate(axis=10,
             days=10,
             beta=0.5,
             gamma=0.25,
             experiments=1,
             day0_ill=10,
             day0_vacc=30):
  p.call([
      './epidemia',
      str(axis),
      str(days),
      str(beta),
      str(gamma),
      str(experiments),
      str(day0_ill),
      str(day0_vacc)
  ])


def plot_map(plt=plt, show=False):
  matrix = np.loadtxt('./mapa.txt', unpack=True)

  side = range(len(matrix[0]))
  X, Y = np.meshgrid(side, side)
  Z = [[int(r) for r in row] for row in matrix]

  plt.pcolormesh(X, Y, Z)
  if show:
    plt.show()


def plot_ill():
  plot_experiment('./chorzy_kazdego_dnia.txt')
  plt.title('Chorzy kazdego dnia')


def plot_convalescent():
  plot_experiment('./ozdrowiali_kazdego_dnia.txt')
  plt.title('Ozdrowiali kazdego dnia')


def plot_susceptibility():
  plot_experiment('./podatni_kazdego_dnia.txt')
  plt.title('Podatni kazdego dnia')


def plot_ill_mean():
  plot_experiment_mean('./chorzy_kazdego_dnia.txt')
  plt.title('Średnia chorych kazdego dnia')


def plot_convalescent_mean():
  plot_experiment_mean('./ozdrowiali_kazdego_dnia.txt')
  plt.title('Średnia ozdrowiałych kazdego dnia')


def plot_susceptibility_mean():
  plot_experiment_mean('./podatni_kazdego_dnia.txt')
  plt.title('Średnia podatnych kazdego dnia')


def plot_experiment(filepath):
  experiments = np.loadtxt(filepath)
  x_axis = range(len(experiments[0]))
  plt.figure()
  for exp in experiments:
    plt.plot(x_axis, exp, 'r-')


def plot_experiment_mean(filepath):
  experiments = np.loadtxt(filepath)
  y_axis = [e.mean() for e in experiments]
  x_axis = range(len(y_axis))

  # plt.figure()
  plt.plot(x_axis, y_axis, 'r-', label=f'Mean')


def experiment2():
  # Stage 1 - Beta dependency
  beta_space = np.slinspace(0, 1, 10)

  for beta in beta_space:
    simulate(axis=100,
             days=200,
             beta=beta,
             experiments=20,
             day0_ill=5,
             day0_vacc=100 * 100 * 0.3)

    plot_susceptibility_mean()
  plt.title('Średnia podatnych kazdego dnia od Beta')
  plt.xlabel('Beta')
  plt.ylabel('średnia podatnych')
  plt.show()


def experiment1():
  _, axis = plt.subplots(2, 2)
  plt.tight_layout(h_pad=2)
  x_scale = 100
  vacc_percent = 0.3

  for day, ax in zip([0, 100, 200, 500],
                     [axis[0, 0], axis[0, 1], axis[1, 0], axis[1, 1]]):
    simulate(axis=x_scale,
             days=day,
             day0_ill=5,
             day0_vacc=x_scale * x_scale * vacc_percent)
    plot_map(ax)
    ax.set_title(f'Day {day}')

  plt.show()


if __name__ == '__main__':
  main()