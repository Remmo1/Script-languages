from unittest import TestCase
from First_name import First_name

class TestFirst_name(TestCase):
    
    def test_name(self):
        names = First_name.open_file('C:\\Uczelnia\\Semestr4\\Jezyki Skryptowe\\laby\\lab8JezykiS\\PopulaneImiona')
        f1 = First_name(names, 'Jan')
        self.assertEqual('Jan', f1.name())
    