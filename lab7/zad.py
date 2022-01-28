import numpy as np
from matplotlib import pyplot as plt


def generate_normal_distribution(lower, upper):
  return np.random.normal(lower, upper)


def generate_uniform_distribution(lower, upper):
  return np.random.uniform(lower, upper)


def odchylenie_standardowe(M, estymator_y, results):
  return np.sqrt(1 / (M - 1) * np.sum([(y - estymator_y)**2 for y in results]))


def estymator(M, results):
  return 1 / M * np.sum(results)


def przedzial_rozszerzenia(results, p, M):
  q = int(p * M)
  output_sorted = results.copy()
  output_sorted.sort()
  r = int((M - q) / 2)
  if not isinstance(r, int):
    r = int((M - q + 1) / 2)
  y_min = output_sorted[r]
  y_max = output_sorted[r + q]

  return y_min, y_max


def _gum_odchylenie_czastkowe(x, mean_x):
  return np.sqrt(1 / len(x) * np.sum([(x - mean_x)**2 for x in x]))


def gum_odchylenie_standardowe(X):
  x1, x2 = zip(*X)
  mean_x1 = np.mean(x1)
  mean_x2 = np.mean(x2)
  std_dev_x1 = _gum_odchylenie_czastkowe(x1, mean_x1)
  std_dev_x2 = _gum_odchylenie_czastkowe(x2, mean_x2)
  std_dev = np.sqrt(std_dev_x1**2 + std_dev_x2**2)

  return std_dev


def gum_przedzial_rozszerzenia(results, std_dev):
  y_mean = np.mean(results)
  y_min = y_mean - 2 * std_dev
  y_max = y_mean + 2 * std_dev

  return y_min, y_max


def calculate_results(PAIRS, SUMS, M, p):
  estymator_y = estymator(M, SUMS)
  std_dev = odchylenie_standardowe(M, estymator_y, SUMS)
  y_min, y_max = przedzial_rozszerzenia(SUMS, p, M)
  gum_std_dev = gum_odchylenie_standardowe(PAIRS)
  gum_y_min, gum_y_max = gum_przedzial_rozszerzenia(SUMS, gum_std_dev)

  print('Estymator:', estymator_y)
  print('Odchylenie standardowe:', std_dev)
  print('Przedział rozszerzenia: [y_min:', y_min, 'y_max:', y_max, ']')
  print('Odchylenie standardowe GUM:', gum_std_dev)
  print('Przedział rozszerzenia GUM: [y_min:', gum_y_min, 'y_max:', gum_y_max,
        ']')


def main():
  # 1. Okreslenie liczby prob monte carlo
  M = 10**6
  p = 0.9545

  print("--- ZADNAIE 1 ---")

  # 2. Wygenerowanie M wektorow danych wejsciowych X
  PAIRS = []
  SUMS = []
  for _ in range(M):
    x1 = generate_normal_distribution(0, 1)
    x2 = generate_normal_distribution(0, 2)
    PAIRS.append((x1, x2))
    SUMS.append(x1 + x2)

  calculate_results(PAIRS, SUMS, M, p)

  print("--- ZADANIE 2 ---")

  # 2. Wygenerowanie M wektorow danych wejsciowych X
  PAIRS = []
  SUMS = []
  for _ in range(M):
    x1 = generate_uniform_distribution(0, 4)
    x2 = generate_uniform_distribution(5, 6)
    PAIRS.append((x1, x2))
    SUMS.append(x1 + x2)

  calculate_results(PAIRS, SUMS, M, p)

  plt.figure()
  plt.hist([a for a, b in PAIRS], bins=50, density=True)
  plt.title("X1")
  plt.savefig("x1.png")

  plt.figure()
  plt.hist([b for a, b in PAIRS], bins=50, density=True)
  plt.title("X2")
  plt.savefig("x2.png")

  plt.figure()
  plt.hist([a + b for a, b in PAIRS], bins=50, density=True)
  plt.title("Y")
  plt.savefig("y.png")


if __name__ == '__main__':
  main()