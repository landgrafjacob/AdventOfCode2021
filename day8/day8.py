answer = 0

# Dictionary for finding numbers with unique number of segements. Two segments means a one, four segments a four, three segments a seven, and seven segments an eight.
unique_char_dict = {2:1, 4:4, 3:7, 7:8}


# Dictionary used to record how many segments the remaining numbers share with 1,4,7,8. For example, 0 shares 2,3,3, and 6 segments with 1,4,7,8, respectively. 
intersect_dict = dict()
intersect_dict[(2,3,3,6)] = 0
intersect_dict[(1,2,2,5)] = 2
intersect_dict[(2,3,3,5)] = 3
intersect_dict[(1,3,2,5)] = 5
intersect_dict[(1,3,2,6)] = 6
intersect_dict[(2,4,3,6)] = 9

# Calculate the number of characters in common between two strings
def intersect(first, second):
  return len([c for c in first if c in second])

with open('input.txt', 'r') as in_file:
  for line in in_file.readlines():
    # Process line into a list of words representing each digit
    in_out = line.strip().split('|')
    [inp, outp] = [in_out[0].strip().split(' '), in_out[1].strip().split(' ')]
    line_list = inp + outp

    # Initialize decode list, whose entry at index i is the string (alphabetized) representing the digit i. 
    decode_list = 10 * ['']

    # Find 1,4,7,8
    for word in line_list:
      sorted_word = ''.join(sorted(word))
      # If the word has one of the unique lengths, add it to the decode list
      if len(word) in unique_char_dict.keys():
        decode_list[unique_char_dict[len(word)]] = sorted_word
    
    # Find rest of numbers
    for word in line_list:
      if len(word) in [5,6]:
        # Calculate intersections with 1,4,7,8
        intersect_tuple = tuple()
        for i in [1,4,7,8]:
          intersect_tuple = intersect_tuple + (intersect(word, decode_list[i]), )

        # Use intersect_dict to find the digit and enter into decode_list
        decode_list[intersect_dict[intersect_tuple]] = ''.join(sorted(word))

    # Decode the output using decode_list
    output_string = ''
    for word in outp:
      output_string += str(decode_list.index(''.join(sorted(word))))

    # Add output to running total 
    answer += int(output_string)

print(answer)


