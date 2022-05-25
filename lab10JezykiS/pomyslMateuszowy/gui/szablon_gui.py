'''
Created on 2021-03-22

@author: Andrzej
'''

import configparser
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import NSEW
import os

dane_konfig="G:/Studia/JezykiSkryptowe/cos/Lab10/tc.txt"

class BazoweGui(tk.Frame):
    def __init__(self, master=None):
        self.konfig= configparser.ConfigParser()
        self.konfig.read(dane_konfig, "UTF8")        
        tk.Frame.__init__(self, master)
        self.parent=master
        self.parent.protocol("WM_DELETE_WINDOW", self.file_quit)
        domyslne=self.konfig["DEFAULT"]
        self.geometria_baza=domyslne.get('bazowa_geometria',"1000x800+50+50")
        self.parent.geometry(self.geometria_baza)
        self.utworz_bazowe_menu()
        self.utworz_pasek_narzedzi()
        self.utworz_status()
        self.utworz_okno_robocze()
        self.dodaj_menu_custom()
        self.dodaj_menu_help()
        self.utworz_dodatki()
        self.parent.columnconfigure(0, weight=999)
        self.parent.columnconfigure(1, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.parent.rowconfigure(1, weight=9999)
        self.parent.rowconfigure(2, weight=1)
    
    def utworz_pasek_narzedzi(self):
        self.toolbar_images = []   #muszą być pamiętane stale
        self.toolbar = tk.Frame(self.parent)
        for image, command in (
                ("images/editdelete.gif", self.file_usun),
                ("images/filenew.gif", self.file_new),
                ("images/fileopen.gif", self.file_open),
                ("images/filesave.gif", self.file_save)):
            image = os.path.join(os.path.dirname(__file__), image)
            try:
                image = tkinter.PhotoImage(file=image)
                self.toolbar_images.append(image)
                button = tkinter.Button(self.toolbar, image=image,
                                        command=command)
                button.grid(row=0, column=len(self.toolbar_images) -1) #KOLEJNE ELEMENTY
            except tkinter.TclError as err:
                print(err)  # gdy kłopoty z odczytaniem pliku
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky=tkinter.NSEW)
        
    
    def utworz_dodatki(self):
        pass
    
    def utworz_status(self):
        self.statusbar = tk.Label(self.parent, text="Linia statusu...",
                                       anchor=tkinter.W)
        self.statusbar.after(5000, self.clearStatusBar)
        self.statusbar.grid(row=2, column=0, columnspan=2,
                            sticky=tkinter.EW)
        pass
    
    def ustawStatusBar(self, txt):
        self.statusbar["text"] = txt
        
    def clearStatusBar(self):
        self.statusbar["text"] = ""
        
    def utworz_bazowe_menu(self):
        self.menubar = tk.Menu(self.parent)
        self.parent["menu"] = self.menubar
        fileMenu = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
                ("New...", self.file_new, "Ctrl+N", "<Control-n>"),
                ("Open...", self.file_open, "Ctrl+O", "<Control-o>"),
                ("Save", self.file_save, "Ctrl+S", "<Control-s>"),
                (None, None, None, None),
                ("Quit", self.file_quit, "Ctrl+Q", "<Control-q>")):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0,
                        command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="File", menu=fileMenu, underline=0) 
        pass
    
    def dodaj_menu_help(self):
        fileMenu = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
                ("New...", self.file_new, "Ctrl+N", "<Control-n>"),
                ("Open...", self.file_open, "Ctrl+O", "<Control-o>"),
                ("Save", self.file_save, "Ctrl+S", "<Control-s>"),
                (None, None, None, None),
                ("Quit", self.file_quit, "Ctrl+Q", "<Control-q>")):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0,
                        command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="Help", menu=fileMenu, underline=0) 
        pass    

    def file_quit(self, event= None):
        reply = tkinter.messagebox.askyesno(
                        "koniec pracy",
                        "naprawdę kończysz?", parent=self.parent)
        event=event
        if reply:
            geometria=self.parent.winfo_geometry()
            self.konfig["DEFAULT"]["bazowa_geometria"]=geometria
            with open(dane_konfig, 'w') as konfig_plik:
                self.konfig.write(konfig_plik)
            self.parent.destroy()
        pass
    
    def dodaj_menu_custom(self, event=None):
        pass 
    def file_usun(self):
        pass
    def file_new(self, event=None):
        event=event
        pass
    def file_open(self,event=None):
        event=event
        pass
    def file_save(self,event=None):
        event=event
        pass
    
    def utworz_okno_robocze(self):
        self.robocze = tk.Frame(self.parent, background='#00704A')
        self.robocze.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)
        pass
    
if __name__ == '__main__':
        root = tk.Tk()
        app = BazoweGui(master=root)
        app.mainloop()
        pass
    