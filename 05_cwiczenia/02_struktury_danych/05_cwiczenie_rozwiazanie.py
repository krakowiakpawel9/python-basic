# -*- coding: utf-8 -*-

"""
Podane są dwie listy:

[4, 5, 3, 3]
[9, 7]

Używając odpowiedniej metody połącz te dwie listy w jedną i wydrukuj do konsoli.

Oczekiwany wynik:

[4, 5, 3, 3, 9, 7]
"""

l1 = [4, 5, 3, 3]
l2 = [9, 7]

l1.extend(l2)
print(l1)