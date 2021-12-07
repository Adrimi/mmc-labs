#!/usr/bin/python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
# Biblioteka wspierająca obliczenia naukowe.
# Importujemy jedynie klasę odpowiedzialną za wyznaczanie
# różnych wielkości charakteryzujących rozkład normalny.
from scipy.stats import norm

dane = np.loadtxt('./dane/gauss.txt', unpack=True)

# Wartości teoretyczne wartości oczekiwanej i odchylenia standardowego.
wart_oczek = 2
odch_std = 2

# Wartości na osi X histogramu.
dziedzina = np.arange(wart_oczek-3*odch_std, wart_oczek+3*odch_std, 0.1)
# Teoretyczna funkcja gęstości prawdopodobieństwa rozkładu normalnego o zadanych parametrach.
fgp = norm.pdf(dziedzina, wart_oczek, odch_std)
# Rysujemy histogram częstości. Histogram liczebności uzyskalibyśmy przy 'normed=False'.
# W nowszej wersji NumPy zamiast 'normed' używamy parametru 'density'.
plt.hist(dane, normed=True, color='blue', alpha=0.3, label='z próby losowej')
# Rysujemy również teoretyczną funkcję gęstości prawodpodobieństwa.
plt.plot(dziedzina, fgp, 'k-', label='teoretyczna')
plt.xlabel('Wartość')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.legend(loc='best')
plt.savefig('./wykresy/histogram.pdf', format='pdf')
plt.show()

# Teoretyczna dystrybuanta rozkładu normalnego o zadanych parametrach.
dystrybuanta = norm.cdf(dziedzina, wart_oczek, odch_std)
# Dystrybuanta empiryczna, czyli histogram skumulowany ('cumulative=True').
# Tym razem wymusiliśmy liczbę przedziałów 'bins'.
plt.hist(dane, bins=20, normed=True, color='red', alpha=0.3,
         cumulative=True, label='z próby losowej')
plt.plot(dziedzina, dystrybuanta, 'k-', label='teoretyczna')
plt.xlabel('Wartość')
plt.ylabel('Dystrybuanta')
plt.legend(loc='best')
plt.savefig('./wykresy/dystrybuanta.pdf', format='pdf')
plt.show()
