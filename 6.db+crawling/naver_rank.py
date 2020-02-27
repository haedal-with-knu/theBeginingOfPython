import requests # pip install requests
import bs4 # pip install bs4
import datetime
import json

data = requests.get('https://www.naver.com/srchrank?frm=main&ag=all&gr=1&ma=-2&si=0&en=0&sp=0').text
data = json.loads(data)
#soup = bs4.BeautifulSoup(html, 'html.parser')
#print(soup)

# 이렇게 실시간 검색어 긁어오면 되는데 잘 안되네요 ㅠㅠ 확인 부탁합니다
# ranks = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k')
# ranks = soup.select("#NM_RTK_VIEW_list_wrap .ah_item .ah_a")
ranks = data['data']
print(ranks)


now = datetime.datetime.now()

with open('naver_rank.txt', 'w', encoding='utf-8') as f:
  f.write(f'{now} 기준 네이버 검색어 순위\n')
  for i, rank in enumerate(ranks): # [(0, 'a'), (1, 'b'), ...]
    f.write(f'{i+1}. {rank["keyword"]}\n')
