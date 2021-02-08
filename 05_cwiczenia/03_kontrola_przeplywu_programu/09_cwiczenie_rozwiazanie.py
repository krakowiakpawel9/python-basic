# -*- coding: utf-8 -*-

"""
Podana jest lista:

lista = [1, 2, 99, 4, 5]

Wydrukuj wszystkie cyfry do konsoli używając pętli for, pomiń wartość 99 
(każda cyfra w osobnej linii)

Wskazówka: Skorzystaj z instrukcji continue

Oczekiwany wynik:

1
2
4
5
"""

lista = [1, 2, 99, 4, 5]
for i in lista:
    if i == 99:
        continue
    print(i)