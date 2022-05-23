"""
Created on 2021-05-18

@author: Andrzej
"""

import os
import random
import tkinter as tk
from tkinter import ANCHOR, END, Button, Listbox, filedialog
from tkinter.constants import DISABLED, NORMAL

from exif_jpg import Exif_dane
from gui.szablon_gui import BazoweGui

ident = "snaps"
to_check_id = "selected_pictures"
to_show_id = "pictures_2_view"


class Muster_Obraz(BazoweGui):
    pass

    def __init__(self, master=None):
        super().__init__(master)
        self.store_button = None
        self.toolbar_size = None
        self.stary_rozmiar = None
        self.obrazBt = None
        self.do_pokazania = None
        self.date_button = None
        self.view_button = None
        self.snap_no = None
        self.to_display = None
        self.to_delete = None
        self.to_show = None
        self.to_check = None
        self.dict = None
        self.magazin_addresses = None
        self.__view_mode = None
        self.__view_date_mode = None

    def start_pracy(self):
        self.__view_mode = 0
        self.__view_date_mode = 0
        self.magazin_addresses = [
            "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/animals",
            "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/cars",
            ""
        ]
        self.dict = {
            "Papugi i motyle": [
                "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/animals"
                "/butterfly.jpg",
                "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/animals/parrot.jpg",
            ],
            "Ferrari i red bull": [
                "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/cars/ferrari.jpg",
                "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/cars/redBull.jpg"
            ]
        }
        self.to_check = []  # all input snaps
        self.to_show = []  # selected snaps
        self.to_delete = []
        self.to_display = []  # what is on the screen
        self.set_pictures2check()
        self.snap_no = -1
        self.view_button = None
        self.date_button = None
        self.uzupelnij_toolbar()
        self.parent.bind("<Configure>", self.zmiana_rozmiaru)
        # nazwa_start=self.konfig["DEFAULT"]["icons"]+"images/"+self.konfig[ident]["obraz_start"]
        self.do_pokazania = Exif_dane(
            "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/animals/butterfly.jpg")
        self.obrazBt = tk.Button(self.robocze, text="start")
        self.obrazBt.pack(fill=tk.Y)
        self.stary_rozmiar = (10, 10)
        pass

    def uzupelnij_toolbar(self):
        for image, command in (
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/larrow.png",
                 self.to_left),
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/rarrow.png",
                 self.to_right),
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/uarrow.png",
                 self.to_top),
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/trash.png",
                 self.delete),
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/change.png",
                 self.change_order),
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/date.png",
                 self.to_date),
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/all.png",
                 self.to_all),
                (
                        "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/"
                        "dictionary.png",
                        self.dictionaries)):
            image = os.path.join(os.path.dirname(__file__), image)
            try:
                image = tk.PhotoImage(file=image)
                self.toolbar_images.append(image)
                button = tk.Button(self.toolbar, image=image,
                                   command=command)
                button.grid(row=0, column=len(self.toolbar_images) - 1)  # KOLEJNE ELEMENTY
            except tk.TclError as err:
                print(err)  # gdy kłopoty z odczytaniem pliku
        self.toolbar_size = len(self.toolbar_images)
        self.store_button = tk.Button(self.toolbar, text="Zapamiętaj", command=self.store_snap)
        self.store_button.grid(row=0, column=self.toolbar_size)
        self.toolbar_size += 1
        self.view_button = tk.Button(self.toolbar, text="Selekcja", command=self.change_mode)
        self.change_mode()
        self.view_button.grid(row=0, column=self.toolbar_size)
        self.toolbar_size += 1
        self.date_button = tk.Button(self.toolbar, text="Dzień", command=self.make_choice_calendar)
        self.date_button.grid(row=0, column=self.toolbar_size)
        self.toolbar_size += 1
        pass

    def store_snap(self):
        if self.snap_no < 0:
            self.ustawStatusBar("brak zdjęć do zapamiętania")
            return
        file_name = self.to_display[self.snap_no]
        if file_name in self.to_show:
            self.ustawStatusBar("już to mam " + file_name)
            return
        self.to_show.append(file_name)
        pass

    def to_left(self):
        test = self.snap_no - 1
        if not self.set_snap_no(test):
            return
        self.dispay_snap()
        pass

    def to_right(self):
        test = self.snap_no + 1
        if not self.set_snap_no(test):
            return
        self.dispay_snap()
        pass

    def to_top(self):
        if not self.set_snap_no(0):
            return
        self.dispay_snap()
        pass

    def to_all(self):
        if not self.set_snap_no(0):
            return
        self.to_display = self.to_check
        pass

    def delete(self):
        self.dispay_snap()
        for elem in self.to_delete:
            if self.to_show.__contains__(elem):
                self.to_show.remove(elem)
            if self.to_check.__contains__(elem):
                self.to_check.remove(elem)
            # os.remove(elem)     ?
        pass

    def change_order(self):
        temp = []
        for elem in self.to_display:
            temp.insert(random.randint(0, len(temp)), elem)
        self.to_display = temp
        self.set_snap_no(0)
        self.dispay_snap()
        pass

    def file_usun(self):
        if self.snap_no < 0:
            self.ustawStatusBar("brak zdjęć do usunięcia")
            return
        file_name = self.to_display[self.snap_no]
        if file_name in self.to_show:
            self.ustawStatusBar("Już znajduje się w koszu " + file_name)
            return
        self.to_delete.append(file_name)

    def set_snap_no(self, wanted):
        if len(self.to_display) == 0:
            self.ustawStatusBar("brak zdjęć do pokazania")
            return False
        if 0 <= wanted < len(self.to_display):
            self.snap_no = wanted
            return True
        if wanted < 0:
            self.snap_no = len(self.to_display) - 1
            return True
        if wanted >= len(self.to_display):
            self.snap_no = 0
        return True

    def dispay_snap(self):
        file_name = self.to_display[self.snap_no]
        try:
            self.do_pokazania = Exif_dane(file_name)
            self.obrazBt.config(image=self.test_image)
            self.zmiana_rozmiaru(None, False)
            msg = "%s %s (%d/%d)" % (self.do_pokazania, file_name, self.snap_no + 1, len(self.to_display))
            self.ustawStatusBar(msg)
        except:
            self.ustawStatusBar("problem z plikiem: " + file_name)
            return
        pass

    def change_mode(self):
        if not self.view_button:
            return
        self.__view_mode = (self.__view_mode + 1) % 3
        self.snap_no = 0
        if self.__view_mode == 0:
            self.view_button.configure(bg="blue", fg="yellow", text="Przegląd")
            self.store_button['state'] = DISABLED
            self.to_display = self.to_show
        elif self.__view_mode == 1:
            self.view_button.configure(fg="red", bg="yellow", text="Selekcja")
            self.store_button['state'] = NORMAL
            self.to_display = self.to_check
        else:
            self.view_button.configure(fg="white", bg="red", text="Usuwanie")
            self.store_button['state'] = DISABLED
            self.to_display = self.to_delete

        if len(self.to_display) == 0:
            self.snap_no = -1
        else:
            self.snap_no = 0
        pass

    def make_choice_calendar(self):
        if not self.date_button:
            return
        self.__view_date_mode = (self.__view_date_mode + 1) % 4
        self.snap_no = 0
        if self.__view_date_mode == 0:
            self.date_button.configure(bg="white", fg="black", text="Dzień")
        elif self.__view_date_mode == 1:
            self.date_button.configure(bg="white", fg="black", text="Tydzień")
        elif self.__view_date_mode == 2:
            self.date_button.configure(bg="white", fg="black", text="Miesiąc")
        else:
            self.date_button.configure(bg="white", fg="black", text="Rok")

        if len(self.to_display) == 0:
            self.snap_no = -1
        else:
            self.snap_no = 0
        pass

    def to_date(self):
        if self.__view_date_mode == 0:
            self.close_date('day')
        elif self.__view_date_mode == 1:
            self.close_date('week')
        elif self.__view_date_mode == 2:
            self.close_date('month')
        else:
            self.close_date('year')

    def close_date(self, period_of_time):
        temp = []
        date = Exif_dane(self.to_display[self.snap_no])
        for elem in self.to_display:
            ex_elem = Exif_dane(elem)
            # print(date.daj_czas()[0:10],"    AND     ",ex_elem.daj_czas()[0:10])    2020/09/09
            if period_of_time == 'day':
                if ex_elem.daj_czas()[0:10].__eq__(date.daj_czas()[0:10]):
                    temp.append(elem)
            elif period_of_time == 'week':
                if (abs(int(ex_elem.daj_czas()[8:10]) - int(date.daj_czas()[8:10])) <= 3) and ex_elem.daj_czas()[
                                                                                              0:7].__eq__(
                    date.daj_czas()[0:7]):
                    temp.append(elem)
            elif period_of_time == 'month':
                if ex_elem.daj_czas()[0:7].__eq__(date.daj_czas()[0:7]):
                    temp.append(elem)
            elif period_of_time == 'year':
                if ex_elem.daj_czas()[0:4].__eq__(date.daj_czas()[0:4]):
                    temp.append(elem)
            else:
                pass
        self.to_display = temp

    def dictionaries(self):
        d_root = tk.Tk()
        d_root.title("Wybór słownika do oglądania")
        d_root.geometry("200x400")

        listbox = Listbox(d_root)
        listbox.pack(pady=15)

        listbox.insert(END, "Lato 2019")
        listbox.insert(END, "Zima 2022")

        def select():
            self.to_display = self.dict[listbox.get(ANCHOR)]
            d_root.destroy()

        select_button = Button(d_root, text="Select", command=select)
        select_button.pack(pady=15)
        d_root.mainloop()

    def zmiana_rozmiaru(self, event, test_size=True):
        event = event
        geometria = self.robocze.winfo_geometry()
        if geometria == "1x1+0+0":
            return
        rozmiar = self.do_pokazania.get_size(self.robocze)
        roznica = rozmiar[0] + rozmiar[1] - self.stary_rozmiar[0] - self.stary_rozmiar[1]
        if abs(roznica) < 6 and test_size:
            return
        self.stary_rozmiar = rozmiar
        self.test_image = self.do_pokazania.ustaw_rozmiar(rozmiar)
        self.obrazBt.config(image=self.test_image)
        pass

    def file_new(self, event=None):
        event = event
        my_filetypes = [('pictures', '.tst')]
        folder2check = self.konfig.get(ident, "ini_save_dir", fallback=None)
        if not folder2check:
            return
        answer = filedialog.askopenfilename(parent=self.parent,
                                            initialdir=folder2check,
                                            title="Please select show:",
                                            filetypes=my_filetypes)
        if not answer:
            return
        with open(answer, 'r') as infile:
            fname = infile.read()
            self.to_show.append(fname)
        self.ustawStatusBar("wczytano selekcję: " + answer)
        pass

    def file_save(self, event=None):
        event = event  # filedialog.asksaveasfilename(
        my_filetypes = [('custom_save', '.tst')]
        folder2check = self.konfig.get(ident, "ini_save_dir", fallback=None)
        if not folder2check:
            return
        answer = filedialog.asksaveasfilename(parent=self.parent,
                                              initialdir=folder2check,
                                              title="Please select a file:",
                                              filetypes=my_filetypes)
        if not answer:
            return
        with open(answer, 'w') as outfile:
            for fname in self.to_show:
                outfile.write(fname)
        self.ustawStatusBar("zapisano selekcję: " + answer)
        pass

    def file_open(self, event=None):
        my_filetypes = [('pictures', '.jpg')]
        folder2check = self.konfig.get(ident, "ini_check_dir", fallback=None)
        if not folder2check:
            return
        answer = filedialog.askopenfilename(parent=self.parent,
                                            initialdir=folder2check,
                                            title="Please select a file:",
                                            filetypes=my_filetypes)
        nk = os.path.split(answer)
        answer = nk[0]
        print(answer)
        self.konfig.set(ident, "ini_check_dir", answer)
        self.set_pictures2check()
        event = event
        pass

    def show_map(self):
        if not self.do_pokazania.drawMap():
            self.ustawStatusBar("brak danych geo lokalizacji")
        pass

    def set_pictures2check(self):
        self.to_check = []
        if not self.konfig.has_section(ident):
            self.konfig.add_section(ident)
        folder2check = self.konfig.get(ident, "ini_check_dir", fallback=None)
        if not folder2check:
            self.ustawStatusBar("Brak folderu:", folder2check)
            return

        self.add_to_check(folder2check)
        for adres in self.magazin_addresses:
            self.add_to_check(adres)
        self.ustawStatusBar("%s %d" % ("Liczba wpisanych plików", len(self.to_check)))
        self.to_display = self.to_check
        pass

    def add_to_check(self, adres):
        for root, dirs, files in os.walk(adres, topdown=True):
            dirs = dirs
            for nazwa in files:
                file_name = os.path.join(root, nazwa)
                nk = os.path.split(file_name)
                if not nk[1].upper().endswith(".JPG"):
                    continue
                file_name = os.path.normpath(file_name)
                self.to_check.append(file_name)


