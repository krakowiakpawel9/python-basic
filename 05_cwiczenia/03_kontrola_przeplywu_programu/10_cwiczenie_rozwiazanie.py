# -*- coding: utf-8 -*-

"""
Przeszukaj czy podana lista:

numbers = [23, 12, 53, 13, 65, 1, 45]

zawiera wartość 13. Skorzystaj z pętli while. Jeżeli wartość zostanie 
znaleziona wydrukuj:

Znaleziono

Oczekiwany wynik:

Znaleziono
"""

numbers = [23, 12, 53, 13, 65, 1, 45]
i = 0
while i < len(numbers):
    if numbers[i] == 13:
        print('Znaleziono')
        break
    i += 1