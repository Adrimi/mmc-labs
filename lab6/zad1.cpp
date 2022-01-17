#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <fmt/core.h>
#include "model_isinga.h"

using namespace std;

// https://youtu.be/K--1hlv9yv0
/** 
 * Once wise man said:
 * Pierwsze ci służy do tego żeby ustalić w jakim zakresie zmieniać temperaturę
 * Ale drugie zadanie tam dwie funkcje trzeba zmienić
 * A w drugim zmieniasz i wykres to ma być zmiany energii czy jakoś tak
*/

struct EXPERIMENT_CONFIGURATION
{
	int minimalEnergy;
	int maximalEnergy;
	int step;
	int size;
};

int main(int argc, char *argv[])
{
	EXPERIMENT_CONFIGURATION experiments[3] = {{-184, -24, 8, 10}, {-768, -32, 32, 20}, {-3072, -128, 128, 40}};

	for (int x = 0; x < size(experiments); x++)
	{
		EXPERIMENT_CONFIGURATION exp = experiments[x];

		// Open output file
		ofstream outdata;
		outdata.open(fmt::format("experiment{0}.txt", x));

		cout << fmt::format("\nRozpoczeto eksperyment nr {}", x + 1);

		for (int i = exp.minimalEnergy; i < exp.maximalEnergy; i += exp.step)
		{
			outdata << "Symulacja modelu Isinga w Zespole Mikrokanonicznym" << endl;
			model_isinga *p1 = new model_isinga(exp.size, i);
			p1->doprowadzenie_do_stanu_rownowagi(1000);
			p1->zliczanie_srednich(1000);
			outdata << "Srednia Energia Ukladu = " << p1->podaj_srednia_energie_ukladu() << endl;
			outdata << "Srednia Energia Duszka =  " << p1->podaj_srednia_energie_duszka() << endl;
			outdata << "Srednia Magnetyzacja   =  " << p1->podaj_srednia_magnetyzacje() << endl;
			outdata << "T = " << p1->podaj_temperature() << endl;

			delete p1;
		}

		cout << fmt::format("\nZakonczono eksperyment nr {}", x + 1);
		outdata.close();
	}

	return 0;
}
