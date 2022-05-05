from unittest import TestCase

from Classes.Ident_number import Ident_number
from Errors.IdFormatError import IdFormatError


class TestIdent_number(TestCase):
    def test_generate_id(self):

        with self.assertRaises(IdFormatError):
            Ident_number('123456789')

        id1 = Ident_number('111111107')
        id2 = Ident_number('222222214')

        self.assertEqual(id1, '111111107')
        self.assertEqual(id2, '222222214')

