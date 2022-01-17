#include <iostream>
#include <cstdlib>
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

	for (EXPERIMENT_CONFIGURATION exp : experiments)
	{
		for (int i = exp.minimalEnergy; i < exp.maximalEnergy; i += exp.step)
		{
			cout << "Symulacja modelu Isinga w Zespole Mikrokanonicznym" << endl;
			model_isinga *p1 = new model_isinga(exp.size, i);
			p1->doprowadzenie_do_stanu_rownowagi(1000);
			p1->zliczanie_srednich(1000);
			cout << "Srednia Energia Ukladu = " << p1->podaj_srednia_energie_ukladu() << endl;
			cout << "Srednia Energia Duszka =  " << p1->podaj_srednia_energie_duszka() << endl;
			cout << "Srednia Magnetyzacja   =  " << p1->podaj_srednia_magnetyzacje() << endl;
			cout << "T = " << p1->podaj_temperature() << endl;

			cout << "-----------------\n";
			delete p1;
		}
		cout << "\n\nZakonczono eksperyment\n\n";
	}

	return 0;
}
