#include <stdio.h>
#include <iostream>
#include <random>
#include <list>
#include <cmath>
#include <map>
#include <vector>
#include <utility>
#include <gsl/gsl_rng.h>

std::map<unsigned long int, unsigned long int> generator(const gsl_rng_type *type, int k, int n)
{
  gsl_rng_env_setup();

  const gsl_rng_type *T = type;
  gsl_rng *r = gsl_rng_alloc(T);

  std::map<unsigned long int, unsigned long int> samples;

  for (int i = 0; i < k; i++)
  {
    samples.insert(std::pair<unsigned long int, unsigned long int>(i, 0));
  }

  for (int i = 0; i < n; i++)
  {
    unsigned long int s = gsl_rng_uniform(r) * k;
    ++samples[int(s)];
  }

  gsl_rng_free(r);

  return samples;
}

int main()
{
  std::vector<int> keys;
  keys.push_back(11);
  keys.push_back(51);
  keys.push_back(101);

  std::vector<double> critical_values_0_05;
  critical_values_0_05.push_back(18.307);  // for df = 10
  critical_values_0_05.push_back(67.505);  // for df = 50
  critical_values_0_05.push_back(124.342); // for df = 100

  int n = 100000;

  // Good generator case
  for (int i = 0; i < 3; i++)
  {
    int k = keys[i];
    double average_value = n / k;
    std::map<unsigned long int, unsigned long int> samples = generator(gsl_rng_ranlux, k, n);
    unsigned long int sum = 0;

    for (int i = 0; i < k; i++)
    {
      sum += samples[i] * samples[i];
    }

    double result = ((double)k * (double)sum) / (double)n - (double)n;

    std::cout << std::endl;
    std::cout << "Result from GOOD rng generator for " << n << " total probes and " << k << " intervals is " << result << std::endl;

    if (result > critical_values_0_05[i])
    {
      std::cout << "Result " << result << " is higher than critical value of " << critical_values_0_05[i] << std::endl;
    }
    else
    {
      std::cout << "Result " << result << " is lower than critical value of " << critical_values_0_05[i] << std::endl;
    }
  }

  // Bad generator case
  for (int i = 0; i < 3; i++)
  {
    int k = keys[i];
    double average_value = n / k;
    std::map<unsigned long int, unsigned long int> samples = generator(gsl_rng_rand, k, n);
    unsigned long int sum = 0;

    for (int i = 0; i < k; i++)
    {
      sum += samples[i] * samples[i];
    }

    double result = ((double)k * (double)sum) / (double)n - (double)n;

    std::cout << std::endl;
    std::cout << "Result from BAD rng generator for " << n << " total probes and " << k << " intervals is " << result << std::endl;

    if (result > critical_values_0_05[i])
    {
      std::cout << "Result " << result << " is higher than critical value of " << critical_values_0_05[i] << std::endl;
    }
    else
    {
      std::cout << "Result " << result << " is lower than critical value of " << critical_values_0_05[i] << std::endl;
    }
  }
  return 0;
}