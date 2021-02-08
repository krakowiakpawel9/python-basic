# -*- coding: utf-8 -*-

"""
Wczytaj plik data.txt przy użyciu metody readlines(). Rezultat (listę)
wydrukuj do konsoli.

Oczekiwany wynik:

['KGHM, 100\n', 'PKN Orlen, 90\n', 'PKO BP, 42']
"""

with open('data.txt', 'r') as file:
    data = file.readlines()
    
print(data)