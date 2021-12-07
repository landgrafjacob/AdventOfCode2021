from os import stat
with open('input.txt', 'r') as in_file:
  pos_list = list(map(int,in_file.readline().strip().split(',')))

min_pos = min(pos_list)
max_pos = max(pos_list)
min_fuel = None

for pos in range(min_pos, max_pos + 1):
  total_fuel = 0
  for crab in pos_list:
    diff = abs(crab-pos)
    total_fuel += diff * (diff + 1) / 2.0

  if not min_fuel or total_fuel <= min_fuel:
    min_fuel = total_fuel
    minimizing_pos = pos


  

print(min_fuel)