# import packages requests dan BeautifulSoup
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.republika.co.id")

# extract konten menjadi objek BeautifulSoup
obj = BeautifulSoup(page.text, 'html.parser')

print ('Menampilkan objek html')
print ('========================')
print (obj)

print ('\nMenampilkan title browser dengan tag')
print ('=======================================')
print (obj.title)

print ('\nMenampilkan title browser tanpa tag')
print ('=======================================')
print (obj.title.text)

print ('\nMenampilkan semua tag h2')
print ('===========================')
print (obj.find_all('h2'))

print ('\nMenampilkan headline berdasarkan div class')
print ('=============================================')
print (obj.find_all('div',class_='bungkus_txt_headline_center'))

print ('\nMenampilkan semua teks headline')
print ('===================================')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
	print(headline.find('h2').text)

print ('\nMenyimpan headline pada file text')
print ('=====================================')
f=open('D:\\Kuliah\\Semester 2\\Proyek 1\\Pertemuan 7\\Scraping\\headline.txt','w')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
	f.write(headline.find('h2').text)
	f.write('\n')
f.close()


import json
# deklarasi list kosong
data=[]
# lokasi file json
f=open('D:\\Kuliah\\Semester 2\\Proyek 1\\Pertemuan 7\\Scraping\\headline.json','w')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
	# append headline ke variabel data
	data.append({"judul":headline.find('h2').text})
# dump list dictionary menjadi json
jdumps=json.dumps(data)
f.writelines(jdumps)
f.close()

from datetime import datetime
now = datetime.now()
tanggal = now.strftime("%d %B %Y %H:%M:%S")

# deklarasi list kosong
dataTerkini=[]
# lokasi file json
f=open('D:\\Kuliah\\Semester 2\\Proyek 1\\Pertemuan 7\\Scraping\\dataTerkini.json','w')
for terkini in obj.find_all('div',class_='teaser_conten1_center'):
	# append headline ke variabel data
	dataTerkini.append({"judul":terkini.find('h2').text,"kategori":terkini.find('h1').text,"waktu_publish":terkini.find('div',class_='date').text,"waktu_scraping":tanggal})
# dump list dictionary menjadi json
jdumps=json.dumps(dataTerkini)
f.writelines(jdumps)
f.close()
