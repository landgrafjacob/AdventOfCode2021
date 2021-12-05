
def check_intersect(line, x_val, y_val):
  if x_val == line[0][0] and (line[0][1] <= y_val <= line[1][1] or line[1][1] <= y_val <= line[0][1]):
    return True

  elif y_val == line[0][1] and (line[0][0] <= x_val <= line[1][0] or line[1][0] <= x_val <= line[0][0]):
    return True

  return False


def insert_or_increment(d, key):
  if key in d:
    d[key] += 1
  else:
    d[key] = 1

intersect_dict = dict()

hor_vert_lines = []
max_x = 0
max_y = 0
with open('test.txt', 'r') as in_file:
  for line in in_file.readlines():
    string_list = line.strip().split(' -> ')
    start = list(map(int,string_list[0].split(',')))
    end = list(map(int,string_list[1].split(',')))
    max_x = max(max_x, start[0], end[0])
    max_y = max(max_y, start[1], end[1])

    if start[0] == end[0]:
      if start[1] <= end[1]:
        for i in range(start[1], end[1] + 1):
          insert_or_increment(intersect_dict, (start[0], i))

      else:
        for i in range(end[1], start[1] + 1):
          insert_or_increment(intersect_dict, (start[0], i))

    elif start[1] == end[1]:
      if start[0] <= end[0]:
        for i in range(start[0], end[0] + 1):
          insert_or_increment(intersect_dict, (i, start[1]))

      else:
        for i in range(end[0], start[0] + 1):
          insert_or_increment(intersect_dict, (i, start[1]))

    elif (end[1]-start[1]) == (end[0]-start[0]):
      if end[0] >= start[0]:
        for i in range(end[0]-start[0] + 1):
          insert_or_increment(intersect_dict, (start[0]+i, start[1]+i))

      else:
        for i in range(start[0] - end[0] + 1):
          insert_or_increment(intersect_dict, (end[0]+i, end[1]+i))

    elif (end[1]-start[1]) == -1*(end[0]-start[0]):
      if end[0] >= start[0]:
        for i in range(end[0]-start[0] + 1):
          insert_or_increment(intersect_dict, (start[0]+i, start[1]-i))

      else:
        for i in range(start[0] - end[0] + 1):
          insert_or_increment(intersect_dict, (end[0]+i, end[1]-i))


num_bad_points = 0
for point, ints in intersect_dict.items():
  if ints > 1:
    num_bad_points += 1

print(num_bad_points)






