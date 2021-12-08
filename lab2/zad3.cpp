#include <iostream>
#include <random>
#include <fstream>

int main()
{
  std::ofstream outfile;
  outfile.open("zad3.txt");

  std::random_device rd;
  std::mt19937 randomSource(rd());
  std::uniform_real_distribution<float> uniform;
  long unsigned int N = 1e6, M = 0, counter = 1, step = N / 100;
  float x, y;

  for (long unsigned i = 0; i < N; i++, counter++)
  {
    x = uniform(randomSource);
    y = uniform(randomSource);
    float d = x * x + y * y;
    if (d <= 1)
      M++;
    if (counter % step == 0)
    {
      float pi = float(4 * M) / counter;
      float est = 4 * sqrt((1 / (double)N) * ((double)M / (double)N) * (double)(1 - (double)M / (double)N));

      outfile << counter << " " << pi << " " << est << std::endl;
      std::cout << counter << " " << (float)M / counter << std::endl;
    }
  }
  return 0;
}
