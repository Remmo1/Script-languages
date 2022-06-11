import tkinter as tk
from tkinter import Tk

import constst
from Downlader import download_photo, download_binary
from Operations import compress_all_n, send_to_archive_n, show_all_files, show_amount_of_files, delete_all, \
    take_from_default_n, search_for_folders, create_folder_for_extension

# główne okno
root = Tk()


# okienka pomocnicze wyświetlające ostrzeżenia i potwierdzenia
def show_warning(msg, window):
    wr_win = tk.Toplevel(window)
    wr_win.title('Błąd')
    wr_win.geometry('450x80')

    ret_m = tk.Label(
        master=wr_win,
        text=msg,
        fg="red",
        width=300,
        height=2
    )
    ret_m.pack()


def show_akn(msg, window):
    ak_win = tk.Toplevel(window)
    ak_win.title('Ukończono!')
    ak_win.geometry('450x80')

    ret_m = tk.Label(
        master=ak_win,
        text=msg,
        fg="green",
        width=300,
        height=2
    )
    ret_m.pack()

    des_bt = tk.Button(
        ak_win,
        text="OK!",
        width=20,
        height=5,
        bg="green",
        fg="black",
        command=ak_win.destroy
    )
    des_bt.pack()


# sekcja pobierania plikow
def downloading(name, choice_d, d_win):
    if name == '':
        show_warning('Wpisz w szarym polu jak chcesz nazwać plik!!!', d_win)
    elif choice_d == 0:
        show_warning('Wybierz jaki to ma być plik, tzn. zaznacz zdjęcie lub plik bin!', d_win)
    else:
        if choice_d == 1:
            download_photo(name + '.jpg')
            show_akn('Zdjęcie pobrano pomyślnie, znajdziesz je w folderze Pobrane', d_win)
        elif choice_d == 2:
            download_binary(name + '.bin')
            show_akn('Plik bin pobrano pomyślnie, znajdziesz go w folderze Pobrane', d_win)


def open_download_choice():
    download_window = tk.Toplevel(root)
    download_window.title('Pobieranie losowych plików')
    download_window.geometry('500x500')

    choose_file_extension = tk.Label(
        master=download_window,
        text="Wybierz plik:",
        fg="white",
        bg="black",
        width=400,
        height=10
    )
    choose_file_extension.pack()

    var = tk.IntVar()
    R1 = tk.Radiobutton(download_window, text="Zdjęcie", variable=var, value=1)
    R1.pack()

    R2 = tk.Radiobutton(download_window, text="Plik bin", variable=var, value=2)
    R2.pack()

    enter_file_name = tk.Label(
        download_window,
        text="Podaj nazwę pliku:",
        width=40,
        height=3
    )
    enter_file_name.pack()

    file_name = tk.Entry(download_window, fg="white", bg="grey", width=50)
    file_name.pack()

    lets_download = tk.Button(
        download_window,
        text="Pobierz plik!",
        width=20,
        height=5,
        bg="orange",
        fg="yellow",
        command=lambda: downloading(file_name.get(), var.get(), download_window)
    )
    lets_download.pack()


# sekcja przenoszenia
def move_files_from_default(win, folders):
    take_from_default_n(folders)
    show_akn('Pliki zostały przeniesione do odpowiednich folderów.', win)


def open_mover(folders):
    mover_win = tk.Toplevel(root)
    mover_win.title('Przenoszenie')
    mover_win.geometry('900x300')

    mover_info = tk.Label(
        master=mover_win,
        text="Uwaga! Wszystkie pliki z folderu Pobrane zostaną przeniesione do projektu i posegregowane "
             "według rozszerzeń, kontynuuować?",
        fg="white",
        bg="black",
        width=800,
        height=10
    )
    mover_info.pack()

    mover_ok_bt = tk.Button(
        master=mover_win,
        text="Tak, przenieś pliki!",
        width=800,
        height=10,
        bg="green",
        fg="white",
        command=lambda: move_files_from_default(mover_win, folders)
    )
    mover_ok_bt.pack()


