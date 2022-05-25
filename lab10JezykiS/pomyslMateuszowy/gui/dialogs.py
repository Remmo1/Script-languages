'''
Created on 2021-03-29

@author: Andrzej
'''
import tkinter as tk

import time
from datetime import date
from tkcalendar import DateEntry
import re

from appls.app_funkcje import levenshtein

class Custom_Dialog(tk.Toplevel):
    def __init__(self, parent, prompt, domyslnie="XX", polozenie="+150+450"):
        tk.Toplevel.__init__(self, parent)
        self.geometry(polozenie)
        parent.wm_attributes("-disabled", True)
        self.transient(parent)
        self.title(prompt)
        self.root=parent    
        self.wynik = tk.StringVar()
        self.wynik.set(domyslnie)
        self.protocol("WM_DELETE_WINDOW", self.close_toplevel)
        self.ustaw_kontrolki()
    def ustaw_kontrolki(self):
        pass   
    def show(self):
        self.wm_deiconify()
        self.wait_window()
        return self.wynik.get()
    def jest_ok(self):
        self.root.wm_attributes("-disabled", False)
        self.destroy()
        pass
    def close_toplevel(self):
        self.root.wm_attributes("-disabled", False)
        self.destroy()

class Pole_Edycyjne(Custom_Dialog):
    def __init__(self, parent, prompt, domyslnie="YYYY", polozenie="+100+200"):
        Custom_Dialog.__init__(self, parent, prompt, domyslnie, polozenie)
        pass    
    def on_ok(self):
        self.wynik.set(self.tekst.get())
        self.jest_ok()
        pass
    def not_ok(self):
        self.wynik.set(None)
        self.jest_ok()
        pass
    def ustaw_kontrolki(self):
        self.tekst = tk.Entry(self, text=self.wynik.get(), textvariable=self.wynik)  
        self.tekst.grid(column=0, row=0)   
        self.ok_button = tk.Button(self, text="OK", command=self.on_ok)  
        self.ok_button.grid(column=1, row=0)   
        self.x_button = tk.Button(self, text="nie", command=self.not_ok)  
        self.x_button.grid(column=2, row=0)   
    
class Sam_Przycisk(Custom_Dialog):
    def __init__(self, parent, prompt, domyslnie="YYYY", polozenie="+100+200"):
        Custom_Dialog.__init__(self, parent, prompt, domyslnie, polozenie)
        pass    
    def on_ok(self):
        self.wynik.set("Nowa wartosc")
        self.jest_ok()
        pass
    def ustaw_kontrolki(self):
        self.ok_button = tk.Button(self, text="OK", command=self.on_ok)  
        self.ok_button.pack()   
        
        # https://www.tutorialspoint.com/python3/tk_listbox.htm
class Daj_Znacznik(Custom_Dialog):
    def __init__(self, parent, prompt, domyslnie="k", wykaz=[]):
        Custom_Dialog.__init__(self, parent, prompt, domyslnie)
        self.podobne=3
        wykaz.sort()
        self.wszystkie=wykaz
        self.wybrane=[]
        self.znacznik.set(domyslnie)
        self.selekcja()
        self.wpisz_do_boxa()
        pass
    
    def ustaw_kontrolki(self):
        self.lewy_panel=tk.Frame(self)
        self.lewy_panel.grid(row=0, column=0)
        self.prawy_panel=tk.Frame(self)
        self.prawy_panel.grid(row=0, column=1)
        
        self.znacznik= tk.StringVar(self)
        self.edit= tk.Entry(self.lewy_panel,  textvariable=self.znacznik)
        self.edit.pack(side="top")
        self.lista_zn=tk.Listbox(self.lewy_panel, selectmode="SINGLE")
        self.lista_zn.pack(side="bottom")

        self.ok = tk.Button(self.prawy_panel, text="akceptacja", command=self.on_ok)  
        self.ok.pack()   
        self.dopisz = tk.Button(self.prawy_panel, text="dopisz", command=self.on_dopisz)  
        self.dopisz.pack()   
        self.usun = tk.Button(self.prawy_panel, text="usun", command=self.on_usun)  
        self.usun.pack()   
        self.wpisz = tk.Button(self.prawy_panel, text="do edycji", command=self.on_wpisz)  
        self.wpisz.pack()   
        self.wpisz = tk.Button(self.prawy_panel, text="poniechaj", command=self.on_poniechaj)  
        self.wpisz.pack()   
        self.wpisz = tk.Button(self.prawy_panel, text="filtruj", command=self.on_filtruj)  
        self.wpisz.pack()   
    
    # do okna edycyjnego    
    def on_poniechaj(self):
        self.wynik.set("")      
        self.jest_ok()
        return 
    
    def on_filtruj(self):
        return 
    
    def on_wpisz(self):
        wybrano=self.lista_zn.curselection()
        if not wybrano:
            return
        for idx in wybrano:
            txt=self.lista_zn.get(idx)
            self.znacznik.set(txt)
            return

    def on_dopisz(self):
        nowy=self.znacznik.get()
        wszystkie=[]
        for idx in range(self.lista_zn.size()):
            elem=self.lista_zn.get(idx)
            wszystkie.append(elem)
        if wszystkie.count(nowy)>0:
            return
        wszystkie.append(nowy)
        wszystkie.sort()
        self.lista_zn.delete(0,self.lista_zn.size())
        for elem in wszystkie:
            self.lista_zn.insert(tk.END, elem)
        pass
    
    def on_usun(self):
        do_kasowania=self.lista_zn.curselection()
        if not do_kasowania:
            return
        for idx in do_kasowania:
            self.lista_zn.delete(idx)
        pass    
    
    
    def __oddaj_liste(self):
        wynik=""
        for idx in range(self.lista_zn.size()):
            elem=self.lista_zn.get(idx)
            wynik+="\t"
            wynik+=elem
        return wynik
    
    def on_ok(self):
        do_oddania=self.lista_zn.curselection()
        if not do_oddania:
            return
        oddaj=self.lista_zn.get(do_oddania)
        oddaj+=self.__oddaj_liste()
        self.wynik.set(oddaj)      
        self.jest_ok()
        pass

    def selekcja(self):
        self.wybrane=[]
        szukam=self.znacznik.get()
        for elem in self.wszystkie:
            #  k==kk[0:len(k)]
            if len(szukam)==0:
                self.wybrane.append(elem)
                continue
            w=levenshtein(szukam, elem)
            if w<=self.podobne:
                self.wybrane.append(elem)
    
    def wpisz_do_boxa(self):
        self.lista_zn.delete(0, self.lista_zn.size())
        for elem in self.wszystkie:
            self.lista_zn.insert(tk.END, elem)
        
