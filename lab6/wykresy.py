import matplotlib.pyplot as plt


def main():
  experiments = [0, 1, 2]
  for exp in experiments:
    with open(f'experiment{exp}.txt', 'r') as file:
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
      plt.plot(magnetyzer, temperatures, label='Magnetyzacja')
      plt.title(f'Eksperyment nr {exp + 1}')
      plt.legend()
      plt.xlabel('Magnetyzacja')
      plt.ylabel('Temperatura')
      plt.grid()
      plt.savefig(f'exp{exp}-magnet.png')

      plt.figure()
      plt.plot(energia, temperatures, label='Energia')
      plt.title(f'Eksperyment nr {exp + 1}')
      plt.legend()
      plt.xlabel('Energia')
      plt.ylabel('Temperatura')
      plt.grid()
      plt.savefig(f'exp{exp}-energy.png')


if __name__ == '__main__':
  main()