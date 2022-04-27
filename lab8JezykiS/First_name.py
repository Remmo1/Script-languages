from Controlled_text import Controlled_text


class First_name(Controlled_text):

    FILEPATH = '/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab8JezykiS/PopularneImiona'

    @staticmethod
    def open_file(filename):
        gender_list = ([], [])
        with open(filename, 'r') as f:
            lines = f.readlines()

            # Wczytywanie imion kobiet
            i = 1
            line = lines[i]
            while line != '\n':
                gender_list[0].append(line[:-1])
                i = i + 1
                line = lines[i]

            # Wczytywanie imion meskich
            i = i + 2
            line = lines[i]
            while i < len(lines):
                gender_list[1].append(line[:-1])
                i = i + 1
                if i == len(lines):
                    break
                line = lines[i]

            return gender_list

    def __init__(self, names, text):
        super().__init__(text)
        self.names = names

    def show_women(self):
        for name in self.names[0]:
            print(name)

    def show_men(self):
        for name in self.names[1]:
            print(name)
