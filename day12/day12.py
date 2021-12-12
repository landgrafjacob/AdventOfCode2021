
# Function to add adjacencies to a dictionary di. di has format {cave: [adjacent, caves]}
def add_to_dict(first, second, di):
    if first in di.keys():
        di[first].append(second)
    else:
        di[first] = [second]

    if second in di.keys():
        di[second].append(first)
    else:
        di[second] = [first]


# Function which return True when a lowercase word is repeated in a list
def small_repeated(cave_list):
    char_dict = dict()
    for char in cave_list:
        if char.islower():
            if char in char_dict.keys():
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    if max(char_dict.values()) > 1:
        return True
    else:
        return False

# Recursive function to count paths. 
# The inputs are the current starting node, 
# the adjacency dictionary, the segment of the path already constructed, 
# and a boolean saying whether a small cave can be repeated at this point
def recursive_paths(start, adj, path, can_repeat):
    # If we're at the end cave, count the path
    if start == 'end':
        return 1

    # Otherwise we will count paths to the end starting at all adjacent caves, and add them all up
    num_paths = 0

    # Loop over neighboring caves
    for cave in adj[start]:
        # If the cave is an uppercase letter, we can move there freely
        if cave.isupper():
            num_paths += recursive_paths(cave, adj, path+[cave], can_repeat)
        
        # If the cave is lowercase, we need to consider the number of times that cave has been visited
        else:
            # We may not go back to the starting cave
            if cave != 'start':

                # If we have not visited the cave at all, we can move there freely
                if path.count(cave) == 0:
                    num_paths += recursive_paths(cave, adj, path+[cave], can_repeat)

                # If the cave has been visied once and we still 
                # have the ability to visit a lowercase cave twice, 
                # then go to this cave and declare that we may no 
                # longer visit a lowercase cave twice.
                elif path.count(cave) == 1 and can_repeat:
                    num_paths += recursive_paths(cave, adj, path+[cave], False)

    return num_paths



# Create dictionary which will store adjacency between caves in the form {cave: [adjacent caves]}
adjacency_dict = dict()

with open('input.txt', 'r') as in_file:
    # Loop through lines of input filling adjacency_dict
    for line in in_file:
        adjacent_caves = line.strip().split('-')
        add_to_dict(adjacent_caves[0], adjacent_caves[1], adjacency_dict)

print(recursive_paths('start', adjacency_dict, ['start'], True))