class Daj_Date(Custom_Dialog):
    def __init__(self, parent, prompt, domyslnie=None):
        Custom_Dialog.__init__(self, parent, prompt, domyslnie)
        pass
    
    def on_ok(self):
        wybrano=self.cal.get()
        self.wynik.set(wybrano)
        self.jest_ok()
        pass
    
    def ustaw_kontrolki(self):
        self.ok_button = tk.Button(self, text="OK", command=self.on_ok)     
        dzis=date.fromtimestamp(time.time())
        self.cal=DateEntry(self, width=12, background='darkblue', locale="pl_PL.UTF-8",
                    foreground='white', borderwidth=2, year=dzis.year, month=dzis.month, day=dzis.day)
        self.ok_button.pack(side="right")
        self.cal.pack(fill="both", expand=True)
        

class CustomDateDialog(tk.Toplevel):
    def __init__(self, parent, prompt, p_year=2021, p_month=3, p_day=1):
        tk.Toplevel.__init__(self, parent)
        self.root=parent    
        self.protocol("WM_DELETE_WINDOW", self.close_toplevel)
        self.var = tk.StringVar()

        self.label = tk.Label(self, text=prompt)
        self.ok_button = tk.Button(self, text="OK", command=self.on_ok)     
        self.cal=DateEntry(self, width=12, background='darkblue', locale="pl_PL.UTF-8",
                    foreground='white', borderwidth=2, year=p_year, month=p_month, day=p_day)
        
        self.label.pack(side="top", fill="x")
        self.ok_button.pack(side="right")
        self.cal.pack(fill="both", expand=True)

    def on_ok(self, event=None):
        event=event
        wybrano=self.cal.get()
        self.var.set(wybrano)
        self.root.wm_attributes("-disabled", False)
        self.destroy()

    def show(self):
        self.wm_deiconify()
        self.wait_window()
        return self.var.get()

    def close_toplevel(self):
        self.root.wm_attributes("-disabled", False)
        self.var.set(None)
        self.destroy()


class Data_od_DzienMscRok(CustomDateDialog):
    def __init__(self, parent, prompt, data_domysl):
        forma=r"(\d+)[\.-/](\d+)[\.-/](\d+)"
        r=re.search(forma,data_domysl)
        if not r:
            return
        CustomDateDialog.__init__(self, parent, prompt, int(r.group(3)),int(r.group(2)),int(r.group(1)))
        pass

class Od_Dzisiaj(CustomDateDialog):
    def __init__(self, parent, prompt):
        dzis=date.fromtimestamp(time.time())
        CustomDateDialog.__init__(self, parent, prompt, dzis.year,dzis.month,dzis.day)
        pass

class Date_getter(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.root=parent
        self.button = tk.Button(self, text="Podaj date", command=self.on_button)
        self.label = tk.Label(self, text="", width=20)
        self.button.pack(padx=8, pady=8)
        self.label.pack(side="bottom", fill="both", expand=True)

    def on_button(self):
        self.root.wm_attributes("-disabled", True)
        string = CustomDateDialog(self.root, "podaj datę:").show()
        self.label.configure(text="Wprowadziłeś:\n" + string)

if __name__ == "__main__":
    root = tk.Tk()
    root.wm_geometry("400x200+500+400")
    
    dialog=Custom_Dialog(root, "test!")
    dialog.show()
    
    edycja=Pole_Edycyjne(root, "edycja","domyślna wartość")
    print ("Pole_Edycyjne",edycja.show())
        
    wybory=["mysz", "kotek", "kocisko"]
    dialog=Daj_Znacznik(root, "znacznik?", "xxx", wybory)
    wybrano=dialog.show()
    print ("Daj_Znacznik",wybrano)
    
    dialog=Daj_Date(root, "data początkowa to dzisiaj")
    wybrano=dialog.show()
    print ("Daj_Date",wybrano)
       
    dialog=Od_Dzisiaj(root, "data poczatkowa")
    wybrano=dialog.show()
    print ("Od_Dzisiaj",wybrano)
    
    dialog=Sam_Przycisk(root, "test!")
    wybrano=dialog.show()
    print ("Sam_Przycisk",wybrano)
    
    dialog=Daj_Znacznik(root, "znacznik","")
    wybrano=dialog.show()
    print ("Daj_Znacznik pusty", wybrano)
    
    root.mainloop()
    