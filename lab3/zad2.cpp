#include <iostream>
#include <fstream>
#include <random>
#include <math.h>
#include <chrono>
#include <vector>

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

void save_to_file(std::string filename, std::vector<std::pair<double, double>> input)
{
  std::ofstream ofs;
  ofs.open(filename);

  for (int i = 0; i < input.size(); i++)
  {
    ofs << input[i].first << " " << input[i].second << std::endl;
  }

  ofs.close();
}

int main()
{
  using std::chrono::duration;
  using std::chrono::high_resolution_clock;

  int iterations = 100000;

  std::vector<std::pair<double, double>> box_mueller_values;
  std::vector<std::pair<double, double>> marsaglii_bray_values;

  auto t1 = high_resolution_clock::now();
  for (int i = 0; i < iterations; i++)
  {
    std::pair<double, double> experiment_value = box_mueller();
    box_mueller_values.push_back(experiment_value);
  }
  auto t2 = high_resolution_clock::now();

  /* Getting number of milliseconds as a double. */
  duration<double, std::milli> ms_double = t2 - t1;
  std::cout << "Box mueller experiment took " << ms_double.count() << " ms." << std::endl;

  auto t3 = high_resolution_clock::now();
  for (int i = 0; i < iterations; i++)
  {
    std::pair<double, double> experiment_value = marsaglii_braya();
    marsaglii_bray_values.push_back(experiment_value);
  }
  auto t4 = high_resolution_clock::now();

  /* Getting number of milliseconds as a double. */
  duration<double, std::milli> ms_double_2 = t4 - t3;
  std::cout << "Marsaglii Bray experiment took " << ms_double_2.count() << " ms." << std::endl;

  /* Save to file */
  save_to_file("zad2_box_mueller.txt", box_mueller_values);
  save_to_file("zad2_marsaglii_bray.txt", marsaglii_bray_values);

  return 0;
}