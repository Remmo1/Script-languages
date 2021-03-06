import datetime
import os
from functools import cmp_to_key
from typing import List

from constst import MAXIMUM_AMOUNT_OF_FILES, ARCHIVE_FOLDER
from z_operation_classes.Mover import Mover


class Archivizer:
    """
    class responsible for archiving files
    """

    @staticmethod
    def amount_of_files_in(folder: str) -> int:
        """
        it returns amount of files in the folder given by a parameter
        :param folder:
        :return: i: amount of files in folder
        """
        i: int = 0
        for f in os.scandir(folder):
            if not str(f).__contains__('__ex_r__info.abc'):
                i = i + 1
        return i

    @staticmethod
    def comparator(a, b) -> int:
        """
        help function, that compares dataTime objects
        :param a:
        :param b:
        :return:
        """
        if a[0].seconds == b[0].seconds:
            return a[0].microseconds - b[0].microseconds
        else:
            return a[0].seconds - b[0].seconds

    def check_in_folder(self, folder: str) -> List[str]:
        """
        moves files to archive, when in the folder given by a parameter there are too many files
        :param folder:
        :return: ret - messages that are used in GUI
        """
        folder_name = folder.split('/')
        folder_name = folder_name[len(folder_name) - 1]
        ret = []

        if self.amount_of_files_in(folder) > MAXIMUM_AMOUNT_OF_FILES:
            taken_files = []
            today = datetime.datetime.today()
            for filename in os.scandir(folder):
                modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(filename.path))  # noqa
                duration = today - modified_date
                taken_files.append((duration, filename.path))  # noqa

            taken_files = sorted(taken_files, key=cmp_to_key(self.comparator))
            i = len(taken_files)

            ret = ['Status plikow w folderze %s' % folder_name]

            for f in taken_files:
                f_n = f[1].split('/')
                f_n = f_n[len(f_n) - 1]
                ret.append(f'Czas ??ycia pliku {f_n}: {f[0].seconds} [s] i {f[0].microseconds} [ms]')

            while i > MAXIMUM_AMOUNT_OF_FILES:
                Mover.move_file_to(taken_files[i - 1][1], ARCHIVE_FOLDER)
                i = i - 1
        else:
            ret.append('Brak plikow do archiwizacji / usuniecia w folderze %s' % folder_name)
        return ret

    def send_to_archive_n(self, folders: str) -> List[str]:
        """
        moves files to archive when neccessary for the whole project
        :param folders:
        :return: ret - messages that are used in GUI
        """
        ret = []
        for ext_f in folders[0]:
            ret.append(self.check_in_folder(folders[0][ext_f])) # noqa
        for rule_f in folders[1]:
            ret.append(self.check_in_folder(folders[1][rule_f])) # noqa

        ret = [element for sublist in ret for element in sublist]

        return ret
