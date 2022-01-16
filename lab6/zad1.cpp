#include <iostream>
#include <cstdlib>
#include "model_isinga.h"

using namespace std;

int main(int argc, char *argv[])
{
	cout << "Symulacja modelu Isinga w Zespole Mikrokanonicznym" << endl;
	model_isinga *p1 = new model_isinga(10, -184);
	p1->doprowadzenie_do_stanu_rownowagi(1000);
	p1->zliczanie_srednich(1000);
	cout << "Srednia Energia Ukladu = " << p1->podaj_srednia_energie_ukladu() << endl;
	cout << "Srednia Energia Duszka =  " << p1->podaj_srednia_energie_duszka() << endl;
	cout << "Srednia Magnetyzacja   =  " << p1->podaj_srednia_magnetyzacje() << endl;
	cout << "T = " << p1->podaj_temperature() << endl;

	delete p1;
	return 0;
}
