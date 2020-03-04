# 1. read file
with open('haedal.txt', 'r') as f:
  lines = f.readlines() # list

# 2. reverse
lines.reverse()

# 3. write files
with open('haedal.txt', 'w') as f:
  f.writelines(lines)