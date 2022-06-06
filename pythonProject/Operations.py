import bz2
import datetime
import os
import shutil
import sys
import zipfile
from functools import cmp_to_key

from constst import DEFAULT_FOLDER, PHOTO_FOLDER, BINARY_FOLDER, OTHERS_FOLDER, MAXIMUM_AMOUNT_OF_FILES, \
    ARCHIVE_FOLDER, MAXIMUM_FILE_SIZE


# spis plikow

def show_in_folder(folder):
    for file in os.scandir(folder):
        tokens = str(file.path).split('/')
        print(tokens[len(tokens) - 1])
    print('\n')


def show_all_files():
    print('\n ====== Spis plików ========\n')
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


# ilość plików w folderach

def show_amount_of_files():
    print(f'Liczba plików w archiwum:\t\t\t {amount_of_files_in(ARCHIVE_FOLDER)}')
    print(f'Liczba plików w folderze pobrane:\t {amount_of_files_in(DEFAULT_FOLDER)}')
    print(f'Liczba plików w folderze binaries:\t {amount_of_files_in(BINARY_FOLDER)}')
    print(f'Liczba plików w folderze zdjęć:\t\t {amount_of_files_in(PHOTO_FOLDER)}')
    print(f'Liczba plików w folderze inne:\t\t {amount_of_files_in(OTHERS_FOLDER)}')


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

    # bierzemy nazwę pliku
    f_n = file_path.split('/')
    f_n = f_n[len(f_n) - 1]
    old_f_n = f_n

    # ucinamy rozszerzenie
    act = len(f_n) - 1
    c = f_n[act]
    while c != '.':
        act = act - 1
        c = f_n[act]
        f_n = f_n[0:act]

    # tworzymy nowy plik
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


def decompress_file(file_path):
    with bz2.open(file_path, "rb") as fin:
        data = fin.read()
        print(f"Plik po dekompresji: {sys.getsizeof(data)}")


def compress_all_files(folder):
    act_f = folder.split('/')
    act_f = act_f[len(act_f) - 1]
    print(f'Folder {act_f}')
    for filename in os.scandir(folder):
        act_f_s = os.path.getsize(filename.path)
        if act_f_s > MAXIMUM_FILE_SIZE:
            compress_file(filename.path)


def compress_all():
    compress_all_files(BINARY_FOLDER)
    compress_all_files(PHOTO_FOLDER)
    compress_all_files(OTHERS_FOLDER)


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
    folder_name = folder.split('/')
    folder_name = folder_name[len(folder_name) - 1]

    if amount_of_files_in(folder) > MAXIMUM_AMOUNT_OF_FILES:
        taken_files = []
        today = datetime.datetime.today()
        for filename in os.scandir(folder):
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(filename.path))
            duration = today - modified_date
            taken_files.append((duration, filename.path))

        taken_files = sorted(taken_files, key=cmp_to_key(comparator))
        i = len(taken_files)

        print('Status plikow w folderze %s' % folder_name)
        for f in taken_files:
            f_n = f[1].split('/')
            f_n = f_n[len(f_n) - 1]
            print(f'Czas życia pliku {f_n}: {f[0].seconds} [s] i {f[0].microseconds} [ms]')

        while i > MAXIMUM_AMOUNT_OF_FILES:
            move_file_to(taken_files[i - 1][1], ARCHIVE_FOLDER)
            i = i - 1
    else:
        print('Brak plikow do archiwizacji / usuniecia w folderze %s' % folder_name)


def send_to_archive():
    check_in_folder(BINARY_FOLDER)
    check_in_folder(PHOTO_FOLDER)
    check_in_folder(OTHERS_FOLDER)


# rozpakowanie folderu

def unzip_folder(folder_name):
    zf = zipfile.ZipFile(folder_name, 'r')
    zf.extractall('/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/pythonProject/downloaded')
    zf.close()
