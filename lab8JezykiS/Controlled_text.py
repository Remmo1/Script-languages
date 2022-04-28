import functools


class Controlled_text:

    # metody sprawdzajace

    @staticmethod
    def check_text(text):
        if str(text).isprintable() and text != ' ':
            try:
                return functools.reduce(lambda acc, x: (acc and False) if x.isspace() else (acc and True), text)
            except TypeError:
                raise Exception('Podane niepoprawne dane!')

    def throw_error_if_text_is_wrong(self, text):
        if not self.check_text(text):
            raise Exception('Podane niepoprawne dane!')

    # konstruktor

    def __init__(self, text):
        self.throw_error_if_text_is_wrong(text)
        self.text = text

    # gettery i settery

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.throw_error_if_text_is_wrong(text)
        self.text = text

    # operatory

    def __lt__(self, other):
        return self.text < other.text

    def __gt__(self, other):
        return self.text > other.text

    def __eq__(self, other):
        return self.text == other.text

    def __le__(self, other):
        return self.text <= other.text

    def __ge__(self, other):
        return self.text >= other.text

    def __ne__(self, other):
        return not self.__eq__(other)
