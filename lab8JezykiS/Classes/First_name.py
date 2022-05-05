from Classes.Controlled_text import Controlled_text
from Errors.NameException import NameException


class First_name(Controlled_text):
    FILEPATH = '/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab8JezykiS/PopularneImiona'
    gender_list = ([], [])

    @staticmethod
    def open_file(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

            # Wczytywanie imion kobiet
            i = 1
            line = lines[i]
            while line != '\n':
                First_name.gender_list[0].append(line[:-1])
                i = i + 1
                line = lines[i]

            # Wczytywanie imion meskich
            i = i + 2
            line = lines[i]
            while i < len(lines):
                First_name.gender_list[1].append(line[:-1])
                i = i + 1
                if i == len(lines):
                    break
                line = lines[i]

            return First_name.gender_list

    def __init__(self, names, text):
        super().__init__(text.capitalize())
        self.gender_list = None
        self.names = names
        if self.get_text() not in First_name.gender_list[0] and self.get_text() not in First_name.gender_list[1]:
            raise NameException('Imie %s nie wystepuje w pliku PopularneImiona i nie mozna go ustawic!' % text)

    @property
    def name(self):
        return self.get_text()

    def is_male(self):
        return self.male_name(self.get_text())

    def is_female(self):
        return self.female_name(self.get_text())

    @staticmethod
    def male_name(name_from_user):
        return name_from_user in First_name.gender_list[1]

    @staticmethod
    def female_name(name_from_user):
        return name_from_user in First_name.gender_list[0]

    def show_women(self):
        for name in self.names[0]:
            print(name)

    def show_men(self):
        for name in self.names[1]:
            print(name)
