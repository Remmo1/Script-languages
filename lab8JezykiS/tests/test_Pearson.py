from unittest import TestCase

from Classes.Pearson import Pearson
from Errors.NameException import NameException


class TestPearson(TestCase):
    def test_pearson(self):

        # czytanie danych
        p1 = Pearson('111111107 Aleksander Pisarski')
        p2 = Pearson('222222214;maTEuSz;pIeTrych')
        p3 = Pearson('333333321/maRiA/MarKOWiak')

        with self.assertRaises(NameException):
            Pearson('111111107\tLeon\nPisarski')

        self.assertEqual(p1.__str__(), '111111107 Aleksander Pisarski')
        self.assertEqual(p2.__str__(), '222222214 Mateusz Pietrych')
        self.assertEqual(p3.__str__(), '333333321 Maria Markowiak')
