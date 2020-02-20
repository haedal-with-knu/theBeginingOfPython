# String Interpolation
trainer = "지우"
challenger = f'{a}'

# 1. 옛날 방식
f'%s %s' % ('피카츄', '파이리') # => '피카츄 파이리'

# 2. pyformat
'{} {}'.format('피카츄', '파이리') #=> '피카츄 파이리'

# 3. f-string
first, second = '피카츄', '파이리'
f'{first} {second}' # => '피카츄 파이리'

# example
enemy = '로켓단'
pokemon = "냐옹이"

print('{0}이 나타났다. {1}를 꺼냈다'.format(enemy, pokemon))
print(f'{pokemon}다해')