if __name__ == '__main__':
    root = tk.Tk()
    app = Muster_Obraz(root)
    app.start_pracy()
    app.mainloop()
    pass

"""
 # struktury i zmienne pomocnicze:
        self.magazin_addresses = [
            "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/cars",
            "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/animals",
            ""
        ]
        self.dict = {
            "Motyle i Koty": [
                "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/animals/"
                "butterfly.jpg",
                "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/animals/cat.jpg"
            ],
            "Ferrari i red bull": [
                "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki "
                "Skryptowe/laby/lab10JezykiS/Inter/gui/cars/ferrari.jpg",
                "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki "
                "Skryptowe/laby/lab10JezykiS/Inter/gui/cars/redBull.jpg "
            ]}

        self.to_delete = []
        self.date_button = None
        self.__view_date_mode = 0

    def start_pracy(self):

        # struktury wbudowane
        self.__view_mode = True
        self.to_check = []  # all input snaps
        self.to_show = []  # selected snaps
        self.to_display = []  # what is on the screen
        self.set_pictures2check()
        self.snap_no = -1
        self.view_button = None
        self.uzupelnij_toolbar()
        self.parent.bind("<Configure>", self.zmiana_rozmiaru)
        self.do_pokazania = Exif_dane(
            "/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/animals/butterfly.jpg"
        )
        self.obrazBt = tk.Button(self.robocze, text="start")
        self.obrazBt.pack(fill=tk.Y)
        self.stary_rozmiar = (10, 10)
        pass

    def uzupelnij_toolbar(self):
        for image, command in (
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/browser.png",
                 self.show_map),
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/larrow.png",
                 self.to_left),
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/rarrow.png",
                 self.to_right),
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/uarrow.png",
                 self.to_top),
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/change.png",
                 self.change_order),
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/trash.png",
                 self.delete),
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/date.png",
                 self.to_date),
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab10JezykiS/Inter/gui/images/all.png",
                 self.to_all),
                ("/media/remmo/Acer/Uczelnia/Semestr4/Jezyki "
                 "Skryptowe/laby/lab10JezykiS/Inter/gui/images/dictionary.png",
                 self.dictionaries)
"""
