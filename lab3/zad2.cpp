#include <iostream>
#include <random>
#include <math.h>

#define PI 3.141592653589793

double power(double base, double exponent)
{
  if (base < 0)
  {
    return pow((-1) * base, exponent);
  }
  else
  {
    return pow(base, exponent);
  }
}

double standart_twodim_generator(double x, double y)
{
  return (1 / (2 * PI)) * exp((-1) * (power(x, 2) + power(y, 2)) / 2);
}

double uniform_random_number(double min, double max)
{
  std::uniform_real_distribution<double> unif(min, max);
  std::default_random_engine re;
  return (double)unif(re);
}

double box_mueller(double min, double max)
{
  double u1 = uniform_random_number(min, max);
  double u2 = uniform_random_number(min, max);

  double x = (sqrt((-2) * log(u1)) * cos(2 * PI * u2));
  double y = (sqrt((-2) * log(u1)) * sin(2 * PI * u2));

  return standart_twodim_generator(x, y);
}

int main()
{
  double random_number_2 = log(-1.0);
  std::cout << random_number_2 << std::endl;

  return 0;
}