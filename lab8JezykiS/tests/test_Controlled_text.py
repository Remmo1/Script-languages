from unittest import TestCase
from Classes.Controlled_text import Controlled_text


class TestControlled_text(TestCase):

    def test_check_text(self):
        with self.assertRaises(Exception):
            Controlled_text('text 2')

        with self.assertRaises(Exception):
            Controlled_text('a b c')

        with self.assertRaises(Exception):
            Controlled_text('\t')

        with self.assertRaises(Exception):
            Controlled_text('\n')

    def test_get_text(self):
        c1 = Controlled_text('text123')
        c2 = Controlled_text('123abCdE')

        self.assertNotEqual(c1.get_text(), c2.get_text())
        self.assertEqual(c1.get_text(), 'text123')
        self.assertEqual(c2.get_text(), '123abCdE')

    def test_set_text(self):
        c1 = Controlled_text('text123')
        c2 = Controlled_text('123abCdE')
        c1.set_text('123abCdE')

        self.assertEqual(c1.get_text(), c2.get_text())
        self.assertNotEqual(c1.get_text(), 'text123')
        self.assertEqual(c2.get_text(), '123abCdE')
