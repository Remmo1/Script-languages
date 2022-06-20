class Deleter:

    """
    class responsible for deleting files
    """

    @staticmethod
    def delete_all(folder: str):
        """
        deletes all files in the folder except rule or extension info
        :param folder:
        :return:
        """
        import os
        for file in os.scandir(folder):
            if not str(file.path).endswith('__ex_r__info.abc'): # noqa
                os.remove(file) # noqa
