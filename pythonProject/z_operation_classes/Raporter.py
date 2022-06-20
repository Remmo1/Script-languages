import bz2
import datetime
import os
import shutil
from functools import cmp_to_key

from constst import DEFAULT_FOLDER, PHOTO_FOLDER, BINARY_FOLDER, OTHERS_FOLDER, MAXIMUM_AMOUNT_OF_FILES, \
    ARCHIVE_FOLDER, MAXIMUM_FILE_SIZE, PROJECT_FOLDER, IDEAS_FOLDER
from z_operation_classes.Archivizer import Archivizer


class Raporter:
    def show_in_folder(self, folder: str):
        """
        function that shows files in folder given by a parameter
        :param folder:
        :return:
        """
        for file in os.scandir(folder):
            tokens = str(file.path).split('/')
            print(tokens[len(tokens) - 1])
        print('\n')

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

    def show_amount_of_files(self):
        """
        showing amount of files in each of the basic directory
        :return:
        """
        print(f'Liczba plików w archiwum:\t\t\t {Archivizer.amount_of_files_in(ARCHIVE_FOLDER)}')
        print(f'Liczba plików w folderze pobrane:\t {Archivizer.amount_of_files_in(DEFAULT_FOLDER)}')
        print(f'Liczba plików w folderze binaries:\t {Archivizer.amount_of_files_in(BINARY_FOLDER)}')
        print(f'Liczba plików w folderze zdjęć:\t\t {Archivizer.amount_of_files_in(PHOTO_FOLDER)}')
        print(f'Liczba plików w folderze inne:\t\t {Archivizer.amount_of_files_in(OTHERS_FOLDER)}')

