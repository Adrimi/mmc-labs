import numpy as np
from matplotlib import pyplot as plt


def main():
  M = 10**4
  p = 0.9545

  input_data = []
  output = []
  for _ in range(M):
    x1 = np.random.uniform(0, 4)
    x2 = np.random.uniform(5, 6)
    input_data.append((x1, x2))
    output.append(x1 + x2)

  # estymator
  est_y = 1 / M * np.sum(output)
  print('Estymator: ', est_y)

  # odchylenie
  std_dev_input = [(y - est_y)**2 for y in output]
  std_dev = np.sqrt(1 / (M - 1) * np.sum(std_dev_input))
  print('Odchylenie: ', std_dev)

  # przedział rozszerzenia
  q = int(p * M)
  output_sorted = output.copy()
  output_sorted.sort()
  r = int((M - q) / 2)
  if not isinstance(r, int):
    r = int((M - q + 1) / 2)
  y_min = output_sorted[r]
  y_max = output_sorted[r + q]
  print('Przedział rozszerzenia: y_min: ', y_min, 'y_max: ', y_max)

  # GUM - odchylenie
  gum_x1, gum_x2 = zip(*input_data)
  gum_mean_x1 = np.mean(gum_x1)
  gum_mean_x2 = np.mean(gum_x2)
  gum_std_dev_x1 = np.sqrt(1 / len(gum_x1) *
                           np.sum([(x - gum_mean_x1)**2 for x in gum_x1]))
  gum_std_dev_x2 = np.sqrt(1 / len(gum_x2) *
                           np.sum([(x - gum_mean_x2)**2 for x in gum_x2]))
  gum_std_dev = np.sqrt(gum_std_dev_x1**2 + gum_std_dev_x2**2)
  print('Odchylenie GUM: ', gum_std_dev)

  # GUM - prrzedział rozszerzenie
  gum_y_mean = np.mean(output)
  gum_y_min = gum_y_mean - 2 * gum_std_dev
  gum_y_max = gum_y_mean + 2 * gum_std_dev
  print('Przedział rozszerzenia GUM: y_min: ', gum_y_min, 'y_max: ', gum_y_max)

  plt.hist(gum_x1, density=True)
  plt.show()

  plt.hist(gum_x2, density=True)
  plt.show()

  plt.hist(output, density=True)
  plt.show()


if __name__ == '__main__':
  main()