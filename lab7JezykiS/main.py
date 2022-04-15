import functools
from timeit import default_timer as timer

# ====================== Zadanie 1 ===============================
#               Tworzenie potrzebnych struktur

FILEPATH = '/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab7JezykiS/covid.txt'


def open_file(filename):
    file = open(filename, 'r')
    return file.readlines()


def create_all_cases(lines_from_file):
    all_cases_list = []
    for line in lines_from_file:
        line = line.split('\t')
        try:
            all_cases_list.append(
                (
                    line[6],  # nazwa kraju
                    int(line[3]),  # rok
                    int(line[2]),  # miesiac
                    int(line[1]),  # dzien
                    int(line[5]),  # zgony
                    int(line[4])  # przypadki
                )
            )
        except ValueError:
            pass
    return all_cases_list


def create_by_date(lines_from_file):
    by_date_dict = {}
    for line in lines_from_file:
        line = line.split('\t')
        try:
            key = (int(line[3]), int(line[2]), int(line[1]))
            if key not in by_date_dict:
                by_date_dict[key] = [(
                    line[6],
                    int(line[5]),
                    int(line[4])
                )]
            else:
                by_date_dict[key].append((
                    line[6],
                    int(line[5]),
                    int(line[4])
                ))
        except ValueError:
            pass
    return by_date_dict


def create_by_country(lines_from_file):
    by_country_dict = {}
    for line in lines_from_file:
        line = line.split('\t')
        if not line[6] in by_country_dict:
            try:
                by_country_dict[line[6]] = [(
                    int(line[3]),  # rok
                    int(line[2]),  # miesiac
                    int(line[1]),  # dzien
                    int(line[5]),  # zgony
                    int(line[4])  # przypadki
                )]
            except ValueError:
                pass
        else:
            try:
                by_country_dict[line[6]].append((
                    int(line[3]),  # rok
                    int(line[2]),  # miesiac
                    int(line[1]),  # dzien
                    int(line[5]),  # zgony
                    int(line[4])  # przypadki
                ))
            except ValueError:
                pass
    return by_country_dict


lines = open_file(FILEPATH)

all_cases = create_all_cases(lines)
by_country = create_by_country(lines)
by_date = create_by_date(lines)

# ====================== Zadanie 2 ===============================

SEARCHEDDATE = (2020, 11, 25)


# dla all_cases
def for_date_a(year, month, day):
    # uwaga na zmiane kolejnosci w all_cases !!!!!
    # teraz jest:
    # - nazwa       ->  line[0]
    # - rok         ->  line[1]
    # - miesiac     ->  line[2]
    # - dzien       ->  line[3]
    # - zgony       ->  line[4]
    # - przypadki   ->  line[5]

    start = timer()

    sum_for_all = functools.reduce(
        lambda acc, line:
        (acc[0] + line[4], acc[1] + line[5]) if line[1] == year and line[2] == month and line[3] == day
        else (acc[0] + 0, acc[1] + 0),
        all_cases,
        (0, 0)
    )

    end = timer()
    print((end - start) * 1000)

    return sum_for_all


print(for_date_a(SEARCHEDDATE[0], SEARCHEDDATE[1], SEARCHEDDATE[2]))


# dla by_date
def for_date_d(year, month, day):
    start = timer()

    sum_for_all = (0, 0)
    key = (year, month, day)
    if key in by_date:
        for line in by_date[key]:
            sum_for_all = (sum_for_all[0] + line[1], sum_for_all[1] + line[2])

    end = timer()
    print((end - start) * 1000)

    return sum_for_all


print(for_date_d(SEARCHEDDATE[0], SEARCHEDDATE[1], SEARCHEDDATE[2]))


# dla by_country
def for_date_c(year, month, day):
    # kolejnosc w by_country:
    # - rok         ->  line[0]
    # - miesiac     ->  line[1]
    # - dzien       ->  line[2]
    # - zgony       ->  line[3]
    # - przypadki   ->  line[4]
    start = timer()

    sum_for_all = (0, 0)

    for line in by_country.values():
        for number in line:
            if number[0] == year and number[1] == month and number[2] == day:
                sum_for_all = (sum_for_all[0] + number[3], sum_for_all[1] + number[4])

    end = timer()
    print((end - start) * 1000)

    return sum_for_all


print(for_date_c(SEARCHEDDATE[0], SEARCHEDDATE[1], SEARCHEDDATE[2]))
