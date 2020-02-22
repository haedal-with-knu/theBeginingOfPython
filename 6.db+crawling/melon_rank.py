# 이 코드도 왜 안돌아가냐 ㅠㅠ 조금만 고치면 작동할듯
import requests
import bs4
import csv

headers ={
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'
}

response = requests.get('https://www.melon.com/chart/index.htm', headers=headers).text
#mobile_response = requests.get('https://m.app.melon.com/index.htm', headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')
songs = soup.select('#lst50')
with open('melon_rank.csv', 'w', encoding='utf-8') as f:
  for song in songs:
    rank = song.select_one('td:nth-child(2) > div > span.rank').text
    title = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = song.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    f.write(f'{rank}위,{title},{artist}\n')