from random import sample

# option possible : choisir si réponse nulle ou non

max_value = None
divs = None
exercise_set = None

while True:
    if max_value == None:
        try:
            max_value = int(input("Entrer la valeur max : "))
        except ValueError:
            print("Entrer un nombre valide")
        continue
    if divs == None:
        try:
            user_divs = input(
                "Entrer les diviseurs sélectionnés séparés par une virgule (ex : 3, 5) : "
            )
            divs = set([int(i.strip()) for i in user_divs.split(",")])
        except ValueError:
            print("Entrer des nombres entiers valides")
        continue
    if exercise_set == None:
        try:
            exercise_set = int(input("Quantité de nombres : "))
            if exercise_set > max_value:
                raise ValueError
        except ValueError:
            print("Entrer un nombre valable")
            continue
    break


class Number:
    def __init__(self, value: int):
        self.value = value
        self.div = self.div()

    def div(self):
        self.divs = [
            i
            for i in range(2, (self.value // 2) + 1)
            if self.value % i == 0 and i in divs
        ]
        return self.divs


data = [Number(i) for i in range(max_value) if len(Number(i).div) >= 1]

for i in range(exercise_set):

    example = sample(data, 1)[0]
    print(example.value, example.div)
