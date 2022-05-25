#!/usr/bin/env python3

import tkinter as tk
from PIL import  Image, ImageTk
from PIL.ExifTags import TAGS, GPSTAGS
from math import  cos, sin,  atan2, sqrt, pi
import os, time



class Exif_dane():
    def __init__(self, nazwa_pliku, magazin_addresses = []):
        self.__nazwa_pliku=nazwa_pliku       

        adres = self.exist(nazwa_pliku, magazin_addresses)
        if not adres[0]:
            raise BaseException("Brak pliku:\t{0}".format(nazwa_pliku))
        self.__plik_rozmiar=os.path.getsize(adres[1] + nazwa_pliku)
        try:
            self.__zdjecie_samo = Image.open(adres[1] + nazwa_pliku)
            self.__exif_data=self.get_exif_data()
        except:
            raise BaseException("Zly format pliku:\t{0}".format(adres[1] + nazwa_pliku))            
        self.__czas=self.__daj_czas_wykonania()
        self.__test_image=ImageTk.PhotoImage(self.__zdjecie_samo)
        self.__lat_lng=self.get_lat_lng()
        self.__rozmiar=self.__zdjecie_samo.size
        self.__lokal=self.daj_lokal()
        self.__home_location=(51.10854, 17.06255) #PWR
        pass

    def exist(self, nazwa_pliku,  magazin_addresses):
        if os.path.exists(nazwa_pliku):
            return (True, "")
        for adres in magazin_addresses:
            if os.path.exists(adres + nazwa_pliku):
                return (True, adres)
        return (False, "")
    
    def daj_photoImage(self):
        return self.__test_image
    
    def daj_plik_rozmiar(self):
        return self.__plik_rozmiar
    
    def daj_czas(self):
        return self.__czas
    
    def daj_zdjecie_rozmiar(self):
        wynik=self.__zdjecie_samo.size
        return wynik
    def daj_lokal(self):
        local=self.__lat_lng
        if not local[0]:
            local=(0.0,0.0)
        wynik="lat:{0:2.2f} lng:{1:2.2}".format(local[0], local[1])
        return wynik

    def zmien_rozmiar(self, okno):
        rozmiar=self.get_size(okno)
        img = self.__zdjecie_samo.resize(rozmiar, Image.ANTIALIAS)
        self.__test_image=ImageTk.PhotoImage(img)
        return self.__test_image

    def ustaw_rozmiar(self, rozmiar):
        img = self.__zdjecie_samo.resize(rozmiar, Image.ANTIALIAS)
        self.__test_image=ImageTk.PhotoImage(img)
        return self.__test_image

    def daj_image(self):
        return self.__zdjecie_samo
       
    def get_exif_data(self):
        exif_data = {}
        info = self.__zdjecie_samo._getexif()
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                if decoded == "GPSInfo":
                    gps_data = {}
                    for t in value:
                        sub_decoded = GPSTAGS.get(t, t)
                        gps_data[sub_decoded] = value[t]

                    exif_data[decoded] = gps_data
                else:
                    exif_data[decoded] = value
        self.exif_data = exif_data
        return exif_data
    
    def get_size(self, okienko):
        okno_h=okienko.winfo_height()
        zdjecie_h=self.__rozmiar[1]
        zdjecie_w=self.__rozmiar[0]
        okno_w=(zdjecie_w*okno_h)//zdjecie_h
        return (okno_w, okno_h)

    def __daj_czas_wykonania(self):
        structt=time.localtime(os.path.getmtime(self.__nazwa_pliku))
        datum="{0:0>4d}/{1:0>2d}/{2:0>2d} ".format(structt.tm_year,structt.tm_mon,structt.tm_mday)
        dtime="{0:0>2d}/{1:0>2d}/{2:0>2d}".format(structt.tm_hour,structt.tm_min,structt.tm_sec)
        fdate="%s%s" % (datum, dtime)
        if not self.__exif_data:
            return fdate
        try:
            tt= self.exif_data['DateTimeOriginal']
            tt=tt.replace(":","/")
        except :
            return fdate
        return tt   

    def get_if_exist(self, data, key):
        if key in data:
            return data[key]
        return None

    def convert_to_degress(self, value):
        d0 = value[0][0]
        d1 = value[0][1]
        d = float(d0) / float(d1)
        m0 = value[1][0]
        m1 = value[1][1]
        m = float(m0) / float(m1)
        s0 = value[2][0]
        s1 = value[2][1]
        s = float(s0) / float(s1)
        return d + (m / 60.0) + (s / 3600.0)

    def get_lat_lng(self):
        lat = None
        lng = None
        exif_data = self.__exif_data
        if "GPSInfo" in exif_data:      
            gps_info = exif_data["GPSInfo"]
            gps_latitude = self.get_if_exist(gps_info, "GPSLatitude")
            gps_latitude_ref = self.get_if_exist(gps_info, 'GPSLatitudeRef')
            gps_longitude = self.get_if_exist(gps_info, 'GPSLongitude')
            gps_longitude_ref = self.get_if_exist(gps_info, 'GPSLongitudeRef')
            if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
                lat = self.convert_to_degress(gps_latitude)
                if gps_latitude_ref != "N":                     
                    lat = 0 - lat
                lng = self.convert_to_degress(gps_longitude)
                if gps_longitude_ref != "E":
                    lng = 0 - lng
        return lat, lng
    
  
    def set_home_location(self, lat, lng):
        self.__home_location=(lat, lng)
        pass
    
    def get_distance_alt(self, inny_obraz):
        mlat, mlng=self.__lat_lng
        if not mlat:
            return -1
        inny=Exif_dane(inny_obraz)
        olat, olng = inny.get_lat_lng() 
        radius = 6371 * 1000 
        dLat = (olat-mlat) * pi / 180
        dLng = (olng-mlng) * pi / 180
        mlat = mlat * pi / 180
        olat = olat * pi / 180
        val = sin(dLat/2) * sin(dLat/2) + sin(dLng/2) * sin(dLng/2) * cos(mlat) * cos(olat)
        ang = 2 * atan2(sqrt(val), sqrt(1-val))    
        return radius*ang
    
    def get_distance(self, inny_obraz):
        inny=Exif_dane(inny_obraz)
        return self.__get_distance_from_to(self.__lat_lng, inny.get_lat_lng()) 
    
    def get_distance_from_home(self):
        mlat, mlng=self.__lat_lng
        if not mlat:
            return -1
        return self.__get_distance_from_to((mlat, mlng), (self.__home_location)) 
        pass
    
    def __get_distance_from_to(self, start, dest):
        mlat, mlng =start
        olat, olng =dest
        if not mlat or not olat:
            return -1
        radius = 6371 * 1000 
        dLat = (olat-mlat) * pi / 180
        dLng = (olng-mlng) * pi / 180
        mlat = mlat * pi / 180
        olat = olat * pi / 180
        val = sin(dLat/2) * sin(dLat/2) + sin(dLng/2) * sin(dLng/2) * cos(mlat) * cos(olat)
        ang = 2 * atan2(sqrt(val), sqrt(1-val))    
        in_meters=radius*ang
        return round(in_meters/1000.0,3)
        
    
    def __str__(self):
        x=self.get_lat_lng()
        if (x==(None, None)):
            loc="no location given"
        else:
            m=self.get_distance_from_home()
            loc="%4.3f  %2.5f; %2.5f"%(m,x[0],x[1]) 
        result=self.daj_czas()+"\t"+loc
        return result
        

    def drawMap(self):
        import webbrowser
        #url https://www.google.com/maps?q=53.96277777777778,21.738611111111112
        decimal_latitude = self.get_lat_lng()[0]
        decimal_longitude = self.get_lat_lng()[1]
        if decimal_latitude==None or decimal_longitude==None:
            return False
        url = f"https://www.google.com/maps?q={decimal_latitude},{decimal_longitude}"
        webbrowser.open_new_tab(url)
        return True 

if __name__ == '__main__':
    root = tk.Tk()   # konieczne dla PhotoImage
    
    metaData= Exif_dane('e:/assets/3LOC.JPG')  # Giżycko
    metaData.drawMap()
    
    metaData= Exif_dane('e:/assets/1.JPG') 
    print ("Tunezja",  metaData)  # Tunezja

    metaData= Exif_dane('e:/assets/11.JPG') 
    print ("Tunezja",  metaData)  # Tunezja

    print (1,metaData)
    metaData= Exif_dane('e:/assets/2.JPG')
    print (2,metaData)
    metaData= Exif_dane('e:/assets/3LOC.JPG')
    print (3,metaData)
    print (metaData.get_lat_lng())
    print (metaData.daj_czas())
    print (metaData.daj_plik_rozmiar())
    print (metaData.daj_zdjecie_rozmiar())

    print (4, metaData.get_distance_from_home())
    print (5, metaData.get_distance('e:/assets/4LOC.JPG'))
    
    pass    
