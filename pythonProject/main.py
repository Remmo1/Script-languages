from Operations import take_from_default, compress_file, decompress_file, show_all_files, send_to_archive
from Downlader import download_photo, download_binary


def main_menu():
    print('================= Witam w systemie zarzadzania plikami! =====================')
    print('=================        [1] Pokazanie plikow           =====================')
    print('=================        [2] Pobieranie plikow          =====================')
    print('=================    [3] Automatyczne przenoszenie      =====================')
    print('=================        [4] Kompresja                  =====================')
    print('=================        [5] Dekompresja                =====================')
    print('=================        [6] Archiwizacja               =====================')
    print('=================        [7] Wyjscie                    =====================')
    return input('/Wcisnij odpowiednia cyfre:~$ ')


def showing():
    show_all_files()


def downloading(name, choice):
    if choice == 1:
        download_photo(name + '.jpg')
    elif choice == 2:
        download_binary(name + '.bin')
    else:
        print('Wybierz numer 1 lub 2!')


def automatic_moving():
    take_from_default()


def compressing(name):
    compress_file(name)


def decompressing(name):
    decompress_file(name)


def archiving():
    send_to_archive()


if __name__ == '__main__':
    a = input('podaj cos: ')
    while (input('podaj cos: ') != 0):
        if a == 1:
            print('podales 1')

    print('koniec')