
# Create a dictionary which will store the rules for insertion, 
# in the form {pair: [two resulting pairs]}. 
insertion_dict = dict()

# Create a dictionary storing the number of times each 
# pair appears in the template {'pair': count}
pair_count_dict = dict()


with open('input.txt') as in_file:
  # Get template by reading first line of input
  template = in_file.readline().strip()
  # Skip over blank line
  in_file.readline()

  # Loop through the rest of the file, filling the insertion rules into insertion_dict
  for line in in_file:
    rule_list = line.strip().split(' -> ')
    insertion_dict[rule_list[0]] = [rule_list[0][0] + rule_list[1], rule_list[1] + rule_list[0][1]]

# Function which increments a value by count if the key is in the dictionary, 
# or adds it otherwise
def increment_or_add(key, count, d):
  if key in d.keys():
    d[key] += count
  else:
    d[key] = count

# Initialize pair_count_dict with the pairs from the beginning template
for i in range(len(template) - 1):
  increment_or_add(template[i:i+2], 1, pair_count_dict)

# Function which performs a step given the current pair_count_dict, returns new pair_count_dict
def perform_step(pair_count_dict):
  # Create new pair counting dictionary
  new_pair_count = dict()

  # For each pair in the current pair_count_dict, add the two resulting pairs to new_pair_count
  for pair, count in pair_count_dict.items():
    for new_pair in insertion_dict[pair]:
      increment_or_add(new_pair, count, new_pair_count)

  return new_pair_count


# Count the number of times each letter appears in template given a pair_count_dict, 
# and the first/last letters of the template. Returns dictionary in form {letter: count}
def count_letters(pair_count_dict, first, last):
  # Create dictionary
  letter_dict = dict()

  # Loop through pairs
  for pair in pair_count_dict.keys():
    # For both letters in the pair, increment the count in letter_dict by the count of the pair
    for letter in pair:
      increment_or_add(letter, pair_count_dict[pair], letter_dict)

  # We have now double-counted all letters, except the first and last, which have only been counted once
  letter_dict[first] += 1
  letter_dict[last] += 1


  # Now that all letters are double-counted, divide each count by 2
  for letter in letter_dict.keys():
    letter_dict[letter] = letter_dict[letter] // 2

  

  return letter_dict

  

# Perform 40 steps
for _ in range(40):
   pair_count_dict = perform_step(pair_count_dict)

# Count the letters from the resulting pair_count_dict
letter_dict = count_letters(pair_count_dict, template[0], template[-1])

# Print desired result
print(max(letter_dict.values()) - min(letter_dict.values()))


