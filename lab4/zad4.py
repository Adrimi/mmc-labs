from matplotlib import pyplot as plt
from math import sin, sqrt
import numpy as np

PI = 3.141592653589793


def f(x):
  return sin(PI * x)


def g(x):
  return (-4) * x * (x - 1)


def expectation(array, n):
  probability = 1 / n
  sum = 0
  for i in range(0, n):
    sum += (array[i] * probability)

  return float(sum)


def variance(array):
  mean = sum(array) / len(array)
  res = sum((i - mean)**2 for i in array) / len(array)
  return res


def covariance(f_samples, g_samples, n):
  f_g_sum = [a * b for a, b in zip(f_samples, g_samples)]
  return (1 / n) * sum(f_g_sum) - (1 / n**2) * sum(f_samples) * sum(g_samples)


# http://www.if.pwr.edu.pl/~pater/DANE/niepewnoci_pomiarw.html
def uncertainty(x, x_dash):
  n = len(x)
  return sqrt(sum((xi - x_dash)**2 for xi in x) / (n * (n - 1)))


def map(array, index):
  return [a[index] for a in array]


def main():
  N = 100

  range_01_samples = np.linspace(0, 1, N)
  g_samples = [g(x) for x in range_01_samples]
  f_samples = [f(x) for x in range_01_samples]

  # 1 Wyswietlic na jednym wykresie funckje f(x) oraz g(x) oraz ich roznice w rzedziale x[0, 1]
  f_g_substract = [abs(a - b) for a, b in zip(f_samples, g_samples)]

  plt.figure()
  plt.xlim([0, 1])
  plt.plot(range_01_samples, f_samples, 'r-', label='f(x)')
  plt.plot(range_01_samples, g_samples, 'g-', label='g(x)')
  plt.plot(range_01_samples, f_g_substract, 'b-', label='f(x) - g(x)')
  plt.grid()
  plt.legend()
  # plt.show()

  # Obliczyc analitycznie wartosc calki I
  # https://www.wolframalpha.com/input/?i=integral+sin%CF%80x+from+0+to+1
  # I = 2/π = 0.636619...
  I = 2 / PI

  # Oszacowac wartosc tej calki metoda podstawowa Monte Carlo
  # Z zastosowaniem zmienniej kontrolnej g(x)
  # Bez zmiennej kontrolnej

  I_dash_c_results = []
  I_dash_results = []

  for n in [N * 10**x for x in range(0, 6)]:
    range_samples = np.linspace(0, 1, n)
    f_samples = [f(x) for x in range_samples]
    g_samples = [g(x) for x in range_samples]
    g_variance = variance(g_samples)
    g_exp_dash = expectation(g_samples, n)

    # 1
    f_exp = expectation(f_samples, n)
    # g_exp = expectation(g_samples, n)
    cov = covariance(f_samples, g_samples, n)

    # 2
    c = cov / g_variance

    # 3
    g_gdash_exp = expectation([sample - g_exp_dash for sample in g_samples], n)
    I_dash_c = f_exp - c * g_gdash_exp
    I_dash = f_exp

    # log
    I_dash_c_uncertainty = uncertainty(f_samples, I_dash_c)
    I_dash_c_delta = abs(I_dash_c - I)
    I_dash_uncertainty = uncertainty(f_samples, I_dash)
    I_dash_delta = abs(I_dash - I)

    print(f'N = {n}')
    print(
        f'I w/o correction | Estimate = {I_dash:0.6f} | Uncertainty = {I_dash_uncertainty:0.6f} | Delta = {I_dash_delta:0.6f}'
    )
    print(
        f'I w/w correction | Estimate = {I_dash_c:0.6f} | Uncertainty = {I_dash_c_uncertainty:0.6f} | Delta = {I_dash_c_delta:0.6f}'
    )

    I_dash_c_results.append([n, I_dash_c, I_dash_c_uncertainty, I_dash_c_delta])
    I_dash_results.append([n, I_dash, I_dash_uncertainty, I_dash_delta])

  # Przedstawic na wspolnym wykresie zaleznosc niepewnosci i bledu od licznosci proby dla obu przypadkow
  x_ticks = range(len(I_dash_c_results))

  plt.figure()
  plt.xticks(x_ticks, map(I_dash_c_results, 0))
  plt.plot(x_ticks,
           map(I_dash_c_results, 2),
           'r--',
           label='Niepewnosc I_dash_c')
  plt.plot(x_ticks, map(I_dash_c_results, 3), 'b--', label='Blad I_dash_c')
  plt.plot(x_ticks, map(I_dash_results, 2), 'o:r', label='Niepewnosc I_dash')
  plt.plot(x_ticks, map(I_dash_results, 3), 'o:b', label='Blad I_dash')
  plt.grid()
  plt.title('Całkowanie z użyciem i bez zmiennej kontrolnej')
  plt.legend()

  plt.show()


if __name__ == '__main__':
  main()