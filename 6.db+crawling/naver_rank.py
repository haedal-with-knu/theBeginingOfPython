import requests # pip install requests
import bs4 # pip install bs4
import datetime

html = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(html, 'html.parser')


# 이렇게 실시간 검색어 긁어오면 되는데 잘 안되네요 ㅠㅠ 확인 부탁합니다
# ranks = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k')
# ranks = soup.select("#NM_RTK_VIEW_list_wrap .ah_item .ah_a")
ranks = soup.select("li.ah_item > a.ah_a > span.ah_k")


now = datetime.datetime.now()

with open('naver_rank.txt', 'w', encoding='utf-8') as f:
  f.write(f'{now} 기준 네이버 검색어 순위\n')
  for i, rank in enumerate(ranks): # [(0, 'a'), (1, 'b'), ...]
    f.write(f'{i+1}. {rank.text}\n')