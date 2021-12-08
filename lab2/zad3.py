from random import uniform
from math import sqrt
from numpy import logspace


def generate_linear_results(number_of_tries):
  points_inside_radix = 0
  total_numer_of_tries = []
  pi_estimations = []
  standard_deviations = []
  V = 4  # because we are operating in 2x2 area

  for n in range(number_of_tries):
    # Get random number form (-1, 1)
    x = uniform(-1, 1)
    y = uniform(-1, 1)

    # Calculate distance from center (0, 0)
    distance = x * x + y * x

    if distance <= 1:
      points_inside_radix += 1

    N = n + 1
    pi = 4 * points_inside_radix / N
    M = points_inside_radix
    standard_deviation = V * sqrt(1 / N * M / N * (1 - M / N))

    total_numer_of_tries.append(N)
    pi_estimations.append(pi)
    standard_deviations.append(standard_deviation)

  return (total_numer_of_tries, pi_estimations, standard_deviations)


def main():
  iterations = 1000000

  N_arr, pi_arr, est_arr = generate_linear_results(iterations)

  with open("zad3.txt", "w") as file:
    for i in logspace(2, 6, dtype='int'):
      if i >= iterations:
        return
      file.write(f'{N_arr[i]} {pi_arr[i]} {est_arr[i]}\n')


if __name__ == '__main__':
  main()