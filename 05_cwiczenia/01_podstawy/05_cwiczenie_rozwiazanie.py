# -*- coding: utf-8 -*-

"""
Sprawdź jaki typ mają następujące zmienne:

x = '1323435'
y = 12334
z = '0'

Wynik podaj przy użyciu jednej funkcji print(). Oczekiwany rezultat:

x: <class 'str'>
y: <class 'int'>
z: <class 'str'>

Wskazówka: Należy skorzystać z funkcji type() w celu sprawdzenia typu zmiennej.
"""

x = '1323435'
y = 12334
z = '0'

print('x: {0}\ny: {1}\nz: {2}'.format(type(x), type(y), type(z)))