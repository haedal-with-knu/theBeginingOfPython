# 1. string split
with open('lunch.csv', 'r', encoding='utf-8') as f:
  lines = f.readlines()
  for line in lines:
    # '종이밥,053-816-5300\n'
    # '종이밥,053-816-5300'
    # ['종이밥', '053-816-5300']
    print(line.strip().split(','))

# 2. csv
import csv
with open('lunch.csv', 'r', encoding='utf-8') as f:
  items = csv.reader(f) # [(..., ...),(...),(...)]
  for item in items:
    print(item)