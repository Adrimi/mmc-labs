#include <iostream>
#include <cstdlib>
#include "model_isinga.h"

using namespace std;

int main(int argc, char *argv[])
{
	cout << "Symulacja modelu Isinga w Zespole Mikrokanonicznym" << endl;

	for (int j = 10; j < 41; j++)
	{
		if (j == 10 or j == 20 or j == 40)
		{
			for (int i = -184; i < -23; i = i + 8)
			{
				cout << "Symulacja modelu Isinga w Zespole Mikrokanonicznym" << endl;
				model_isinga *p1 = new model_isinga(j, i);
				p1->doprowadzenie_do_stanu_rownowagi(1000);
				p1->zliczanie_srednich(1000);
				cout << "Srednia Energia Ukladu = " << p1->podaj_srednia_energie_ukladu() << endl;
				cout << "Srednia Energia Duszka =  " << p1->podaj_srednia_energie_duszka() << endl;
				cout << "Srednia Magnetyzacja   =  " << p1->podaj_srednia_magnetyzacje() << endl;
				cout << "T = " << p1->podaj_temperature() << endl;

				cout << "-----------------\n";
				delete p1;
			}
		}
	}

	return 0;
}
