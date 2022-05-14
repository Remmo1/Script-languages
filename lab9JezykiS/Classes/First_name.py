from Classes.Controlled_text import Controlled_text
from Errors.NameException import NameException


class First_name(Controlled_text):

    def __init__(self, text):
        super().__init__(text.capitalize())

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
