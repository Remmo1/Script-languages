import os

import requests
import zipfile

from Operations import move_file_to
from constst import DEFAULT_FOLDER, DOWNLOADED_PHOTOS, DOWNLOADED_BINARIES


def download(url, name):
    response = requests.get(url)
    open(name, 'wb').write(response.content)
    if move_file_to(name, DEFAULT_FOLDER) == -1:
        os.remove(name)


def download_photo(name):
    download(DOWNLOADED_PHOTOS, name)


def download_binary(name):
    download(DOWNLOADED_BINARIES, name)


def unzip_folder(folder_name):
    zf = zipfile.ZipFile(folder_name, 'r')
    zf.extractall('/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/pythonProject/downloaded')
    zf.close()
