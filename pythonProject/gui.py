from random import choice
import tkinter as tk
from tkinter import Tk, Label, Button

from Downlader import download_photo, download_binary

"""
# tkinter podstawy


def click_action(button):
    button.config(text=f'Wow!')


def create_command(func, *args, **kwargs):
    def command():
        return func(*args, **kwargs)

    return command()


clicks = 0


def increase_clicks(button):
    global clicks
    clicks += 1
    button.config(text="Wow! x %s" % clicks)


if __name__ == '__main__':

    root = Tk()
    root.title('App')
    root.geometry('600x400')

    label = Label(root, text='Look at me!', font=30, fg='blue')
    label.pack()

    # click_button = Button(root, text='click me!', width=8, command=click_action)
    # lub
    click_button = Button(root, text='click me!', width=8)
    # click_button.config(command=click_action)

    click_button.pack()

    # click_button.config(command=create_command(click_action, click_button))
    # lub
    click_button.config(command=lambda: increase_clicks(click_button))

    root.mainloop()

 


# tkinter marynarzyk

avaliable_choices = ['p', 'k', 'n']
cpu = choice(avaliable_choices)


def play(player, cpu):
    win_with = {'p': 'k', 'k': 'n', 'n': 'p'}
    if player == cpu:
        return None
    elif win_with[player] == cpu:
        return True
    else:
        return False


def play_cmd(player):
    global text_label
    cpu = choice(avaliable_choices)
    is_user_winner = play(player, cpu)
    if is_user_winner is None:
        text_label.config(text='Remis', fg='blue')
    elif is_user_winner:
        text_label.config(text='To bylo zwyciestwo absolutne', fg='green')
    else:
        text_label.config(text='gg ez noob', fg='red')


if __name__ == '__main__':
    root = Tk()
    root.title('Marynarzyk')
    root.geometry('300x150')

    text_label = Label(root, font=40, text='Zagrajmy w marynarza!')
    text_label.pack()

    Button(
        root, text='Papier', font=40, width=10,
        command=lambda: play_cmd('p')
    ).pack()
    Button(
        root, text='Kamien', font=40, width=10,
        command=lambda: play_cmd('k')
    ).pack()
    Button(
        root, text='Nozyce', font=40, width=10,
        command=lambda: play_cmd('n')
    ).pack()

    root.mainloop()

"""

# tkinter z real python

"""

def some_f(entry):
    sth = entry.get()
    print(sth)


if __name__ == '__main__':
    root = Tk()
    root.geometry('600x400')

    label = tk.Label(
        text="Hello, Tkinter",
        fg="white",  # Set the text color to white
        bg="black",  # Set the background color to black
        width=10,
        height=10
    )

    entry = tk.Entry(fg="yellow", bg="blue", width=50)

    button = tk.Button(
        text="Click me!",
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
        command=lambda: some_f(entry)
    )

    label.pack()
    button.pack()
    entry.pack()

    root.mainloop()


"""

# glowne okno
root = Tk()


# okienka pomocnicze wyswietlajace ostrzezenia i potwierdzenia
def show_warning(msg, window):
    wr_win = tk.Toplevel(window)
    wr_win.title('Blad')
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
    ak_win.title('Ukonczono!')
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
        show_warning('Wpisz w szarym polu jak chcesz nazwac plik!!!', d_win)
    elif choice_d == 0:
        show_warning('Wybierz jaki to ma byc plik, tzn. zaznacz zdjecie lub plik bin!', d_win)
    else:
        if choice_d == 1:
            download_photo(name + '.jpg')
            show_akn('Zdjecie pobrano pomyslnie, znajdziesz je w folderze Pobrane', d_win)
        elif choice_d == 2:
            download_binary(name + '.bin')
            show_akn('Plik bin pobrano pomyslnie, znajdziesz go w folderze Pobrane', d_win)


def open_download_choice():
    download_window = tk.Toplevel(root)
    download_window.title('Pobieranie losowych plikow')
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
    R1 = tk.Radiobutton(download_window, text="Zdjecie", variable=var, value=1)
    R1.pack()

    R2 = tk.Radiobutton(download_window, text="Plik bin", variable=var, value=2)
    R2.pack()

    enter_file_name = tk.Label(
        download_window,
        text="Podaj nazwe pliku:",
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


# sekcja porzadkowania
def open_cleaner():
    cleaner_win = tk.Toplevel(root)
    cleaner_win.title('Sprzatacz')
    cleaner_win.geometry('700x500')

    text_box = tk.Text(cleaner_win)
    text_box.insert('1.0', 'Uwaga!')
    text_box.insert('2.0', 'Wcisniecie tego przycisku oznacza przeniesienie wszystkich plikow')
    text_box.insert('3.0', 'z folderu Pobrane, do projektu i posegregowanie ich wedlug rozszerzen.')
    text_box.insert('4.0', 'Ponadto w przypadku przekroczenia limitu plikow najstarsze z nich zostana')
    text_box.insert('5.0', 'zarchiwizowane.')
    text_box.pack()



# ============================================= main ======================================
if __name__ == '__main__':
    root.title('System zarzadzania plikami')
    root.geometry("800x800")
    root.config(width=1000)

    download_button = tk.Button(
        text="Pobierz plik",
        width=800,
        height=10,
        bg="blue",
        fg="yellow",
        command=open_download_choice
    )
    download_button.pack()

    cleaner_button = tk.Button(
        text="Zrob porzadek",
        width=800,
        height=10,
        bg="orange",
        fg="yellow",
        command=open_cleaner
    )
    cleaner_button.pack()

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
        text='Ogolny',
        width=25,
        height=5,
        bg="yellow",
        fg="blue",
    )

    r2 = tk.Button(
        master=raports_choice,
        text='Ilosc plikow',
        width=25,
        height=5,
        bg="green",
        fg="blue",
    )

    r1.pack()
    r2.pack()

    root.mainloop()
