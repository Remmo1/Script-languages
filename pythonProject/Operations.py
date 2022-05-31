import shutil
import os
import sys
import zlib
import datetime
from functools import cmp_to_key

from constst import DEFAULT_FOLDER, PHOTO_FOLDER, BINARY_FOLDER, OTHERS_FOLDER, MAXIMUM_AMOUNT_OF_FILES, ARCHIVE_FOLDER


# spis plikow
def show_in_folder(folder):
    for file in os.scandir(folder):
        print(file.path)
    print('\n')


def show_all_files():
    print('Pliki z archiwum:')
    show_in_folder(ARCHIVE_FOLDER)

    print('Pliki w folderze pobrane')
    show_in_folder(DEFAULT_FOLDER)

    print('Pliki z rozszerzeniem .bin')
    show_in_folder(BINARY_FOLDER)

    print('Zdjecia')
    show_in_folder(PHOTO_FOLDER)

    print('Inne')
    show_in_folder(OTHERS_FOLDER)


# Przerzucanie plikow miedzy folderami

def move_file_to(file_path, target_directory):
    try:
        shutil.move(file_path, target_directory)
        return 0
    except shutil.Error:
        print('Taki plik juz istnieje!')
        return -1


def move_photo(file_path):
    move_file_to(file_path, PHOTO_FOLDER)


def move_binary_file(file_path):
    move_file_to(file_path, BINARY_FOLDER)


# metoda bioraca pliki z folderu domyslnego i wrzucajaca je do projektu

def take_from_default():
    for filename in os.scandir(DEFAULT_FOLDER):
        if filename.is_file() and str(filename.path).endswith('.jpg'):
            move_photo(filename.path)
        elif filename.is_file() and str(filename.path).endswith('.bin'):
            move_binary_file(filename.path)
        else:
            move_file_to(filename.path, OTHERS_FOLDER)


# kompresja plikow

def compress_file(file_path):
    with open(file_path, mode='rb') as fin, open(file_path, mode='wb') as fout:
        data = fin.read()
        compressed = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
        print('Original size: %s' % sys.getsizeof(data))
        print('Copressed size: %s' % sys.getsizeof(compressed))

        fout.write(compressed)


# dekompresja plikow

def decompress_file(filename):
    with open(filename, mode="rb") as fin, open(filename, mode='wb') as fout:
        data = fin.read()
        compressed_data = zlib.decompress(data)
        print(f"Compressed size: {sys.getsizeof(data)}")
        print(f"Decompressed size: {sys.getsizeof(compressed_data)}")

        fout.write(compressed_data)


# archiwizowanie plikow

def amount_of_files_in(folder):
    i = 0
    for _ in os.scandir(folder):
        i = i + 1
    return i


def comparator(a, b):
    if a[0].seconds == b[0].seconds:
        return a[0].microseconds - b[0].microseconds
    else:
        return a[0].seconds - b[0].seconds


def check_in_folder(folder):
    if amount_of_files_in(folder) > MAXIMUM_AMOUNT_OF_FILES:
        taken_files = []
        today = datetime.datetime.today()
        for filename in os.scandir(folder):
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(filename.path))
            duration = today - modified_date
            taken_files.append((duration, filename.path))

        taken_files = sorted(taken_files, key=cmp_to_key(comparator))
        i = len(taken_files)

        while i > MAXIMUM_AMOUNT_OF_FILES:
            move_file_to(taken_files[i - 1][1], ARCHIVE_FOLDER)
            i = i - 1
    else:
        print('Brak plikow do archiwizacji / usuniecia')


def send_to_archive():
    take_from_default()
    check_in_folder(BINARY_FOLDER)
    check_in_folder(PHOTO_FOLDER)
    check_in_folder(OTHERS_FOLDER)
