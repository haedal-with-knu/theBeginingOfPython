import bs4 #pip install bs4
import requests #pip install requests

headers ={
  'User-Agent': 'Not_Crawling X)'
}

response = requests.get('https://www.melon.com',headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')
songs = soup.select('.on.nth1 >.list_wrap.typeRealtime>ul>.rank_item')

with open('melon_rank.csv', 'w') as f:
  for song in songs:
    rank = song.select_one('div.rank_number > span.rank').text
    title = song.select_one('div.rank_cntt > div.rank_info > p.song > a').text
    artist = song.select_one('div.rank_cntt > div.rank_info > div.artist > div.ellipsis > a').text
    f.write(f'{rank}위,{title},{artist}\n')