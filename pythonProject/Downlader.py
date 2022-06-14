import os

import requests

from Operations import move_file_to
from constst import DEFAULT_FOLDER, DOWNLOADED_PHOTOS, DOWNLOADED_BINARIES


def download(url, name):
    """
    downloads something from given url and saves it as given name in Downloads folder
    :param url:
    :param name:
    :return:
    """
    response = requests.get(url)
    open(name, 'wb').write(response.content)
    if move_file_to(name, DEFAULT_FOLDER) == -1:
        os.remove(name)


def download_photo(name):
    """
    downloads random .jpg file and saves it as given name in Downloads folder
    :param name:
    :return:
    """
    download(DOWNLOADED_PHOTOS, name)


def download_binary(name):
    """
    downloads random .bin file and saves it as given name in Downloads folder
    :param name:
    :return:
    """
    download(DOWNLOADED_BINARIES, name)
