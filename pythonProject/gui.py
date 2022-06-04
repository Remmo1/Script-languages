import tkinter as tk
from tkinter import Tk

import Operations
from Downlader import download_photo, download_binary
from Operations import compress_all

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
def move_files_from_default(win):
    Operations.take_from_default()
    show_akn('Pliki zostały przeniesione do odpowiednich folderów.', win)


def open_mover():
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
        command=lambda: move_files_from_default(mover_win)
    )
    mover_ok_bt.pack()


# sekcja kompresji
def compressing(win):
    compress_all()
    show_akn('Pliki zostały pomyślnie skopresowane.', win)


def open_compresser():
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
        command=lambda: compressing(compresser_win)
    )
    compresser_ok_bt.pack()


# ============================================= main ======================================

if __name__ == '__main__':
    root.title('System zarządzania plikami')
    root.geometry("800x800")
    root.config(width=1000)

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
        command=open_mover
    )
    mover_button.pack()

    compress_button = tk.Button(
        text="Automatyczna kompresja",
        width=80,
        height=5,
        bg="grey",
        fg="white",
        command=open_compresser
    )
    compress_button.pack()

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
    )

    r2 = tk.Button(
        master=raports_choice,
        text='Ilość plików',
        width=25,
        height=5,
        bg="green",
        fg="blue",
    )

    r1.pack(padx=5, pady=10, side=tk.LEFT)
    r2.pack(padx=5, pady=10, side=tk.LEFT)

    root.mainloop()
