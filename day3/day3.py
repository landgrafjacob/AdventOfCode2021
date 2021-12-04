
# PART 1
# in_file = open('input.txt', 'r')

# count = [0] * 12
# length = 0

# gamma_string = ''
# epsilon_string = ''

# for index, line in enumerate(in_file.readlines()):
#   length = index + 1

#   for pos in range(len(line)):
#     if line[pos] == '1':
#       count[pos] += 1


# for c in count:
#   if c > length/2:
#     gamma_string += '1'
#     epsilon_string += '0'
#   else:
#     gamma_string += '0'
#     epsilon_string += '1'

# gamma = int(gamma_string, 2)
# epsilon = int(epsilon_string, 2)

# print(gamma * epsilon)


# in_file.close()

in_file = open('input.txt', 'r')


def recursive_filter(input_list, pos, most_common):
  length = len(input_list)
  if length == 1:
    return int(input_list[0],2)

  else:
    count = 0
    for line in input_list:
      if line[pos] == '1':
        count += 1
    
    if count >= length/2:
      common_bit = '1'
    else:
      common_bit = '0'

    new_list = []
    for line in input_list:
      if most_common:
        if line[pos] == common_bit:
          new_list.append(line)
      else:
        if line[pos] != common_bit:
          new_list.append(line)

    return recursive_filter(new_list, pos+1, most_common)


line_list = in_file.readlines()

print(recursive_filter(line_list,0,True) * recursive_filter(line_list,0,False))



in_file.close()