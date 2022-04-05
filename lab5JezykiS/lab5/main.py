from fastnumbers import isfloat

# Zadanie 1

msg = "Podaj liczbę kandydata na maksimum lub zakończ (2 razy enter): "
lineFromUser = input(msg)
maxiumum = lineFromUser

while lineFromUser != "":
    if lineFromUser.isdigit() and int(lineFromUser):
        maximum = int(lineFromUser)
    lineFromUser = input(msg)

print("Maksimum: ", maximum)

# Zadanie 2
msg = "Podaj liczbę do średniej lub zakończ (2 razy enter): "
lineFromUser = input(msg)
counter = 0
sumToAvr = 0

while lineFromUser != "":
    if lineFromUser.isdigit():
        sumToAvr = sumToAvr + int(lineFromUser)
    counter = counter + 1
    lineFromUser = input(msg)

if counter != 0:
    print("Średnia wynosi: ", "%.3f" % round(int(sumToAvr) / int(counter), 3))
else:
    print("Średnia wynosi zero")


# ===================== ZADANIE 3 =========================

# zadanie 1

def check_is_it_palindrom(word):
    return word == word[::-1]


wordF = input("Podaj napis do sprawdzenia: ")

print(check_is_it_palindrom(wordF))


# zadanie 2

def check_is_it_prime(number):
    for j in range(2, number):
        if number % j == 0:
            return False
    return True


def find_next_prime(number):
    if number <= 1:
        return 2

    n = number + 1
    while True:
        if check_is_it_prime(n):
            return n
        else:
            n = n + 1


someNumber = int(input("Podaj liczbe: "))
print("The next prime number is: ", find_next_prime(someNumber))

# zadanie 3

startNumber = int(input("Podaj liczbe startowa: "))
amountOfNumbers = int(input("Podaj ile liczb wypisac: "))
begin = startNumber

for i in range(0, amountOfNumbers):
    nextNumber = find_next_prime(begin)
    print(nextNumber)
    begin = nextNumber


# zadanie 4

msg = "Podaj liczbę (lub 2 x enter): "
step = int(input("Podaj krok: "))
lineFromUser = input(msg)

numbers = []
result = []

while lineFromUser != "":
    if isfloat(lineFromUser):
        numbers.append(float(lineFromUser))
        if len(numbers) == step:
            result.append(sum(numbers) / step)
            numbers.pop(0)
    lineFromUser = input(msg)

print(result)

# zadanie 5

precision = float(input("Podaj dokladnosc: "))

actualN = 1
nextNumber = 4 / 3
counter = 2
result = nextNumber

while True:
    if abs(nextNumber - actualN) < precision:
        break
    else:
        actualN = nextNumber
        nextNumber = (4 * counter * counter) / ((4 * counter * counter) - 1)
        result = nextNumber * result
        counter = counter + 1

print(str(result * 2))
