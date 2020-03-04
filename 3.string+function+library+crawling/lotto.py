# "있는 바뉘를 다시 만들지 말아라"g
# 모듈 = 비슷한 기능의 함수를 모아둔 파일
# import -> 모듈을 불러오는 키워드

# 로또 번호 뽑아보자
import random

numbers = range(1, 46)

lotto = random.sample(numbers, 6)
print(lotto)
print(f'오늘의 행운의 로또는 {sorted(lotto)} 입나다')