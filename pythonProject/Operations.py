import bz2
import datetime
import os
import shutil
import smtplib
import sys
import zipfile
from email.mime.text import MIMEText
from functools import cmp_to_key

from constst import DEFAULT_FOLDER, PHOTO_FOLDER, BINARY_FOLDER, OTHERS_FOLDER, MAXIMUM_AMOUNT_OF_FILES, \
    ARCHIVE_FOLDER, MAXIMUM_FILE_SIZE, PROJECT_FOLDER


# spis plików

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


# Przerzucanie plików między folderami

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


# metoda biorąca pliki z folderu domyślnego i wrzucająca je do projektu

# wersja podstawowa
def take_from_default():
    for filename in os.scandir(DEFAULT_FOLDER):
        if filename.is_file() and str(filename.path).endswith('.jpg'):
            move_photo(filename.path)
        elif filename.is_file() and str(filename.path).endswith('.bin'):
            move_binary_file(filename.path)
        else:
            move_file_to(filename.path, OTHERS_FOLDER)


# wersja bardziej uniwersalna
def take_from_default_n(folders):
    for filename in os.scandir(DEFAULT_FOLDER):
        ''' Ważne założenie: reguły mają pierwszeństwo przed rozszerzeniami! '''

        moved = False

        # reguły
        for rule in folders[1]:
            if str(rule) != 'archive' and str(rule) != 'others':
                if str(filename.path).__contains__(rule) and not str(filename.path).endswith(rule):
                    move_file_to(filename.path, folders[1][rule])
                    moved = True
                    break

        # rozszerzenia
        if not moved:
            for ext in folders[0]:
                if str(filename.path).endswith(ext):
                    move_file_to(filename.path, folders[0][ext])
                    moved = True
                    break
            if not moved:
                move_file_to(filename.path, folders[1]['others'])


# kompresja plików

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


def compress_all_n(folders):
    for ext_f in folders[0]:
        compress_all_files(folders[0][ext_f])
    for rule_f in folders[1]:
        compress_all_files(folders[1][rule_f])


# archiwizowanie plików

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


def send_to_archive_n(folders):
    for ext_f in folders[0]:
        check_in_folder(folders[0][ext_f])
    for rule_f in folders[1]:
        check_in_folder(folders[1][rule_f])


# rozpakowanie folderu

def unzip_folder(folder_name):
    zf = zipfile.ZipFile(folder_name, 'r')
    zf.extractall('/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/pythonProject/downloaded')
    zf.close()


# usuwanie z folderu

def delete_all(folder):
    for file in os.scandir(folder):
        if not str(file.path).endswith('__ex_r__info.abc'):
            os.remove(file)


# funkcje użytkownika

def return_file_name(path: str) -> str:
    f_n = path.split('/')
    return f_n[len(f_n) - 1]


def search_for_folders(folder):
    folders_rules = {}
    folders_ext = {}

    for f in os.scandir(folder):
        if os.path.isdir(f):
            for fi in os.scandir(f):
                f_n = return_file_name(fi.path)
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


def create_folder_for_extension(f_name, ext, folders):
    try:
        f_path = PROJECT_FOLDER + '/' + f_name
        os.mkdir(PROJECT_FOLDER + '/' + f_name)
    except OSError:
        pass

    try:
        f = open(PROJECT_FOLDER + '/' + f_name + '/__ex_r__info.abc', 'x')
        if ext[0] != '.':
            ext = '.' + ext

        f.write(ext)

        folders[0][ext] = f_path

    except FileExistsError:
        pass


def create_folder_for_rules(f_name, rule, folders):
    try:
        f_path = PROJECT_FOLDER + '/' + f_name
        os.mkdir(PROJECT_FOLDER + '/' + f_name)
    except OSError:
        pass

    try:
        f = open(PROJECT_FOLDER + '/' + f_name + '/__ex_r__info.abc', 'x')

        f.write(rule)

        folders[1][rule] = f_path

    except FileExistsError:
        pass


# wyślij email do twórcy

def send_mail(text):

    sender = 'from@fromdomain.com'
    receivers = ['to@todomain.com']

    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """

    try:
        smtpObj = smtplib.SMTP('onet.pl', 587)
        smtpObj.sendmail(sender, receivers, message)
        print
        "Successfully sent email"
    except smtplib.SMTPException:
        print
        "Error: unable to send email"
