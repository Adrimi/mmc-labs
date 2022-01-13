#!/usr/bin/python

from matplotlib import pyplot as plt
import numpy as np
import subprocess as p


def main():
  # compile()
  # cleanup_results()
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


def flush(text):
  print(f'\r{text}', flush=True, end='')


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


def plot_ills():
  plot_experiment('./chorzy_kazdego_dnia.txt')
  plt.title('Chorzy kazdego dnia')


def plot_convalescens():
  plot_experiment('./ozdrowiali_kazdego_dnia.txt')
  plt.title('Ozdrowiali kazdego dnia')


def plot_susceptibilies():
  plot_experiment('./podatni_kazdego_dnia.txt')
  plt.title('Podatni kazdego dnia')


def plot_experiment(filepath):
  experiments = np.loadtxt(filepath)
  x_axis = range(len(experiments[0]))
  plt.figure()
  for exp in experiments:
    plt.plot(x_axis, exp, 'r-')


def experiment2():
  # Initial values
  days = 200
  experiments = 5
  day0_ill = 5
  beta = 0.8
  size = 100
  total_population = size**2

  # Stage 1 - Vaccinated population percent dependency on sus population
  vacc_population_space = np.linspace(0,
                                      total_population - size,
                                      size + 1,
                                      dtype=int)
  results_space = []

  for index, vacc in enumerate(vacc_population_space):
    flush(f'Vaccinate simulation nr {index}/{len(vacc_population_space) - 1}')
    simulate(axis=size,
             days=days,
             beta=beta,
             experiments=experiments,
             day0_ill=day0_ill,
             day0_vacc=vacc)

    results = np.loadtxt('./podatni_kazdego_dnia.txt', unpack=True)
    results_space.append(results.min())
    cleanup_results()

  flush('Simulation completed')
  plt.figure()
  plt.plot([v / size for v in vacc_population_space], results_space, 'r-')
  plt.title('Średnia podatnych osób od procentu populacji osoób zaszczepionych')
  plt.xlabel('Procent zaszczepionych')
  plt.ylabel('Liczba osób podatnych')
  plt.grid()

  # Stage 2 - Beta dependency, assuming 30% of vaccined
  # beta_space = np.linspace(0.01, 1, size)
  # results_space = []

  # for index, beta in enumerate(beta_space):
  #   flush(f'Beta Simulation nr {index}/{len(beta_space) - 1}')
  #   simulate(axis=size,
  #            days=days,
  #            beta=beta,
  #            experiments=experiments,
  #            day0_ill=day0_ill,
  #            day0_vacc=total_population * 0.3)

  #   results = np.loadtxt('./podatni_kazdego_dnia.txt', unpack=True)
  #   results_space.append(results.min())
  #   cleanup_results()

  # flush('Simulation completed')
  # plt.figure()
  # plt.plot(beta_space, results_space, 'b-')
  # plt.title('Średnia podatnych osób od wsp. Beta')
  # plt.xlabel('Współczynnik Beta')
  # plt.ylabel('Liczba osób podatnych')
  # plt.grid()
  # plt.show()

  # # Stage 3 - Gamma dependency with Beta 0.5 and vaccinated 30%
  # gamma_space = np.linspace(0.1, 1, size)
  # results_space = []

  # for index, gamma in enumerate(gamma_space):
  #   flush(f'Gamma simulation nr {index}/{len(gamma_space) - 1}')
  #   simulate(axis=size,
  #            days=days,
  #            beta=beta,
  #            gamma=gamma,
  #            experiments=experiments,
  #            day0_ill=day0_ill,
  #            day0_vacc=total_population * 0.3)

  #   results = np.loadtxt('./podatni_kazdego_dnia.txt', unpack=True)
  #   results_space.append(results.min())
  #   cleanup_results()

  # flush('Simulation completed')
  # plt.figure()
  # plt.plot(gamma_space, results_space, 'g-')
  # plt.title('Średnia podatnych osób od wsp. Gamma')
  # plt.xlabel('Współczynnik Gamma')
  # plt.ylabel('Liczba osób podatnych')
  # plt.grid()
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