# for 변수 in 리스트:
#   실행한 명령

# 1. for 기본 구조
pokemons = ['피카츄', '파이리', '꼬북이']
for pokemon in pokemons:
  print(pokemon)

# 2. 문자열 반복하기
for letter in '잠만보':
  print(letter)

# 3. 들여쓰기에 대한 이해
for pokemon in pokemons:
  print(pokemon)
print(pokemons)

for pokemon in pokemons:
  print(pokemon)
  print(pokemons)

# 4. 순서열 만들기
for num in range(3):
  print(f"피카츄 {num}마리")

# 5. 내용 바꾸기
for num in range(3):
  pokemons[num] = "이브이"
print(pokemons)

print(num) # range 종료시 매개변수 값