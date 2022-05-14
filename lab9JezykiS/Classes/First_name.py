from Classes.Controlled_text import Controlled_text


class First_name(Controlled_text):

    def __init__(self, text):
        super().__init__(text.capitalize())

    @property
    def name(self):
        return self.get_text()
