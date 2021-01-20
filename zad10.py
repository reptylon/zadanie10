import re

bridge_of_death = '''
-Jaki jest twój ulubiony kolor?
-Niebieski!
-Dobrze. Idź.
...
-Stój. Jakie jest twe imię?
-Sir Galahad z Camelotu.
-Jaki jest twój cel?
-Odnaleźć Graala.
-Jaki jest twój ulubiony kolor?
-Niebieski... nie... żóóóółtyyyy!
'''

pattern = re.compile(r'[A-Za-ząćęłńóśźżĄĘŁŃÓŚŹŻ]{4,}')
result = set(pattern.findall(bridge_of_death))

for word in result:
    print(word)