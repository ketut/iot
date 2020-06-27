#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from lxml import html
import sys
import json

headerku = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
        }

#working
URL2 = 'https://infocorona.baliprov.go.id/API/good_api_lagi.php'
r = requests.post(URL2, headers=headerku)
soup = BeautifulSoup(r.text,'lxml')

#kasus positif
t7 = soup.find_all('div')[7]
t71 = t7.find_all('div')[1]
positif_corona = t71.find('h3').text.split()
#perawatan
t11 = soup.find_all('div')[11]
perawatan_corona = t11.find('h3').text
perawatan_corona = perawatan_corona.split()

#Pasien Sembuh
t15 = soup.find_all('div')[15]
sembuh_corona = t15.find('h3').text
sembuh_corona = sembuh_corona.split()

#pasien meninggal
t19 = soup.find_all('div')[19]
meninggal = t19.find('h3').text
meninggal = meninggal.split()

tanggal = soup.find('p').text.split()

print("Jumlah positif korona terkonfirmasi: " + positif_corona[0] + " Orang")
print("Jumlah pasien korona dalam perawatan: " + perawatan_corona[0]+ " Orang")
print("Jumlah pasien korona yang sembuh: " + sembuh_corona[0]+ " Orang")
print("Jumlah pasien korona yang meninggal: "+ meninggal[0] + " Orang")
print("Data diperbaharui pada tanggal: {} {} {}".format(tanggal[3],tanggal[4],tanggal[5]))

tanggal = str(tanggal[3])+" "+str(tanggal[4])+" "+str(tanggal[5])

html_head = """
<html><head><title>covid19</title></head>
<body>
"""
html_foot = """
</body>
</html>
"""
with open("public/corona.html", "w") as file:
    file.write(html_head)
    file.write("\n")
    file.write("<a href=\"index.html\">back to index</a>")
    file.write("<br">
    file.write("Perkembangan Kasus Penyebaran COVID-19 di Provinsi Bali")
    file.write("<br>")
    file.write("Jumlah kasus terkonfirmasi positif korona: ") 
    file.write(positif_corona[0])
    file.write("<br>")
    file.write("Jumlah pasien dalam perawatan: ")
    file.write(perawatan_corona[0])
    file.write("<br>")
    file.write("Jumlah pasien sembuh: ")
    file.write(sembuh_corona[0])
    file.write("<br>")
    file.write("Jumlah korban meninggal: ")
    file.write(meninggal[0])
    file.write("<br>")
    file.write("Data diperbaharui tanggal: ")
    file.write(tanggal)
    file.write("<br>")
    file.write("<br>")
    file.write("Sumber: https://infocorona.baliprov.go.id")
    file.write(html_foot)
    file.close()
    print("corona.html writed")

with open("public/index.html", "w") as file:
    file.write(html_head)
    file.write("<a href=\"corona.html\">Info Corona Bali</a>")
    file.write(html_foot)
    file.close()
    print("index.html writed")
      

data = {'infected': positif_corona[0],'being treated': perawatan_corona[0],'recovered':sembuh_corona[0], 'fatal':meninggal[0],'tanggal':tanggal}

with open('public/api/v1/covid_bali.json', 'w') as outfile:
    json.dump(data, outfile)
print("JSON created")
print("Everything must be OK now")
