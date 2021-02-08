# -*- coding: utf-8 -*-

"""
Utwórz listę z podanych nazw technologii:

> python
> java
> sql
> sas

Następnie zapisz każdy element listy w nowej linii pliku techs.txt.
"""

techs = ['python', 'java', 'sql', 'sas']
with open('techs.txt', 'w') as file:
    for tech in techs:
        print(tech, file=file)