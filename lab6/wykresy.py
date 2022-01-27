import matplotlib.pyplot as plt


def main():
  experiments = [0, 1, 2]
  for exp in experiments:
    with open(f'lab6/experiment{exp}_zad2.txt', 'r') as file:
      temperatures = []
      energia = []
      magnetyzer = []

      for line in file.readlines():
        if "T " in line:
          temperatures.append(float(line.split()[-1]))
        if "Srednia Magnetyzacja" in line:
          magnetyzer.append(float(line.split()[-1]))
        if "Srednia Energia Ukladu" in line:
          energia.append(float(line.split()[-1]))

      plt.figure()
      plt.plot(temperatures, magnetyzer, label='Magnetyzacja')
      plt.title(f'Eksperyment nr {exp + 1}')
      plt.legend()
      plt.ylabel('Magnetyzacja')
      plt.xlabel('Temperatura')
      plt.grid()
      plt.savefig(f'lab6/exp{exp}-magnet_zad2.png')

      plt.figure()
      plt.plot(temperatures, energia, label='Energia')
      plt.title(f'Eksperyment nr {exp + 1}')
      plt.legend()
      plt.ylabel('Energia')
      plt.xlabel('Temperatura')
      plt.grid()
      plt.savefig(f'lab6/exp{exp}-energy_zad2.png')


if __name__ == '__main__':
  main()