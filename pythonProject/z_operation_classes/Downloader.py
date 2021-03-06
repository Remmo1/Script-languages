import os

import requests

from constst import DEFAULT_FOLDER, DOWNLOADED_PHOTOS, DOWNLOADED_BINARIES
from z_operation_classes.Mover import Mover


class Downloader:

    """
    class responsible for downloading random files from the internet
    """

    @staticmethod
    def download(url: str, name: str) -> type(None):
        """
        downloads something from given url and saves it as given name in Downloads folder
        :param url:
        :param name:
        :return:
        """
        response = requests.get(url)
        open(name, 'wb').write(response.content)
        if Mover.move_file_to(name, DEFAULT_FOLDER) == -1:
            os.remove(name)

    def download_photo(self, name: str) -> type(None):
        """
        downloads random .jpg file and saves it as given name in Downloads folder
        :param name:
        :return:
        """
        self.download(DOWNLOADED_PHOTOS, name)

    def download_binary(self, name: str) -> type(None):
        """
        downloads random .bin file and saves it as given name in Downloads folder
        :param name:
        :return:
        """
        self.download(DOWNLOADED_BINARIES, name)
