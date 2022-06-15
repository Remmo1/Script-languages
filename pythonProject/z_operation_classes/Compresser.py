import bz2
import os

from constst import MAXIMUM_FILE_SIZE


class Compresser:
    @staticmethod
    def compress_file(file_path):
        """
        Compresses file given by its path.
        It doesn't delete the old file, only adds compressed version.
        :param file_path:
        :return:
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

        if os.path.exists(new_f_n):
            print(f'\tPlik {old_f_n} już został skompresowany! Nazywa się teraz {f_n}')
            return

        with open(file_path, mode="rb") as fin, bz2.open(new_f_n, "wb") as fout:
            fout.write(fin.read())

        file_s = file_path.split('/')
        file_s = file_s[len(file_s) - 1]

        print(f'\tPlik {file_s}:')
        print(f'\tPrzed kompresją: {os.stat(file_path).st_size:,}')
        print(f'\tPo kompresji: {os.stat(new_f_n).st_size:,}')

    def compress_all_files(self, folder):
        """
        compresses every file in folder given by a parameter
        :param folder:
        :return:
        """
        act_f = folder.split('/')
        act_f = act_f[len(act_f) - 1]
        print(f'Folder {act_f}')
        for filename in os.scandir(folder):
            act_f_s = os.path.getsize(filename.path)
            if act_f_s > MAXIMUM_FILE_SIZE:
                self.compress_file(filename.path)

    def compress_all_n(self, folders):
        """
        compresses every file in project (new version that takes care about new rules and extensions)
        :param folders:
        :return:
        """
        for ext_f in folders[0]:
            self.compress_all_files(folders[0][ext_f])
        for rule_f in folders[1]:
            self.compress_all_files(folders[1][rule_f])
