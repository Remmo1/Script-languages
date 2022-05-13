from Classes.Controlled_text import Controlled_text
from Errors.NameException import NameException


class First_name(Controlled_text):
    FILEPATH = '/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab8JezykiS/PopularneImiona'
    GENDER_LIST = ([], [])

    @staticmethod
    def open_file(filename):
        # wczytujemy tylko gdy tego nie zrobilismy wczesniej
        if First_name.GENDER_LIST == ([], []):
            with open(filename, 'r') as f:
                lines = f.readlines()

                # Wczytywanie imion kobiet
                i = 1
                line = lines[i]
                while line != '\n':
                    First_name.GENDER_LIST[0].append(line[:-1])
                    i = i + 1
                    line = lines[i]

                # Wczytywanie imion meskich
                i = i + 2
                line = lines[i]
                while i < len(lines):
                    First_name.GENDER_LIST[1].append(line[:-1])
                    i = i + 1
                    if i == len(lines):
                        break
                    line = lines[i]
        return First_name.GENDER_LIST

    def __init__(self, text):
        super().__init__(text.capitalize())
        if self.get_text() not in First_name.GENDER_LIST[0] and self.get_text() not in First_name.GENDER_LIST[1]:
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
        return name_from_user in First_name.GENDER_LIST[1]

    @staticmethod
    def female_name(name_from_user):
        return name_from_user in First_name.GENDER_LIST[0]

    @staticmethod
    def show_women():
        for name in First_name.GENDER_LIST[0]:
            print(name)

    @staticmethod
    def show_men():
        for name in First_name.GENDER_LIST[1]:
            print(name)
