#include "model_isinga.h"
#include <iostream>

model_isinga::model_isinga()
{
	L = 10;
	E = -192;
	siatka = new int *[L];
	for (int i = 0; i < L; i++)
		siatka[i] = new int[L];
}

model_isinga::model_isinga(int rozmiar, int energia)
{
	L = rozmiar;
	E = energia;
	siatka = new int *[L];
	for (int i = 0; i < L; i++)
		siatka[i] = new int[L];

	generatorek = gsl_rng_alloc(gsl_rng_default);
	gsl_rng_set(generatorek, 3987);
}

model_isinga::~model_isinga()
{
	if (siatka != NULL)
	{
		for (int i = 0; i < L; i++)
			delete[] siatka[i];
		delete[] siatka;
	}
	gsl_rng_free(generatorek);
}

void model_isinga::ustaw_same_jedynki()
{
	for (int i = 0; i < L; i++)
		for (int j = 0; j < L; j++)
			siatka[i][j] = 1;
}

void model_isinga::doprowadzenie_do_stanu_rownowagi(int liczba_krokow)
{
	int i, j, dE;
	magnetyzacja = L * L;
	E_Start = -2 * L * L;
	E_Duszka = E - E_Start;
	ustaw_same_jedynki();

	for (int k = 0; k < liczba_krokow; k++)
	{
		i = (int)floor(gsl_rng_uniform(generatorek) * L);
		j = (int)floor(gsl_rng_uniform(generatorek) * L);
		dE = Delta_E(i, j);
		if (dE <= E_Duszka)
		{
			E_Duszka -= dE;
			E_Start += dE;
			siatka[i][j] = -siatka[i][j];
			magnetyzacja += 2 * siatka[i][j];
		}
	}
}

// https://www.youtube.com/watch?v=yaY8iNZx7xc
void model_isinga::doprowadzenie_do_stanu_rownowagi_creutz()
{
	int i, j, dE;
	int E_Duszka_Do_Sredniej = 0;
	int liczba_krokow = 0;
	magnetyzacja = L * L;
	E_Start = -2 * L * L;
	// 1. Ustalić początkową energię duszka
	E_Duszka = E - E_Start;
	ustaw_same_jedynki();

	do
	{
		// Petla statystycznie po kazdym spinie
		for (int k = 0; k < L * L; k++)
		{
			// 2. Wybrać w sposób losowy spin układu, a następnie dokonać zmiany stanu układu (zmiana stanu układu na koniec!)
			i = (int)floor(gsl_rng_uniform(generatorek) * L);
			j = (int)floor(gsl_rng_uniform(generatorek) * L);

			// 3. Obliczyć różnicę energii między stanami i oraz j
			dE = Delta_E(i, j);

			// 4. Jeżeli dE < 0, to nowa konfiguracja układu zostaje zaakceptowana, a różnica energii przekazana duszkowi. Powrót do punktu 2.
			if (dE < 0)
			{
				E_Duszka += dE;
				// magnetyzacja += 2 * siatka[i][j];
			}
			// 5. Jeżeli dE > 0, to akceptacja nowej konfiguracji układu następuje jedynie w przypadku, gdy dE + E_Duszka > 0. Wówczas konieczną energię pobiera się od duszka.
			else if (dE > 0 && dE + E_Duszka > 0)
			{
				E_Duszka -= dE;
			}

			// Zmiana stanu układu
			siatka[i][j] = -siatka[i][j];
		}

		// Statystyka
		// Jako jeden krok MC należy rozumieć próbę zmiany przynajmniej raz (statystycznie) stanu każdego spinu
		liczba_krokow++;
		E_Duszka_Do_Sredniej += E_Duszka;
		std::cout << E_Duszka << std::endl;
	} while (E_Duszka >= E);

	std::cout << "Energia koncowa duszka: " << E_Duszka << std::endl;

	// Obliczanie srednich
	// Srednia_Energia_Ukladu = E_tot / (float)liczba_krokow;
	Srednia_E_Duszka = (float)(E_Duszka_Do_Sredniej) / (float)liczba_krokow;
	std::cout << "srednia duszka: " << Srednia_E_Duszka << std::endl;
	std::cout << "kroki: " << liczba_krokow << std::endl;
	// Srednia_Magnetyzacja = magnetyzacja_tot / (float)liczba_krokow / ((float)L * (float)L);
	Temperatura = 4.0 / (log(1 + 4.0 / Srednia_E_Duszka));
}

// Oblicza roznice energii przy zmianie kierunku spinu
// przy zalozeniu periodycznych warunkow brzegowych
int model_isinga::Delta_E(int i, int j)
{
	int lewy, prawy, gorny, dolny;
	int E_pocz, E_konc;

	// Y-axis boundry
	gorny = i - 1;
	dolny = i + 1;
	if (i == 0)
		gorny = L - 1;
	if (i == L - 1)
		dolny = 0;

	// X-axis boundry
	prawy = j + 1;
	lewy = j - 1;
	if (j == 0)
		lewy = L - 1;
	if (j == L - 1)
		prawy = 0;

	// Compute change in energy
	E_pocz = siatka[i][j] * (siatka[i][lewy] + siatka[i][prawy] + siatka[gorny][j] + siatka[dolny][j]);
	E_konc = -E_pocz;

	return E_pocz - E_konc;
}

// Wyznacza srednia Energie Duszka, Energie ukladu, Magnetyzacje oraz Temperature
void model_isinga::zliczanie_srednich(int liczba_krokow)
{
	int E_Duszka_Do_Sredniej = 0, i, j, dE;
	int magnetyzacja_tot = 0;
	int E_tot = 0;
	int przed, po;

	// Petla liczby_krokow
	for (int l = 0; l < liczba_krokow; l++)
	{
		// Petla statystycznie po kazdym spinie
		for (int k = 0; k < L * L; k++)
		{
			i = (int)floor(gsl_rng_uniform(generatorek) * L);
			j = (int)floor(gsl_rng_uniform(generatorek) * L);
			dE = Delta_E(i, j);
			if (dE <= E_Duszka)
			{
				siatka[i][j] = -siatka[i][j];
				E_Duszka -= dE;
				E_Start += dE;
				magnetyzacja += 2 * siatka[i][j];
			}
		}
		E_Duszka_Do_Sredniej += E_Duszka;
		E_tot += E_Start;
		magnetyzacja_tot += abs(magnetyzacja);
	}

	// Obliczanie srednich
	Srednia_Energia_Ukladu = E_tot / (float)liczba_krokow;
	Srednia_E_Duszka = (float)(E_Duszka_Do_Sredniej) / (float)liczba_krokow;
	Srednia_Magnetyzacja = magnetyzacja_tot / (float)liczba_krokow / ((float)L * (float)L);
	Temperatura = 4.0 / (log(1 + 4.0 / Srednia_E_Duszka));
}

float model_isinga::podaj_srednia_energie_duszka()
{
	return Srednia_E_Duszka;
}

float model_isinga::podaj_srednia_energie_ukladu()
{
	return Srednia_Energia_Ukladu;
}

float model_isinga::podaj_srednia_magnetyzacje()
{
	return Srednia_Magnetyzacja;
}

float model_isinga::podaj_temperature()
{
	return Temperatura;
}
