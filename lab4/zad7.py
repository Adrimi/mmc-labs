import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import qmc

PI = 3.141592653589793


def pseudorandom(n):
  a = 0
  x = np.random.uniform(a, PI, size=n)
  est = (PI - a) * np.mean(np.sin(x))
  return est, np.abs(est - 2)


def quasirandom(n):
  a = 0
  sampler = qmc.Sobol(d=1, seed=None)
  x = sampler.random(n).T.squeeze() * PI
  est = (PI - a) * np.mean(np.sin(x))
  return est, np.abs(est - 2)


def main():
  pseudorandom_estimations = []
  pseudorandom_errors = []

  for _ in range(0, 1000):  # 1000 prob
    est, err = pseudorandom(1000)
    pseudorandom_estimations.append(est)
    pseudorandom_errors.append(err)

  quasirandom_estimations = []
  quasirandom_errors = []

  for _ in range(0, 1000):  # 1000 prob
    est, err = quasirandom(1000)
    quasirandom_estimations.append(est)
    quasirandom_errors.append(err)

  plt.figure()
  plt.hist(pseudorandom_estimations, label='pseudorandom')
  plt.hist(quasirandom_estimations, label='quasirandom')
  plt.legend(loc='best')
  plt.title('Estimation differences between different random methods')

  plt.figure()
  plt.hist(pseudorandom_errors, label='pseudorandom')
  plt.hist(quasirandom_errors, label='quasirandom')
  plt.legend(loc='best')
  plt.title('Error differences between different random methods')

  plt.show()


if __name__ == '__main__':
  main()
