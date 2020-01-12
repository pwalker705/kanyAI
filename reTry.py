import lyricsgenius
from bs4 import BeautifulSoup
import re
import requests


song = 'https://genius.com/Twista-kanye-west-and-jamie-foxx-slow-jamz-lyrics'
#song = 'https://genius.com/Kanye-west-breathe-in-breathe-out-lyrics'
title = re.search('https://genius.com/(.*?)-lyrics', song).group(1)

print(title)