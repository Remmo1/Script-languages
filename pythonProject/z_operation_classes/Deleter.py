class Deleter:
    @staticmethod
    def delete_all(folder):
        """
        deletes all files in the folder except rule or extension info
        :param folder:
        :return:
        """
        import os
        for file in os.scandir(folder):
            if not str(file.path).endswith('__ex_r__info.abc'):
                os.remove(file)
