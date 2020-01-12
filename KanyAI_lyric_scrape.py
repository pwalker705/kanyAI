#KanyAI 


import lyricsgenius
from bs4 import BeautifulSoup
import re
import requests
import time


#artist = genius.search_artist('Kanye West', max_songs = 3)

#artist.save_lyrics()





albums = ['https://genius.com/albums/Kanye-west/The-college-dropout',
'https://genius.com/albums/Kanye-west/Late-registration',
'https://genius.com/albums/Kanye-west/Graduation',
'https://genius.com/albums/Kanye-west/808s-heartbreak',
'https://genius.com/albums/Kanye-west/My-beautiful-dark-twisted-fantasy',
'https://genius.com/albums/Kanye-west/Yeezus',
'https://genius.com/albums/Kanye-west/The-life-of-pablo']

songs = []

for album in albums:
	url = album
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "html.parser")
	for link in soup.findAll('a', attrs={'href': re.compile("^https://.*.lyrics$")}):
		songs.append(link.get('href'))
#print(songs)

for song in songs:
	page = requests.get(song)
	soup = BeautifulSoup(page.text, "html.parser")
	lyrics = soup.find('div', class_="lyrics").get_text()

	title = re.search('https://genius.com/(.*?)-lyrics', song).group(1)

	f =  open("{}.txt".format(title),'w', encoding="utf-8")
	f.write(lyrics)
	
	time.sleep(.75)			



#url = 'https://genius.com/Kanye-west-we-dont-care-lyrics'
#page = requests.get(url)
#html = BeautifulSoup(page.text, "html.parser")

#lyrics = html.find("div", class_="lyrics").get_text()
#print(lyrics[:150])	



