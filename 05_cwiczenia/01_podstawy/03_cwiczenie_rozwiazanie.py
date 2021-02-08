# -*- coding: utf-8 -*-

"""
Utwórz trzy zmienne:

> kwota_poczatkowa
> stopa_procentowa
> okres_trwania 

i przypisz odpowiednio wartości 1000 PLN, 5%, 2 lata.

Oblicz wartość inwestycji kwoty początkowej po 2 latach. Zakładamy kapitalizację roczną. 
Podana stopa procentowa jest stopą w skali roku (w obliczeniach należy ją zamienić na ułamek.)
Spróbuj sam zastanowić się nad problemem, jeżeli będziesz potrzebował wsparcia, skorzystaj ze wskazówki poniżej.

Uwaga: Aby zadanie zostało zaliczone poprawnie należy wydrukować tylko właściwy wynik do konsoli funkcją print().

Wskazówka: wzór na wartość przyszłą możemy zapisać w następujący sposób  fv = pv * (1 + r)**n, gdzie:

> fv - wartość przyszła
> pv - wartość początkowa
> r - stopa procentowa
> n - liczba okresów
"""

kwota_poczatkowa = 1000
stopa_procentowa = 0.05
okres_trwania = 2

fv = kwota_poczatkowa * (1 + stopa_procentowa) ** okres_trwania
print(fv)