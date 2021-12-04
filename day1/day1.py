in_file = open('input2.txt', 'r')
num_of_increases = 0
num_of_decreases = 0
num_of_equalities = 0

input_list = list(map(int, in_file.readlines()))
list_length = len(input_list)


begin_pointer = 0
end_pointer = 3

while end_pointer < list_length:
  if input_list[end_pointer] > input_list[begin_pointer]:
    num_of_increases += 1
  elif input_list[end_pointer] < input_list[begin_pointer]:
    num_of_decreases += 1
  else:
    num_of_equalities += 1
  end_pointer += 1
  begin_pointer += 1


print(num_of_increases, num_of_decreases, num_of_equalities)
