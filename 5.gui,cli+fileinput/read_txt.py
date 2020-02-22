# Read File

# 1. open files()
f = open('haedal.txt', 'r')
all_text = f.read()
print(all_text)
f.close()

# 2. with open()
with open('haedal.txt', 'r') as f:
  lines = f.readlines() # List
  for line in lines:
    print(line)