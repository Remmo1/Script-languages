import sys
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
sum = 0

while lineFromUser != "":
    if lineFromUser.isdigit():
        sum = sum + int(lineFromUser)
    counter = counter + 1
    lineFromUser = input(msg)

if counter != 0:
    print("Średnia wynosi: ", "%.3f" % round(int(sum)/int(counter), 3))
else:
    print("Średnia wynosi zero")



# ===================== ZADANIE 3 =========================

# zadanie 1

def check_is_it_palindrom(word):
    return word == word[::-1]


print(check_is_it_palindrom("aabbbbb"))
print(check_is_it_palindrom("ala"))


# zadanie 2

def check_is_it_prime(number):
    for i in range(2, number):
        if number % i == 0:
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
    next = find_next_prime(begin)
    print(next)
    begin = next


# zadanie 4

msg = "Podaj liczbę (lub 2 x enter): "
step = int(input("Podaj krok: "))
lineFromUser = input(msg)

avr = 0
actual = 0
next = 0
result = []

while lineFromUser != "":
    if isfloat(lineFromUser):
        next = float(lineFromUser)
        result.append( (next + actual) / 2 )
        actual = next
    lineFromUser = input(msg)

print(result[1::])

# zadanie 5

precision = float(input("Podaj dokladnosc: "))

actual = 1
next = 4/3
counter = 2
result = next

while True:
    if abs(next - actual) < precision:
        break
    else:
        actual = next
        next = ( 4 * counter * counter ) / ( ( 4 * counter * counter ) - 1)
        result = next * result
        counter = counter + 1

print(str(result * 2))