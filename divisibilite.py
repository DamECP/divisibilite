from random import sample, shuffle, randint


class Number:
    def __init__(self, value: int, divisors: set):
        self.value = value
        self.divisors = self.get_divisors(divisors)
        self.n_of_divs = len(self.divisors)

    def get_divisors(self, divisors: set):
        self.divs = [
            i
            for i in divisors
            if self.value % i == 0
            # Calcul des diviseurs de 'self.value' parmi
            # ceux fournis par l'utilisateur, 1 est exclu
        ]
        return self.divs


def user_max_value():
    while True:
        try:
            value = int(input("Entrer la valeur max : "))
            return value
        except ValueError:
            print("Entrer un nombre valide")


def user_divisors():
    while True:
        try:
            user_divisors = input(
                "Entrer les diviseurs sélectionnés séparés par une virgule (ex : 3, 5) : "
            )
            divisors = set([int(i.strip()) for i in user_divisors.split(",")])
            return divisors
        except ValueError:
            print("Entrer des nombres entiers valides")


def len_of_exercise():
    while True:
        try:
            examples = int(input("Quantité : "))
            return examples
        except ValueError:
            print("Entrer un nombre valable")


def user_primes():
    while True:
        try:
            primes = int(input('Nombre de réponses "vides" (nombres premiers) : '))
            if primes < 0:
                raise ValueError
            return primes
        except ValueError:
            print("Entrée non valide")


# Paramètres user
max_value = user_max_value()
exercise_divs = user_divisors()
exercise_len = len_of_exercise()
n_of_primes = user_primes()


# Liste avec tous les nombres possibles selon le nombre de diviseurs min attendu
data = [
    n for n in (Number(i, exercise_divs) for i in range(max_value)) if n.n_of_divs >= 1
]

# Liste des nombres premiers dans le range attendu
set_primes = [
    n for n in (Number(i, exercise_divs) for i in range(max_value)) if n.n_of_divs == 0
]

# Vérifications et ajustements
message = "Demande incohérente, quantités ajustées :"

# 1. Trop de nombres premiers demandés
if n_of_primes > len(set_primes):
    print(f"{message} {len(set_primes)} nombres premiers disponibles.")
    n_of_primes = len(set_primes)


# 2. Trop de premiers pour la quantité totale
if n_of_primes > exercise_len:
    print(message)
    n_of_primes = randint(1, exercise_len)

# 3. Trop de non premiers
if exercise_len - n_of_primes > len(data):
    print(message)
    n_of_primes = exercise_len - len(data)


# Génération de la liste selon la quantité de premiers demandée
exercise_set = sample(set_primes, n_of_primes) + sample(
    data, exercise_len - n_of_primes
)

# Mélange la liste
shuffle(exercise_set)

# Affichage
for i in exercise_set:
    print(f"{i.value} : {i.divs}")
