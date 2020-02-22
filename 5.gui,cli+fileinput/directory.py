# python3 폴더, 경로 다루기 : https://m.blog.naver.com/smilewhj/221079181059
# 파이썬 파일과 디렉토리 경로 : https://itmining.tistory.com/122


# 아래의 코드들은 IDLE, 파이썬 콘솔 창에서 입력해주세요

import os

# 현재 작업하고 있는 폴더 확인
os.getcwd()
# 현재 위치의 절대경로 확인
os.path.abspath('.')


# os.chdir("원하는 경로") # IDLE에서 사용하는 경우 사용 가능

# 현재 경로에 haedal 폴더 생성
os.makedirs('haedal') # 절대 경로도 사용 가능
# 현재 경로에서 haedal 폴더가 존재하는가?
os.path.exists('haedal')
# 해달 파일이 존재하는가?
os.path.isfile('haedal')
# 해달 폴더가 존재하는가?
os.path.isdir('haedal')

# 파일명이 포함된 경로에서 경로명 출력
os.path.dirname(os.getcwd())
# 파일명이 포함된 경로에서 파일명 출력
os.path.basename(os.getcwd())

# 현재 파일 크기를 확인
os.path.getsize(os.getcwd())
# 해달 폴더 크기 확인
os.path.getsize('haedal')



