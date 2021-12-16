#include <iostream>
#include <fstream>
#include <random>
#include <math.h>
#include <chrono>
#include <vector>

std::uniform_real_distribution<float> uniform;
std::random_device rd;
std::mt19937 randomSource(rd());

double randomix_2000(double min, double max)
{
  return (double)uniform(randomSource) * max;
}

double random_number_from_probability_density(double x)
{
  return (5.0 / 12.0) * (1.0 + pow(x - 1.0, 4.0));
}

double acceptance_rejection()
{
  double u1, u2;

  do
  {
    u1 = randomix_2000(0, 2);
    u2 = randomix_2000(0, 2);
  } while (u2 >= random_number_from_probability_density(u1));

  return u1;
}

double superposition()
{
  double u1 = randomix_2000(0, 2);
  double u2 = randomix_2000(0, 1);

  if (u2 >= 5.0 / 6.0)
  {
    double sign;
    if (u1 - 1.0 < 0)
    {
      sign = -1.0;
    }
    else
    {
      sign = 1.0;
    }
    return (1.0 + sign * pow(abs(u1 - 1.0), (1.0 / 5.0)));
  }
  else
  {
    return u1;
  }
}

void save_to_file(std::string filename, std::vector<double> input)
{
  std::ofstream ofs;
  ofs.open(filename);

  for (int i = 0; i < input.size(); i++)
  {
    ofs << input[i] << std::endl;
  }

  ofs.close();
}

int main()
{
  using std::chrono::duration;
  using std::chrono::high_resolution_clock;

  int iterations = 100000;

  std::vector<double> acceptance_rejection_experiment;
  std::vector<double> superposition_experiment;

  auto t1 = high_resolution_clock::now();

  for (int i = 0; i < iterations; i++)
  {
    double experiment_value = acceptance_rejection();
    acceptance_rejection_experiment.push_back(experiment_value);
  }

  auto t2 = high_resolution_clock::now();

  /* Getting number of milliseconds as a double. */
  duration<double, std::milli> ms_double = t2 - t1;
  std::cout << "Acceptance-rejection experiment took " << ms_double.count() << " ms." << std::endl;

  auto t3 = high_resolution_clock::now();

  for (int i = 0; i < iterations; i++)
  {
    double experiment_value = superposition();
    superposition_experiment.push_back(experiment_value);
  }

  auto t4 = high_resolution_clock::now();

  /* Getting number of milliseconds as a double. */
  duration<double, std::milli> ms_double_2 = t4 - t3;
  std::cout << "Superposition experiment took " << ms_double_2.count() << " ms." << std::endl;

  /* Save to file */

  save_to_file("zad3_elimination.txt", acceptance_rejection_experiment);
  save_to_file("zad3_superposition.txt", superposition_experiment);

  return 0;
}