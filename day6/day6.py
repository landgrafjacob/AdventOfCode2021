fish_list = [0,0,0,0,0,0,0,0,0]

with open('input.txt', 'r') as in_file:
  for timer in in_file.readline().strip().split(','):
    fish_list[int(timer)] += 1



for _ in range(256):
  fish_list = fish_list[1:] + fish_list[:1]
  fish_list[6] += fish_list[8]

print(sum(fish_list))




