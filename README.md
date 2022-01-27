# mmc-labs

## LAB 6

To compile a file `zad1.cpp` use either:

Have XCode cancer?

```shell
g++ -Wc++11-extensions -std=c++20 -lgsl -lfmt zad1.cpp model_isinga.cpp -o zad1
```

have `g++-11` or `gcc-11`? It works (without `fmt` for some reason, deal with it)

```shell
g++-11 -std=c++20 -lgsl -lfmt -L/usr/local/lib -I/usr/local/include zad1.cpp model_isinga.cpp -o zad1
```

TODO:

- [x] Krzywe wyglądają dobrze, choć lepiej temperaturę wykreślić na osi X – nawet jeśli nie zadajemy jej wprost, to jest jednak lepiej kontrolowana niż magnetyzacja.

- [x] W Zadaniu2 trzeba zmienić formalizm z układu mikrokanonicznego na kanoniczny.

- [x] Tak, kod będzie w dużej mierze taki sam.

- [x] Tyle, że nie ma duszka rozdającego energię, tylko doprowadzamy układ do równowagi w danej temperaturze (którą musimy zadać z góry w konstruktorze – trzeb więc dopisac nowy konstruktor do klasy głównej, przyjmujący wielkość siatki i "double temperatura".

- [ ] Poza tym modyfikujemy – w jednakowy sposób! – dwie funkcje: doprowadzenie do stanu równowagi i zliczanie średnich. Zamiast wymiany energii mamy w obu algorytm Metropolisa taki, jak dr Niewiński przedstawił na wykładzie.

- [ ] To znaczy: sprawdzamy, czy po obróceniu spinu energia wzrośnie, czy zmaleje, jeśli zmaleje, to obracamy (i aktualizujemy wszystkie statystyki typu energia, magnetyzacja itp!), jeśli wzrośnie, to stosujemy **magiczny wzór z eksponensem**, żeby sprawdzić, na ile taka zmiana jest prawdopodobna w danej temperaturze.

- [ ] Losujemy liczbę z przedziału (0, 1) i jeśli jest mniejsza od obliczonego prawdopodobieństwa, to spin obracamy (i aktualizujemy statystyki).

- [ ] Generalnie jednak dobrze byłoby przypomnieć sobie z wykładu, czym się różni układ kanoniczny od mikrokanonicznego.



  
