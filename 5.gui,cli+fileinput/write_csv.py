lunch = {
  '종이밥': '053-816-5300',
  '맘스터치': '053-955-4242',
  '돈가스백작': '053-955-0601'
}
# 1. f-string
with open('lunch.csv', 'w', encoding='utf-8') as f:
  for item in lunch.items(): # [('종이밥','053-...), ...]
    f.write(f'{item[0]},{item[1]}\n')

# 2. join()
with open('lunch.csv', 'w', encoding='utf-8') as f:
  for item in lunch.items(): # [('종이밥','053-...), ...]
    f.write(','.join(item)+'\n')
    # ','.join(('종이밥','053-...), ('맘스터치', '053-...'))
    # => 종이밥,053-816-5300,맘스터치,...

# 3.csv
import csv
with open('lunch.csv', 'w', encoding='utf-8') as f:
  csv_writer = csv.writer(f)
  for item in lunch.items():
    csv_writer.writerow(item)