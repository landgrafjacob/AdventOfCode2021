in_file = open('input.txt', 'r')

h_pos = 0
depth = 0
aim = 0

for line in in_file.readlines():
  instruction = line.strip().split()
  
  if instruction[0] == 'forward':
    h_pos += int(instruction[1])
    depth += int(instruction[1]) * aim
  elif instruction[0] == 'down':
    aim += int(instruction[1])
  else:
    aim -= int(instruction[1])

print(h_pos, depth, h_pos * depth)