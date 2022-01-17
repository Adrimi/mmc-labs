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
