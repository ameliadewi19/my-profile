from selenium import webdriver
import urllib.request
import json
import re
from selenium.common.exceptions import NoSuchElementException

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.flickchart.com/Charts.aspx?perpage=250")

from datetime import datetime
now = datetime.now()

movielist = []
i = 1
for movie in driver.find_elements_by_class_name("movieInfo"):
	print(movie.text.split("\n"))
	for img in movie.find_elements_by_tag_name("img"):
		print(img.get_attribute("src"))
	urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
	
	# rank
	rank = movie.find_element_by_class_name("movieRanking")
	print(rank.text)

	# title
	title = movie.find_element_by_css_selector("span[itemprop='name']")
	print(title.text)
	
	year = movie.find_element_by_class_name("chartsYear")
	print(year.text)

	g = movie.find_element_by_class_name('genre')
	print(g.text)
	genre = g.text.split("•")
	print(genre)

	d = movie.find_element_by_class_name('director')
	print(d.text)
	direct = d.text.split("•")
 
	# print(title)
		# title = t.text
	i = i+1
	movielist.append(
		{
			# "Title": judul.text.split("\n")[0]
			"Rank": rank.text,
			"Title": title.text,
			"Year": year.text,
			"Genre": g.text,
			"Director": direct[0],
			"Image": img.get_attribute("src"),
			"Time": now.strftime("%d %B %Y %H:%M:%S")
		}
	)

hasil_scraping = open("..\\hasilscraping.json", "w")
json.dump(movielist, hasil_scraping, indent = 6)
hasil_scraping.close()

driver.quit()