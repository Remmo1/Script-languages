from Classes.Controlled_text import Controlled_text
import re


class Last_name(Controlled_text):
    LAST_NAME_PATTERN = re.compile('([a-zA-Z]+)-*((([a-zA-Z])+)*)')

    @staticmethod
    def two_parts_last_name(text):
        matches = Last_name.LAST_NAME_PATTERN.finditer(text)
        first_last_name = ''
        second_last_name = ''

        for m in matches:
            first_last_name = m.group(1)
            second_last_name = m.group(2)
            break

        if second_last_name != '':
            return first_last_name.capitalize() + '-' + second_last_name.capitalize()
        else:
            return first_last_name.capitalize()

    def __init__(self, text):
        super().__init__(self.two_parts_last_name(text))

    @property
    def lname(self):
        return self.get_text()

    @lname.setter
    def lname(self, text):
        self.set_text(self.two_parts_last_name(text))
