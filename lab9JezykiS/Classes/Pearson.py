from Classes.First_name import First_name
from Classes.Ident_number import Ident_number
from Classes.Last_name import Last_name
from Errors.NameException import NameException


class Pearson:

    @staticmethod
    def split_by(data, token):
        return str(data).split(token)

    def __init__(self, data):
        ok_data = []

        if str(data).__contains__(' '):
            ok_data = Pearson.split_by(data, ' ')
        elif data.__contains__(';'):
            ok_data = Pearson.split_by(data, ';')
        elif data.__contains__('/'):
            ok_data = Pearson.split_by(data, '/')
        else:
            raise NameException('Podany ciag: %s nie jest poprawny!' % data)

        First_name.open_file(First_name.FILEPATH)

        self.id = Ident_number(ok_data[0])
        self.first_name = First_name(ok_data[1])
        self.last_name = Last_name(ok_data[2])

    def __str__(self):
        return self.id.getId() + ' ' + self.first_name.name + ' ' + self.last_name.lname
