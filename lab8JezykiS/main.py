class Controlled_text:
    def __init__(self):
        self.text = 'empty'

    @property
    def text(self):
        return self.text

    @text.setter
    def text(self, new_text):
        if new_text == 'empty':
            raise TypeError('Podana wartosc nie jest prawidlowa!')
        self.text = new_text

    def __str__(self):
        return 'Tekst: %s' % self.text


t2 = Controlled_text()
t2.text = 'new'

print(t2.__str__())
