import bz2
import datetime
import os
import shutil
from functools import cmp_to_key

from constst import DEFAULT_FOLDER, PHOTO_FOLDER, BINARY_FOLDER, OTHERS_FOLDER, MAXIMUM_AMOUNT_OF_FILES, \
    ARCHIVE_FOLDER, MAXIMUM_FILE_SIZE, PROJECT_FOLDER, IDEAS_FOLDER


def show_in_folder(folder: str):
    """
    function that shows files in folder given by a parameter
    :param folder:
    :return:
    """
    for file in os.scandir(folder):
        tokens = str(file.path).split('/')
        print(tokens[len(tokens) - 1])
    print('\n')


def show_all_files():
    """
    function that shows all files in the basic folders, console version
    :return:
    """
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


def show_amount_of_files():
    """
    showing amount of files in each of the basic directory
    :return:
    """
    print(f'Liczba plików w archiwum:\t\t\t {amount_of_files_in(ARCHIVE_FOLDER)}')
    print(f'Liczba plików w folderze pobrane:\t {amount_of_files_in(DEFAULT_FOLDER)}')
    print(f'Liczba plików w folderze binaries:\t {amount_of_files_in(BINARY_FOLDER)}')
    print(f'Liczba plików w folderze zdjęć:\t\t {amount_of_files_in(PHOTO_FOLDER)}')
    print(f'Liczba plików w folderze inne:\t\t {amount_of_files_in(OTHERS_FOLDER)}')


def move_file_to(file_path, target_directory):
    """
    moves file (given by its path) to the directory
    :param file_path:
    :param target_directory:
    :return:
    """
    try:
        shutil.move(file_path, target_directory)
        return 0
    except shutil.Error:
        print('Taki plik juz istnieje!')
        return -1


def move_photo(file_path):
    """
    moves .jpg file to photos folder
    :param file_path:
    :return:
    """
    move_file_to(file_path, PHOTO_FOLDER)


def move_binary_file(file_path):
    """
    moves .bin file to binaries folder
    :param file_path:
    :return:
    """
    move_file_to(file_path, BINARY_FOLDER)


def take_from_default():
    """
    Takes all files from the default Downloads folder and puts it into project folder.
    This is baisic version, sorts only .jpg and .bin files
    :return:
    """
    for filename in os.scandir(DEFAULT_FOLDER):
        if filename.is_file() and str(filename.path).endswith('.jpg'):
            move_photo(filename.path)
        elif filename.is_file() and str(filename.path).endswith('.bin'):
            move_binary_file(filename.path)
        else:
            move_file_to(filename.path, OTHERS_FOLDER)


def take_from_default_n(folders):
    """
    Takes all files from the default Downloads folder and puts it into project folder.
    This is advanced version. It sorts by rules and extensions (user can add his ideas).
    :param folders:
    :return:
    """
    for filename in os.scandir(DEFAULT_FOLDER):
        ''' Ważne założenie: reguły mają pierwszeństwo przed rozszerzeniami! '''

        moved = False

        # rules
        for rule in folders[1]:
            rule = str(rule).lower()
            f_n = str(filename.path).lower()
            if rule != 'archive' and rule != 'others':
                if f_n.__contains__(rule) and not f_n.endswith(rule):
                    move_file_to(filename.path, folders[1][rule])
                    moved = True
                    break

        # extensions
        if not moved:
            for ext in folders[0]:
                if str(filename.path).endswith(ext):
                    move_file_to(filename.path, folders[0][ext])
                    moved = True
                    break
            if not moved:
                move_file_to(filename.path, folders[1]['others'])


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


def compress_all_files(folder):
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
            compress_file(filename.path)


def compress_all_n(folders):
    """
    compresses every file in project (new version that takes care about new rules and extensions)
    :param folders:
    :return:
    """
    for ext_f in folders[0]:
        compress_all_files(folders[0][ext_f])
    for rule_f in folders[1]:
        compress_all_files(folders[1][rule_f])


def amount_of_files_in(folder):
    """
    it returns amount of files in the folder given by a parameter
    :param folder:
    :return:
    """
    i = 0
    for _ in os.scandir(folder):
        i = i + 1
    return i


def comparator(a, b):
    """
    help function, that compares dataTime objects
    :param a:
    :param b:
    :return:
    """
    if a[0].seconds == b[0].seconds:
        return a[0].microseconds - b[0].microseconds
    else:
        return a[0].seconds - b[0].seconds


def check_in_folder(folder):
    """
    moves files to archive, when in the folder given by a parameter there are too many files
    :param folder:
    :return:
    """
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
    """
    moves files to archive when neccessary for the whole project
    :param folders:
    :return:
    """
    for ext_f in folders[0]:
        check_in_folder(folders[0][ext_f])
    for rule_f in folders[1]:
        check_in_folder(folders[1][rule_f])


def delete_all(folder):
    """
    deletes all files in the folder except rule or extension info
    :param folder:
    :return:
    """
    for file in os.scandir(folder):
        if not str(file.path).endswith('__ex_r__info.abc'):
            os.remove(file)


def return_file_name(path: str) -> str:
    """
    it returns the file name by its path
    :param path:
    :return:
    """
    f_n = path.split('/')
    return f_n[len(f_n) - 1]


def search_for_folders(folder):
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
    """
    creates folder for given extension, adds it to programm FOLDERS and creates extension info
    :param f_name:
    :param ext:
    :param folders:
    :return:
    """
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
    """
    creates folder for given rule, adds it to programm FOLDERS and creates rule info
    :param f_name:
    :param rule:
    :param folders:
    :return:
    """
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


def send_idea(text):
    """
    saves given text as a file
    :param text:
    :return:
    """
    try:
        f = open(IDEAS_FOLDER + '/' + str(str(text).__hash__() % 3000) + '.txt', 'x')
        f.write(text)
    except FileExistsError:
        pass
