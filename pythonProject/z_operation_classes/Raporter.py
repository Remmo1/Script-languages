import os

from constst import DEFAULT_FOLDER, PHOTO_FOLDER, BINARY_FOLDER, OTHERS_FOLDER, ARCHIVE_FOLDER, PROJECT_FOLDER
from z_operation_classes.Archivizer import Archivizer
from z_operation_classes.Starting import Starter


class Raporter:
    """
    class responsible for creating raports
    """

    @staticmethod
    def show_in_folder(folder: str):
        """
        function that shows files in folder given by a parameter
        :param folder:
        :return:
        """
        for file in os.scandir(folder):
            tokens = str(file.path).split('/')
            print(tokens[len(tokens) - 1])
        print('\n')

    @staticmethod
    def files_in_folder(folder: str) -> [str]:
        """
        function that returns files in folder given by a parameter as a string list
        :param folder:
        :return:
        """
        results = [str]
        for file in os.scandir(folder):
            tokens = str(file.path).split('/')
            results.append(tokens[len(tokens) - 1])
        return results

    def show_all_files(self):
        """
        function that shows all files in the basic folders, console version
        :return:
        """
        print('\n ====== Spis plików ========\n')
        print('Pliki z archiwum:')
        self.show_in_folder(ARCHIVE_FOLDER)

        print('Pliki w folderze pobrane')
        self.show_in_folder(DEFAULT_FOLDER)

        print('Pliki z rozszerzeniem .bin')
        self.show_in_folder(BINARY_FOLDER)

        print('Zdjecia')
        self.show_in_folder(PHOTO_FOLDER)

        print('Inne')
        self.show_in_folder(OTHERS_FOLDER)

    def take_all_files(self):
        folder_files = {str: [str]}

        for f in os.scandir(PROJECT_FOLDER):
            if os.path.isdir(f):
                for fi in os.scandir(f):
                    f_n = Starter.return_file_name(fi.path)
                    if os.path.isfile(fi) and (f_n == '__ex_r__info.abc'):
                        folder_files[Starter.return_file_name(f.path)] = self.files_in_folder(f.path)
                        break

        ret2 = []
        for folder in folder_files:
            ret2.append('Folder: ' + str(folder) + str(':\n'))
            for file in folder_files[folder]:
                line = str(file) + str('\n')
                ret2.append(line)

        return ret2

    @staticmethod
    def show_amount_of_files():
        """
        showing amount of files in each of the basic directory
        :return:
        """
        print(f'Liczba plików w archiwum:\t\t\t {Archivizer.amount_of_files_in(ARCHIVE_FOLDER)}')
        print(f'Liczba plików w folderze pobrane:\t {Archivizer.amount_of_files_in(DEFAULT_FOLDER)}')
        print(f'Liczba plików w folderze binaries:\t {Archivizer.amount_of_files_in(BINARY_FOLDER)}')
        print(f'Liczba plików w folderze zdjęć:\t\t {Archivizer.amount_of_files_in(PHOTO_FOLDER)}')
        print(f'Liczba plików w folderze inne:\t\t {Archivizer.amount_of_files_in(OTHERS_FOLDER)}')

    @staticmethod
    def amount_of_files_in_all_folders(folders):
        ret = [str]
        for ext_f in folders[0].values():
            ret.append('Liczba plików w folderze %s: %s' %
                       (Starter.return_file_name(ext_f), Archivizer.amount_of_files_in(ext_f)))
        for rule_f in folders[1].values():
            ret.append('Liczba plików w folderze %s: %s' %
                       (Starter.return_file_name(rule_f), Archivizer.amount_of_files_in(rule_f)))

        return ret

    def new_csv_file_arrived(self, file):
        pass