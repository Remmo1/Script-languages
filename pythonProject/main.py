from Operations import take_from_default, compress_file, decompress_file, show_all_files, send_to_archive
from Downlader import download_photo, download_binary


# ======================================== MENU GLOWNE =====================================
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


# ======================================== MENU Pobierania =====================================
def download_menu():
    print('=================     [1] Pobierz losowe zdjecie        =====================')
    print('=================    [2] Pobierz losowy plik .bin       =====================')
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
    user_choice = int(main_menu())

    while True:
        if user_choice == 7:
            break

        elif user_choice == 1:
            show_all_files()

        elif user_choice == 2:
            p_o_b = int(download_menu())
            fn = input('/Podaj nazwe pliku (nie dopisuj rozszerzenia na koncu):~$ ')
            downloading(fn, p_o_b)
            print('Twoj plik zostal pobrany pomyslnie!!!')

        elif user_choice == 3:
            take_from_default()
            print('Wszystkie pliki trafily na swoje miejsce!\nZnajdziesz je tutaj:')
            print('/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/pythonProject')

        elif user_choice == 4:
            pass

        elif user_choice == 5:
            pass

        elif user_choice == 6:
            send_to_archive()

        user_choice = int(main_menu())

    print('Wspolpraca z Toba to byla czysta przyjemnosc!')