# sekcja kompresji
def compressing(win, folders):
    compress_all_n(folders)
    show_akn('Pliki zostały pomyślnie skopresowane.', win)


def open_compresser(folders):
    compresser_win = tk.Toplevel(root)
    compresser_win.title('Kompresja')
    compresser_win.geometry('900x300')

    compresser_info = tk.Label(
        master=compresser_win,
        text="Uwaga! Wszystkie pliki w projekcie o rozmiarze powyżej 3MB zostaną skompresowane, kontynuuować?",
        fg="white",
        bg="black",
        width=800,
        height=10
    )
    compresser_info.pack()

    compresser_ok_bt = tk.Button(
        master=compresser_win,
        text="Tak, skompresuj pliki!",
        width=800,
        height=10,
        bg="green",
        fg="white",
        command=lambda: compressing(compresser_win, folders)
    )
    compresser_ok_bt.pack()


# sekcja archiwizacji
def archiving(win, folders):
    send_to_archive_n(folders)
    show_akn('Pliki zostały pomyślnie przeniesione do archiwum.', win)


def open_archivizer(folders):
    archiver_win = tk.Toplevel(root)
    archiver_win.title('Archiwizacja')
    archiver_win.geometry('900x300')

    archiver_info = tk.Label(
        master=archiver_win,
        text="Uwaga! Najstarsze pliki zostaną przeniesione do archiwum, kontynuuować?",
        fg="white",
        bg="black",
        width=800,
        height=10
    )
    archiver_info.pack()

    archiver_ok_bt = tk.Button(
        master=archiver_win,
        text="Tak, archiwizuj pliki!",
        width=800,
        height=10,
        bg="green",
        fg="white",
        command=lambda: archiving(archiver_win, folders)
    )
    archiver_ok_bt.pack()


# sekcja usuwania

def deleting(win):
    delete_all(constst.ARCHIVE_FOLDER)
    show_akn('Pliki z archiwum zostały trwale usunięte', win)


def open_deleter():
    deleter_win = tk.Toplevel(root)
    deleter_win.title('Usuwanie')
    deleter_win.geometry('900x300')

    deleter_info = tk.Label(
        master=deleter_win,
        text="Uwaga! Wszystkie pliki z archiwum zostaną trwale usunięte, kontynuuować?",
        fg="white",
        bg="black",
        width=800,
        height=10
    )
    deleter_info.pack()

    deleter_ok_bt = tk.Button(
        master=deleter_win,
        text="Tak, usuń pliki!",
        width=800,
        height=10,
        bg="red",
        fg="white",
        command=lambda: deleting(deleter_win)
    )
    deleter_ok_bt.pack()


# sekcja własnych funkcji

def open_functions_chooser(folders):
    function_win = tk.Toplevel(root)
    function_win.title('Kreator funkcji')
    function_win.geometry('600x400')

    fr = tk.Frame(function_win)
    fr.pack()

    bt1 = tk.Button(fr, text='Folder na rozszerzenia', width=20, height=20, bg='cyan', fg='black',
                    command=lambda: open_ext_folder_creator(folders))
    bt1.pack(side=tk.LEFT, padx=5, pady=20)
    bt2 = tk.Button(fr, text='Folder na nazwy', width=20, height=20, bg='purple', fg='black',
                    command=lambda: open_name_folder_creator(folders, function_win))
    bt2.pack(side=tk.LEFT, padx=5, pady=20)
    bt3 = tk.Button(fr, text='Własny pomysł', width=20, height=20, bg='yellow', fg='black',
                    command=lambda: open_user_ideas_creator(folders, function_win))
    bt3.pack(side=tk.LEFT, padx=5, pady=20)


