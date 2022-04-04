from selenium import webdriver
import urllib.request
import json
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.celebritynetworth.com/list/top-100-richest-people-in-the-world/")

from datetime import datetime
now = datetime.now()
tanggal = now.strftime("%d %B %Y %H:%M:%S")

movielist = []
i = 1
j = 1
k = 1
for movie in driver.find_elements_by_class_name("top_profile"):
	print(movie.text.split("\n"))
	for thumb in movie.find_elements_by_class_name("thumb"):
		for img in movie.find_elements_by_tag_name("img"):
			print(img.get_attribute("src"))
			k = k+1
		urllib.request.urlretrieve(img.get_attribute("src"), str(k)+".png")
		j = j+1
	i = i+1
	# movielist.append(
	# 	{"Rank": movie.text.split("\n")[0],
	# 	"Title": movie.text.split(",")[1],
	# 	"Director": movie.text.split("\u")[2],
	# 	"Image": img.get_attribute("src")
	# 	}
	# )

hasil_scraping = open("hasilscraping.json", "w")
json.dump(movielist, hasil_scraping, indent = 6)
hasil_scraping.close()

driver.quit()