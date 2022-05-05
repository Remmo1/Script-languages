from unittest import TestCase

from Classes.First_name import First_name
from Errors.NameException import NameException


class TestFirst_name(TestCase):

    def setUp(self):
        First_name.open_file(First_name.FILEPATH)

    def test_name(self):
        f1 = First_name('Jan')
        self.assertEqual(f1.name, 'Jan')

        with self.assertRaises(NameException):
            First_name('Remigiusz')

    def test_is_male(self):
        f1 = First_name('Aleksander')
        self.assertTrue(f1.is_male())

    def test_is_female(self):
        f1 = First_name('Aleksandra')
        self.assertTrue(f1.is_female())

    def test_male_name(self):
        f1 = First_name('Leon')
        self.assertTrue(f1.male_name(f1.get_text()))

    def test_female_name(self):
        f1 = First_name('Emilia')
        self.assertTrue(f1.female_name(f1.get_text()))
