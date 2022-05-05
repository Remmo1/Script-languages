from unittest import TestCase

from Classes.Ident_number import Ident_number
from Errors.IdFormatError import IdFormatError
from Errors.PrivilageError import PrivilageError


class TestIdent_number(TestCase):
    def test_id(self):

        # zle dane
        with self.assertRaises(IdFormatError):
            Ident_number('12345sadasd')

        with self.assertRaises(IdFormatError):
            Ident_number('123456')

        with self.assertRaises(IdFormatError):
            Ident_number('1234567891')

        with self.assertRaises(IdFormatError):
            Ident_number('123456789')

        # identycznosc wartosci
        id1 = Ident_number('111111107')
        id2 = Ident_number('222222214')

        self.assertEqual(id1.getId(), '111111107')
        self.assertEqual(id2.getId(), '222222214')

        # brak mozliwosci zmiany
        with self.assertRaises(PrivilageError):
            id1.set_text('333333321')

        # nie mozna dopisac id bedacego juz w bazie
        with self.assertRaises(IdFormatError):
            Ident_number('111111107')
