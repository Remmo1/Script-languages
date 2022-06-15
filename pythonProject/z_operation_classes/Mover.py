import os
import shutil

from constst import PHOTO_FOLDER, BINARY_FOLDER, DEFAULT_FOLDER, OTHERS_FOLDER


class Mover:

    @staticmethod
    def move_file_to(file_path, target_directory):
        """
        moves file (given by its path) to the directory
        :param file_path:
        :param target_directory:
        :return:
        """
        try:
            shutil.move(file_path, target_directory)
            return 0
        except shutil.Error:
            print('Taki plik juz istnieje!')
            return -1

    def move_photo(self, file_path):
        """
        moves .jpg file to photos folder
        :param file_path:
        :return:
        """
        self.move_file_to(file_path, PHOTO_FOLDER)

    def move_binary_file(self, file_path):
        """
        moves .bin file to binaries folder
        :param file_path:
        :return:
        """
        self.move_file_to(file_path, BINARY_FOLDER)

    def take_from_default(self):
        """
        Takes all files from the default Downloads folder and puts it into project folder.
        This is baisic version, sorts only .jpg and .bin files
        :return:
        """
        for filename in os.scandir(DEFAULT_FOLDER):
            if filename.is_file() and str(filename.path).endswith('.jpg'):
                self.move_photo(filename.path)
            elif filename.is_file() and str(filename.path).endswith('.bin'):
                self.move_binary_file(filename.path)
            else:
                self.move_file_to(filename.path, OTHERS_FOLDER)

    def take_from_default_n(self, folders):
        """
        Takes all files from the default Downloads folder and puts it into project folder.
        This is advanced version. It sorts by rules and extensions (user can add his ideas).
        :param folders:
        :return:
        """
        for filename in os.scandir(DEFAULT_FOLDER):
            ''' Ważne założenie: reguły mają pierwszeństwo przed rozszerzeniami! '''

            moved = False

            # rules
            for rule in folders[1]:
                rule = str(rule).lower()
                f_n = str(filename.path).lower()
                if rule != 'archive' and rule != 'others':
                    if f_n.__contains__(rule) and not f_n.endswith(rule):
                        self.move_file_to(filename.path, folders[1][rule])
                        moved = True
                        break

            # extensions
            if not moved:
                for ext in folders[0]:
                    if str(filename.path).endswith(ext):
                        self.move_file_to(filename.path, folders[0][ext])
                        moved = True
                        break
                if not moved:
                    self.move_file_to(filename.path, folders[1]['others'])
