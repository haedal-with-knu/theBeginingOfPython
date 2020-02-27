import requests # pip install requests
import datetime
import json

data = requests.get('https://www.naver.com/srchrank?frm=main&ag=all&gr=1&ma=-2&si=0&en=0&sp=0').text
data = json.loads(data)

ranks = data['data']

now = datetime.datetime.now()

with open('naver_rank.txt', 'w', encoding='utf-8') as f:
  f.write(f'{now} 기준 네이버 검색어 순위\n')
  for i, rank in enumerate(ranks): # [(0, 'a'), (1, 'b'), ...]
    f.write(f'{i+1}. {rank["keyword"]}\n')
