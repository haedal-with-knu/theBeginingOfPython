# while = 조건 + 반복

# while 조건:
#   실행할_명령

# for와 while 비교하기
for num in range(3):
  print(f'잠만보가 {num}시간째 자는 중')

num = 0
while num < 3:
  print(f'이상해씨가 {num}일째 씨 뿌리는 중')
  num = num + 1
print("다 심었다!")

# 수수께끼
pokemon = ''
while pokemon != '잠만보':
  answer = input('지금 자고 있는 포켓몬은? ')
print('정답입니다')

# 넘어가기와 멈추기
print("while문 안에서 continue와 break를 사용하는 예시를 찾아봅시다")

# 무한반복
while True:
  print("여기 들어갈 예시를 만들어봅시다")