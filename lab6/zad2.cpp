#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <vector>
#include <fmt/core.h>
#include "model_isinga.h"

using namespace std;

int main(int argc, char *argv[])
{
	int experiments[3] = {10, 20, 40};

	for (int x = 0; x < size(experiments); x++)
	{
		int size = experiments[x];
		// Open output file
		ofstream outdata;
		outdata.open(fmt::format("experiment{0}_zad2.txt", x));

		cout << fmt::format("\nRozpoczeto eksperyment nr {}", x + 1);

		for (float t = 1.0; t <= 10.0; t += 0.2)
		{
			model_isinga *p1 = new model_isinga(size, t);
			p1->doprowadzenie_do_stanu_rownowagi2(1000);
			p1->zliczanie_srednich2(1000);
			outdata << "------------------------------------------------" << endl;
			outdata << "T = " << t << endl;
			outdata << "Srednia Energia Ukladu = " << p1->podaj_srednia_energie_ukladu() << endl;
			outdata << "Srednia Magnetyzacja   =  " << p1->podaj_srednia_magnetyzacje() << endl;

			delete p1;
		}

		cout << fmt::format("\nZakonczono eksperyment nr {}", x + 1);
		outdata.close();
	}

	return 0;
}
