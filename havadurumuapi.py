import tkinter as tk
from PIL import ImageTk
import requests
import json

# Hava durumu sorgu fonkisyonu
def hava_durumu():
    sehir = sehirMetin.get()
    apiAnahtari = 'api-key'# mevcut api anahtarı güvenlik nedeniyle gösterilmiyor
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={apiAnahtari}')


    havaVerisi = response.json()


    gokyuzuAciklama = havaVerisi['weather'][0]['description']

    # Hava durumu açıklamasını Türkçe'ye çevirme
    gokyuzutipleriEN = ['clear sky', 'few clouds', 'overcast clouds', 'scattered clouds',
                        'broken clouds', 'shower rain', 'rain', 'thunderstorm', 'snow', 'mist']
    gokyuzuTipleriTR = ['Güneşli', 'Az Bulutlu', 'Çok Bulutlu(Kapalı)', 'Alçak Bulutlu', 'Yer Yer Açık Bulutlu',
                        'Sağanak Yağmurlu', 'Yağmurlu', 'Gök Gürültülü Fırtına', 'Karlı', 'Puslu']
    for i in range(len(gokyuzutipleriEN)):
        if gokyuzuAciklama == gokyuzutipleriEN[i]:
            gokyuzuAciklama = gokyuzuTipleriTR[i]

    sehirAdi = havaVerisi['name']

    # Sıcaklık verileri ve K'den °C'a dönüştürme
    sicaklik = round((havaVerisi['main']['temp'] - 273.15), 2)# Genel sıcaklık
    hisSicaklik = round((havaVerisi['main']['feels_like'] - 273.15), 2)  # hissedilen sıcaklık
    minSicaklik = round((havaVerisi['main']['temp_min'] - 273.15), 2)# Minimum sıcaklık
    maksSicaklik = round((havaVerisi['main']['temp_max'] - 273.15), 2)# Maksimum sıcaklık

    # Hava durumu bilgisini düzenleme
    hava_durumu_bilgisi = "Şehir: {}\nGökyüzü: {}\nSıcaklık: {}°C\nHissedilen: {}°C\nMinimum: {}°C\nMaksimum: {}°C".format(
        sehirAdi, gokyuzuAciklama, sicaklik, hisSicaklik, minSicaklik, maksSicaklik)

    return hava_durumu_bilgisi

# Hava durumu sorgusu isteme ve sonuç görüntüleme
def get_weather():
    hava_durumu_bilgisi = hava_durumu()
    sonuc.config(text=hava_durumu_bilgisi)


# pencere oluşturma
pencere = tk.Tk()
pencere.title("Hava Durumu Uygulaması")
pencere.geometry("600x400")

# Arka plan resmi
arkaresim = ImageTk.PhotoImage(file="resim1.png")
label = tk.Label(pencere, image=arkaresim)
label.place(relwidth=1, relheight=1)

# Şehir etiketi
sehirEtiket = tk.Label(pencere, text="Şehir Adı:", font="Verdana 14 bold")
sehirEtiket.place(x=260, y=20)

# Şehir giriş alanı
sehirMetin = tk.Entry(pencere, font="Verdana 14 bold")
sehirMetin.place(x=170, y=60,)

# Hava durumu sorgu butonu
sorguButton = tk.Button(
    pencere, text="Hava Durumu Sorgula", command=get_weather)
sorguButton.place(x=250, y=100)

# Hava durumu sonucunu gösterecek etiket
sonuc = tk.Label(pencere, text="", font="Verdana 9 bold")
sonuc.place(x=250, y=140)

pencere.mainloop()
