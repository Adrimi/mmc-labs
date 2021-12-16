#include <iostream>
#include <fstream>
#include <random>
#include <math.h>

#define PI 3.141592653589793

std::uniform_real_distribution<float> uniform;
std::random_device rd;
std::mt19937 randomSource(rd());

double standart_twodim_generator(double x, double y)
{
  return (1.0 / (2.0 * PI)) * exp((-1.0) * (pow(x, 2.0) + pow(y, 2.0)) / 2.0);
}

double randomix_2000(double min, double max)
{
  return (double)uniform(randomSource) * max;
}

std::pair<double, double> marsaglii_braya()
{
  double u, v;
  double b = 0;

  do
  {
    u = randomix_2000(0, 1);
    v = randomix_2000(0, 1);
    b = u * u + v * v;
  } while (b >= 1);

  double z = sqrt(-2.0 * log(b) / b);

  return std::pair<double, double>(u * z, v * z);
}

std::pair<double, double> box_mueller()
{
  double u1 = randomix_2000(0, 1);
  double u2 = randomix_2000(0, 1);

  double x = (sqrt((-2) * log(u1)) * cos(2 * PI * u2));
  double y = (sqrt((-2) * log(u1)) * sin(2 * PI * u2));

  return std::pair<double, double>(x, y);
}

int main()
{
  std::ofstream ofs;
  int iterations = 100000;

  ofs.open("zad2_box_muller.txt");

  for (int i = 0; i < iterations; i++)
  {
    auto point = box_mueller();
    ofs << point.first << " " << point.second << std::endl;
  }

  ofs.close();

  ofs.open("zad2_marsaglii_braya.txt");

  for (int i = 0; i < iterations; i++)
  {
    auto point = marsaglii_braya();
    ofs << point.first << " " << point.second << std::endl;
  }

  ofs.close();

  return 0;
}