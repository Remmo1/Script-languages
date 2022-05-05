from unittest import TestCase

from Classes.Last_name import Last_name


class TestLast_name(TestCase):

    def test_regex(self):
        l1 = Last_name('Nowak-kOwAlski')
        self.assertEqual(l1.lname, 'Nowak-Kowalski')

        l2 = Last_name('Pisarski')
        self.assertEqual(l2.lname, 'Pisarski')

        l3 = Last_name('wolska')
        self.assertEqual(l3.lname, 'Wolska')

        l4 = Last_name('Abacki-nOwaK-Tomaszewski-Kubacki-wilk')
        self.assertEqual(l4.lname, 'Abacki-Nowak')
