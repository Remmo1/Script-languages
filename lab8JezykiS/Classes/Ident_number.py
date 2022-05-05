from Classes.Controlled_text import Controlled_text
from Errors.IdFormatError import IdFormatError
from Errors.PrivilageError import PrivilageError


class Ident_number(Controlled_text):
    NUMBERS_IN_USE = []

    def __init__(self, text):
        super().__init__(text)
        if text.isdigit() and len(text) == 9 and text not in self.NUMBERS_IN_USE:
            sumA = 0
            for i in range(0, 7):
                sumA += int(text[i])
            if sumA % 97 != int(text[7] + text[8]):
                raise IdFormatError('Id niepoprawne, suma kontrolna niezgodna z oczekiwaniami: %s', (text[7] + text[8]))
            else:
                self.NUMBERS_IN_USE.append(text)
        else:
            raise IdFormatError('Podany tekst: %s nie spelnia wymagan id, '
                                'tzn. nie ma dziewieciu cyfr lub nie wszystkie jego znaki sa cyframi'
                                'lub takie id juz istnieje' % text)

    def getId(self):
        return str(self.get_text())

    def setId(self, newId):
        raise PrivilageError('Nie wolno zmieniac raz ustawionego ID!')
