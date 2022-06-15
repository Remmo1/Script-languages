import os

from constst import PROJECT_FOLDER, IDEAS_FOLDER


class Userfunctions:

    @staticmethod
    def create_folder_for_extension(f_name, ext, folders):
        """
        creates folder for given extension, adds it to programm FOLDERS and creates extension info
        :param f_name:
        :param ext:
        :param folders:
        :return:
        """
        try:
            f_path = PROJECT_FOLDER + '/' + f_name
            os.mkdir(PROJECT_FOLDER + '/' + f_name)
        except OSError:
            pass

        try:
            f = open(PROJECT_FOLDER + '/' + f_name + '/__ex_r__info.abc', 'x')
            if ext[0] != '.':
                ext = '.' + ext

            f.write(ext)

            folders[0][ext] = f_path

        except FileExistsError:
            pass

    @staticmethod
    def create_folder_for_rules(f_name, rule, folders):
        """
        creates folder for given rule, adds it to programm FOLDERS and creates rule info
        :param f_name:
        :param rule:
        :param folders:
        :return:
        """
        try:
            f_path = PROJECT_FOLDER + '/' + f_name
            os.mkdir(PROJECT_FOLDER + '/' + f_name)
        except OSError:
            pass

        try:
            f = open(PROJECT_FOLDER + '/' + f_name + '/__ex_r__info.abc', 'x')

            f.write(rule)

            folders[1][rule] = f_path

        except FileExistsError:
            pass

    @staticmethod
    def send_idea(text):
        """
        saves given text as a file
        :param text:
        :return:
        """
        try:
            f = open(IDEAS_FOLDER + '/' + str(str(text).__hash__() % 3000) + '.txt', 'x')
            f.write(text)
        except FileExistsError:
            pass
