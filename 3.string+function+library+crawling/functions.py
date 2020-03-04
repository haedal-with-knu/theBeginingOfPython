# 함수 = 반복되는 코드를 모아서 이름을 붙인 것, 코드묶음

# 함수의 종류
# 1.내장 함수는 파이썬에 포함된 함수
# 2.모듈은 비슷한 함수끼리 모아둔 파일
# 3.사용자 정의 함수는 직접 만들어 사용하는 함수

# def 함수_이름(인수):
#   실행할_명령
#   return 반환값

def gotcha():
  print("잡았다!")

gotcha()

# 매개변수 사용하는 함수
def add(num1, num2):
  return num1 + num2
print(add(1,1))

def add_mul(num1, num2):
  return num1 + num2, num1 * num2
print(add_mul(1,2))

# 100만번 이상 진행하면, 생각보다 편하다
def attack(name):
  print(name, "100만 볼트")
  print(name, "전광석화")
  print(name, "번개")

attack("피카츄")
attack("라이츄")
attack("피츄")

