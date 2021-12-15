

# Variables to store the set of dots (where a dot is represented by a tuple (row, column)), 
# and the list of folds (stored as lists ['x'/'y', coordinate])
dots = set()
folds = []


# Initialize dots and folds 
with open('input.txt', 'r') as in_file:
  # Boolean to detect when we've hit the folds section
  at_folds = False


  for line in in_file:
    # If the line is empty, move to the fold section
    if line == '\n':
      at_folds = True
    # If we've hit the folds section, append the next fold to folds
    elif at_folds:
      info = line.strip().split()
      axis = info[-1][0]
      coordinate = info[-1][2:]
      folds.append([axis, int(coordinate)])
    # If we have not hit the folds section, add the next dot
    else:
      dot_coords = tuple(map(int, line.strip().split(',')))
      dots.add(dot_coords)

print(folds)

# Function to perform a fold on a set of dots. Does not change dots. 
def perform_fold(dots, fold):
  new_dots = set()
  #If the axis of folding is vertical 
  if fold[0] == 'x':

    # Iterate through dots
    for dot in dots:
      # Check if each dot has x-coordinate larger than the coordinate of the folding axis
      if dot[0] > fold[1]:
        # If so, calculate the x-coordinate it will be folded onto, and add that dot
        new_dots.add((2*fold[1] - dot[0], dot[1]))
      else:
        # Otherwise, simply add the dots
        new_dots.add(dot)

  # Same process for horizontal folds
  elif fold[0] == 'y':
    for dot in dots:
      if dot[1] > fold[1]:
        new_dots.add((dot[0], 2*fold[1] - dot[1]))
      else:
        new_dots.add(dot)

  return new_dots


# Function to return a string output (as a list of strings) given a list of dots 
def dots_to_string(dots):
  x_max = 0
  y_max = 0
  # Calculate the largest x- and y-coordinate (display size)
  for dot in dots:
    x_max = max(x_max, dot[0])
    y_max = max(y_max, dot[1])

  # Create a display and fill it with '.'
  char_list = (y_max + 1) * [ (x_max + 1) * '.']

  # Fill in a '#' for all the dots
  for dot in dots:
    char_list[dot[1]] = char_list[dot[1]][:dot[0]] + '#' + char_list[dot[1]][dot[0] + 1:]

  return char_list


# Perform all the folds 
for fold in folds:
  dots = perform_fold(dots, fold)

# Print string
dot_str_list = dots_to_string(dots)
for row in dot_str_list:
  print(row)


