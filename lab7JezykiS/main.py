FILEPATH = '/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab7JezykiS/covid.txt'


def open_file(fileName):
    file = open(fileName, 'r')
    return file.readlines()


def create_all_cases(lines):
    all_cases = []
    map(lambda line: all_cases.append((line[6])), lines)
    return all_cases


lines = open_file(FILEPATH)
all_cases = create_all_cases(lines)
for i in all_cases:
    print(i)

print('some new feature')
for i in range(1, 101):
    print(i)

