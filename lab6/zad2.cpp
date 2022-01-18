#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <fmt/core.h>
#include "model_isinga.h"

using namespace std;

int main(int argc, char *argv[])
{
	int experiments[3] = {10, 20, 40};

	// TODO: Implement algorytm Creutza
	for (int x = 0; x < size(experiments); x++)
	{
		int size = experiments[x];

		model_isinga *p1 = new model_isinga(size, -184);
		p1->doprowadzenie_do_stanu_rownowagi_creutz();
		// outdata << "Srednia Energia Ukladu = " << p1->podaj_srednia_energie_ukladu() << endl;
		cout << "Srednia Energia Duszka =  " << p1->podaj_srednia_energie_duszka() << endl;
		// outdata << "Srednia Magnetyzacja   =  " << p1->podaj_srednia_magnetyzacje() << endl;
		cout << "T = " << p1->podaj_temperature() << endl;

		delete p1;
	}

	return 0;
}
