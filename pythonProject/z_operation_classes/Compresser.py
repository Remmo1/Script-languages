import bz2
import os
from typing import List

from constst import MAXIMUM_FILE_SIZE


class Compresser:

    """
    class responsible for compressing bigger files
    """

    @staticmethod
    def compress_file(file_path: str) -> (int, List[str]):
        """
        Compresses file given by its path.
        It doesn't delete the old file, only adds compressed version.
        :param file_path:
        :return: (n_f_s, ret) - (new compressed file size, messages that are used in GUI)
        """

        # we're taking file name
        f_n = file_path.split('/')
        f_n = f_n[len(f_n) - 1]
        old_f_n = f_n

        # cutting extension
        act = len(f_n) - 1
        c = f_n[act]
        while c != '.':
            act = act - 1
            c = f_n[act]
            f_n = f_n[0:act]

        # creating new file
        f_n = f_n + '-compressed.bz2'
        new_f_n = str(file_path).replace(old_f_n, f_n)

        # preparing for returning
        ret = []
        if os.path.exists(new_f_n):
            ret.append(f'Plik {old_f_n} już został skompresowany!\n\t\t\t\t\tNazywa się teraz {f_n}')
            return 0, ret

        with open(file_path, mode="rb") as fin, bz2.open(new_f_n, "wb") as fout:
            fout.write(fin.read())

        file_s = file_path.split('/')
        file_s = file_s[len(file_s) - 1]

        n_f_s = os.stat(new_f_n).st_size
        ret.append(f'Plik {file_s}:')
        ret.append(f'Przed kompresją: {os.stat(file_path).st_size:,}')
        ret.append(f'Po kompresji: {n_f_s:,}')

        return n_f_s, ret

    def compress_all_files(self, folder: str) -> List[str]:
        """
        compresses every file in folder given by a parameter
        :param folder:
        :return: ret - messages that are used in GUI
        """
        ret = []
        act_f = folder.split('/')
        act_f = act_f[len(act_f) - 1]
        ret.append(f'Folder {act_f}:')
        was_sth_to_do = False

        for filename in os.scandir(folder):
            act_f_s = os.path.getsize(filename.path) # noqa
            if act_f_s > MAXIMUM_FILE_SIZE:
                msg = self.compress_file(filename.path) # noqa
                ret.append(msg[1])
                was_sth_to_do = True

        if not was_sth_to_do:
            ret.append(['Brak plików do komresji!'])

        return ret

    def compress_all_n(self, folders: str) -> List[str]:
        """
        compresses every file in project (new version that takes care about new rules and extensions)
        :param folders:
        :return: ret - messages that are used in GUI
        """
        ret = []
        for ext_f in folders[0]:
            ret.append(self.compress_all_files(folders[0][ext_f])) # noqa
        for rule_f in folders[1]:
            ret.append(self.compress_all_files(folders[1][rule_f])) # noqa

        ret = [element for sublist in ret for element in sublist]

        return ret
