# Zadanie 1
import sys

list = []

for line in sys.stdin:
    for var in line.split():
        if var == '\n': break
        list.append(int(var))

for i in range(0, len(list)):
    print(list[i])



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
begin = startNumber + 1

for i in range(0, amountOfNumbers):
    next = find_next_prime(begin)
    print(next)
    begin = next

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