#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from lxml import html
import sys
import json
proxyku = {
        'https':'https://icams:PASSWORD@proxy.bpsbali.id:3128/'
        }

headerku = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
        }
#working with ajustment
URL0 = 'https://infocorona.baliprov.go.id' 
#working
URL1 = 'https://infocorona.baliprov.go.id/API/good_api_manual.php' 
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
print("Data diperbaharui pada tanggal: ",tanggal[3],tanggal[4],tanggal[5])

filename = 'positif.json'
with open(filename, 'w') as f1:
    json.dump(positif_corona[0], f1, ensure_ascii=False)
filename = 'perawatan.json'
with open(filename,'w') as f2:
    json.dump(perawatan_corona[0],f2,ensure_ascii=False)
c_positif = open('covid.txt','w')
c_positif.write(positif_corona[0] + "\n")
c_positif.write(perawatan_corona[0])
c_positif.close()
print("Done")

html_head = """
<html><head><title>covid19</title></head>
<body>
"""
html_foot = """
</body>
</html>
"""
with open("corona.html", "w") as file:
    file.write(html_head)
    file.write("\n")
    file.write("Jumlah Kasus Positif Korono: ") 
    file.write(+ positif_corona[0])
    file.write("<br>")
    file.write("Jumlah pasien dalam perawatan :")
    file.write(perawatan_corona[0])
    file.write("<br>")
    file.write("Jumlah pasien sudah sembuh : ")
    file.write(meninggal[0])
    file.write("<br>")
    file.write("Data diperbaharui tanggal :")
    file.write(tanggal[3])
    file.write(tanggal[4])
    file.write(tanggal[5])
    file.write("<br>")
    file.write(html_foot)
    file.close()

with open("index.html", "w") as file:
    file.write(html_head)
    file.write("<a href=\"index.html\">back to index</a>")
    file.write("<br>")
    file.write("<a href=\"corona.html\">Info Corona Bali</a>")
    file.write(html_foot)
    file.close()