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
