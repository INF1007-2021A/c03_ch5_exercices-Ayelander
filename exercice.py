#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number *= -1
    return number

# Solution alternative:
# return number if number > 0 else number *= -1
# Utile pour faire les choses en une seule ligne
# Si le code est complexe, cette approche n'est pas à privilégier


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    for first_char in prefixes:
        print(first_char + suffixe)

# Solution alternative:
# liste_nom = []

# for letter in prefixes:
#   liste_nom.append(letter + suffixe)

def is_prime(number: int) -> bool:
    for i in range(2, round((number/2)+1)):
        if number % i == 0:
            return True
    return False

def prime_integer_summation() -> int:
    n = int(input("How many primes do you want to sum?"))
    i = 2 # 0 and 1 are not prime kekw

    list_of_primes = []

    nb_prime = 0

    while nb_prime <= n:
        if is_prime(i):
            list_of_primes.append(i)
            nb_prime += 1
        i += 1
    return sum(list_of_primes)

# Solution alternative 1:

# somme = 0

# liste_premiers = [2, 3, 5, 7, 11, ...]

# for nombre in liste_premiers:
#    somme += nombre

# Solution alternative 2:

# somme = 0

# liste_premiers = [2, 3, 5, 7, 11, ...]

#   return sum(liste_premiers)

def factorial(number: int) -> int:
    result = 1
    if number < 0:
        print("This number has no factorial")
    elif number == 0:
        print("This number's factorial is 1")
    elif number > 0:
        for i in range(1,number+1):
            result *= i
    return result

# Solution alternative:

# while number > 1
# result *= number
# number -= 1

def use_continue() -> None:
    i = 1
    for i in range (1,10):
        if i == 5:
            continue
        print(i)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    return []


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
