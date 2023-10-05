import tkinter as tk
from PIL import ImageTk
import requests
import json

# Hava durumu sorgu fonkisyonu
def hava_durumu():
    sehir = sehiradi.get()
    api_key = 'api-key' #mevcut api anahtarı güvenlik nedeniyle gösterilmiyor
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}')

    weatherData = response.json()

    # Hava durumu açıklamasını Türkçe'ye çevirme
    skyDescription = weatherData['weather'][0]['description']
    cityName = weatherData['name']
    skyTypes = ['clear sky', 'few clouds', 'overcast clouds', 'scattered clouds',
                'broken clouds', 'shower rain', 'rain', 'thunderstorm', 'snow', 'mist']
    skyTypesTR = ['Güneşli', 'Az Bulutlu', 'Çok Bulutlu(Kapalı)', 'Alçak Bulutlu', 'Yer Yer Açık Bulutlu',
                  'Sağanak Yağmurlu', 'Yağmurlu', 'Gök Gürültülü Fırtına', 'Karlı', 'Puslu']
    for i in range(len(skyTypes)):
        if skyDescription == skyTypes[i]:
            skyDescription = skyTypesTR[i]

    # Sıcaklık verilerini K'den°C'a dönüştürme 
    temp = round((weatherData['main']['temp'] - 273.15), 2)  # Genel sıcaklık
    feels_temp = round(
        (weatherData['main']['feels_like'] - 273.15), 2)  # hissedilen sıcaklık
    temp_min = round((weatherData['main']['temp_min'] - 273.15), 2)  # Minimum sıcaklık
    temp_max = round((weatherData['main']['temp_max'] - 273.15), 2)  # Maksimum sıcaklık

    # Hava durumu bilgisini düzenleme
    hava_durumu_bilgisi = "Şehir: {}\nGökyüzü: {}\nSıcaklık: {}°C\nHissedilen: {}°C\nMinimum: {}°C\nMaksimum: {}°C".format(
        cityName, skyDescription, temp, feels_temp, temp_min, temp_max)

    return hava_durumu_bilgisi

# Hava durumu sorgusu isteme ve sonuç görüntüleme
def get_weather():
    hava_durumu_bilgisi = hava_durumu()
    sonuc.config(text=hava_durumu_bilgisi)

# pencere oluşturma
window = tk.Tk()
window.title("Hava Durumu Uygulaması")
window.geometry("600x400")

# Arka plan resmi
image1 = ImageTk.PhotoImage(file="resim1.png")
label = tk.Label(window, image=image1)
label.place(relwidth=1, relheight=1)

# Şehir etiketi
sehiretiket = tk.Label(window, text="Şehir Adı:", font="Verdana 14 bold")
sehiretiket.place(x=260, y=20)

# Şehir giriş alanı
sehiradi = tk.Entry(window, font="Verdana 14 bold")
sehiradi.place(x=170, y=60,)

# Hava durumu sorgu butonu
sorgubutton = tk.Button(
    window, text="Hava Durumu Sorgula", command=get_weather)
sorgubutton.place(x=250, y=100)

# Hava durumu sonucunu gösterecek etiket
sonuc = tk.Label(window, text="", font="Verdana 9 bold")
sonuc.place(x=250, y=140)

window.mainloop()
