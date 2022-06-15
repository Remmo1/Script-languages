import os


class Starter:
    @staticmethod
    def return_file_name(path: str) -> str:
        """
        it returns the file name by its path
        :param path:
        :return:
        """
        f_n = path.split('/')
        return f_n[len(f_n) - 1]

    def search_for_folders(self, folder):
        """
        Set up function that HAS TO BE DONE BEFORE ANY OPERATION.
        It serach for folders and returns them as a pair (extensions, rules).
        :param folder:
        :return:
        """
        folders_rules = {}
        folders_ext = {}

        for f in os.scandir(folder):
            if os.path.isdir(f):
                for fi in os.scandir(f):
                    f_n = self.return_file_name(fi.path)
                    if os.path.isfile(fi) and (f_n == '__ex_r__info.abc'):
                        ex_r_file = open(fi)
                        data = ex_r_file.read()
                        if data[0] == '.':
                            folders_ext[data] = f.path
                        else:
                            folders_rules[data] = f.path
                        ex_r_file.close()
                        break

        return folders_ext, folders_rules
