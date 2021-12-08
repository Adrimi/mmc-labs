#!/usr/bin/python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np

# n  - liczność próby Monte-Carlo,
# y  - estymata całki,
# sd - estymata odchylenia standardowego 'y'.
n, y, sd = np.loadtxt('zad3.txt', unpack=True)

# Składna jak dla 'plot', ale trzeci argument to wysokość pionowego
# słupka błędu, obrazującego niepewność wyznaczania estymaty.
# Obszar pomiędzy górnym i dolnym słupkiem błędu
# to przedział ufności 95 % wyznaczania estymaty.
plt.errorbar(n, y, 2 * sd, fmt='go', label='Estymata Monte Carlo')
# Rzeczywista wartość całki to 1. Wykreślamy ją linią punktową,
# biegnącą przez cały zakres zmienności argumentu 'n'.
plt.plot([min(n), max(n)], [1, 1], 'k:', label='Wartość rzeczywista')
# Skala logarytmiczna na osi X jest konieczna.
plt.xscale('log')
plt.xlabel('Liczność próby')
plt.ylabel('Wartość całki')
plt.legend(loc='best')
plt.savefig('przedzialy.pdf', format='pdf')
plt.show()