def open_ext_folder_creator(folders):
    ext_f_win = tk.Toplevel(root)
    ext_f_win.title('Kreator folderu rozszerzeń')
    ext_f_win.geometry('600x400')

    l1 = tk.Label(ext_f_win, text='Podaj nazwę folderu: ')
    l1.pack(padx=5, pady=20)
    e1 = tk.Entry(ext_f_win)
    e1.pack(padx=5, pady=20)

    l2 = tk.Label(ext_f_win, text='Podaj nazwę rozszerzenia (nie musisz podawać kropki na początku):')
    l2.pack(padx=5, pady=20)
    e2 = tk.Entry(ext_f_win)
    e2.pack(padx=5, pady=20)

    confirm_bt = tk.Button(ext_f_win, text='Tak, stwórz folder na podane rozszerzenia!',
                           width=35, height=5, bg='green', fg='white',
                           command=lambda: create_folder_for_ext(e1.get(), folders, e2.get(), ext_f_win))
    confirm_bt.pack(padx=5, pady=20)


def create_folder_for_ext(f_n, folders, ext, win):
    if f_n == '':
        show_warning('Podaj nazwę folderu!', win)
    elif ext == '':
        show_warning('Podaj nazwę rozszerzenia!', win)
    else:
        create_folder_for_extension(f_n, ext, folders)
        show_akn('Folder o nazwie %s przechowujący rozszerzenia %s został utworzony!' % (f_n, ext), win)


def open_name_folder_creator(folders, win):
    pass


def open_user_ideas_creator(folders, win):
    pass


# ============================================= main ======================================

if __name__ == '__main__':
    root.title('System zarządzania plikami')
    root.geometry("900x900")
    root.config(width=1000)
    root.config(height=1000)
    root.eval('tk::PlaceWindow . center')
    FOLDERS = search_for_folders(constst.PROJECT_FOLDER)

    download_button = tk.Button(
        text="Pobierz plik",
        width=80,
        height=5,
        bg="blue",
        fg="yellow",
        command=open_download_choice
    )
    download_button.pack()

    mover_button = tk.Button(
        text="Automatyczne Przenoszenie",
        width=80,
        height=5,
        bg="orange",
        fg="black",
        command=lambda: open_mover(FOLDERS)
    )
    mover_button.pack()

    compress_button = tk.Button(
        text="Automatyczna kompresja",
        width=80,
        height=5,
        bg="cyan",
        fg="black",
        command=lambda: open_compresser(FOLDERS)
    )
    compress_button.pack()

    archive_button = tk.Button(
        text="Automatyczna archiwizacja",
        width=80,
        height=5,
        bg="green",
        fg="white",
        command=lambda: open_archivizer(FOLDERS)
    )
    archive_button.pack()

    delete_button = tk.Button(
        text="Automatyczne usuwanie",
        width=80,
        height=5,
        bg="purple",
        fg="white",
        command=open_deleter
    )
    delete_button.pack()

    user_function_button = tk.Button(
        text="Stwórz własne funkcje",
        width=80,
        height=5,
        bg="brown",
        fg="black",
        command=lambda: open_functions_chooser(FOLDERS)
    )
    user_function_button.pack()

    raports_label = tk.Label(
        text="Generuj raport:",
        fg="white",
        bg="black",
        width=800,
        height=10
    )
    raports_label.pack()

    raports_choice = tk.Frame(master=root)
    raports_choice.pack()

    r1 = tk.Button(
        master=raports_choice,
        text='Ogólny',
        width=25,
        height=5,
        bg="yellow",
        fg="blue",
        command=show_all_files
    )

    r2 = tk.Button(
        master=raports_choice,
        text='Ilość plików',
        width=25,
        height=5,
        bg="green",
        fg="white",
        command=show_amount_of_files
    )

    r1.pack(padx=5, pady=10, side=tk.LEFT)
    r2.pack(padx=5, pady=10, side=tk.LEFT)

    root.mainloop()
