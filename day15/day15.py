# https://adventofcode.com/2021/day/15

from queue import PriorityQueue

# Convert file into an array of integers
with open('input.txt', 'r') as in_file:
  risk_list = [[int(x) for x in y.strip()] for y in in_file.readlines()]


# Function which takes a array of integers and extends it as described in part 2 of the problem
def extend_risk_list(risk_list):
  original_height = len(risk_list)

  # Create the extended list variable
  extended_list = []

  # Loop through rows of original array
  for line in risk_list:
    # Start with original row
    new_row = line.copy()

    # Add on the same row with the entries incremented by 1,2,3,4, respectively. 
    for i in range(4):
      new_row.extend([(risk + i) % 9 + 1 for risk in line])

    # Add the long row to the extended array
    extended_list.append(new_row)

  # Loop through the extended rows 
  for i in range(4):
    # Make a new row where the entries have been incremented by 1,2,3, and 4
    for line_num in range(original_height):
      extended_list.append([(risk + i) % 9 + 1 for risk in extended_list[line_num]])

  return extended_list



# Function which takes the coordinates (i,j) in an m x n array and return a list of adjacent coordinates (horizontally and vertically)
def adjacent_entries(i, j, m, n):
    adj_coords = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]
    return filter(lambda x: 0 <= x[0] and x[0] <= m-1 and 0 <= x[1] and x[1] <= n-1, adj_coords)

# Function giving the taxicab distance between two coordinates first and second. Will be used as the priority value in our priority queue
def taxicab_dist(first, second):
  return abs(second[1] - first[1]) + abs(second[0] - first[0])


# Function which takes an array of risks, and return the total risk of the least risky path from the beginning to the end. 
# Uses A* pathfinding with the taxicab metric as the heuristic
def lowest_risk_path(risk_list):
  num_rows = len(risk_list)
  num_cols = len(risk_list[0])

  # Starting and ending coordinates
  start = (0,0)
  end = (num_rows-1, num_cols-1)

  # Create priority queue for unvisited nodes
  unvisited_queue = PriorityQueue()
  # Put starting node in queue
  unvisited_queue.put((0, start))

  # Initialize a dictionary whose keys are nodes, and the corresponding values are 
  # the node previously seen on the shortest path from the start node the key node
  came_from = {start: None}

  # Create dictionary whose keys are nodes, and the values are the 
  # smallest total risk along a path from start to that node
  tentative_risk = {start: 0}

  # While there are nodes in the unvisited node queue
  while not unvisited_queue.empty():
    # Pop a node off the queue
    pos = unvisited_queue.get()[1]

    # If the node is the end node, then we are done
    if pos == end:
      break

    
    else:
      # Otherwise, loop through the nodes neighbors
      for new_pos in adjacent_entries(pos[0], pos[1], num_rows, num_cols):
        # Calculate the total risk of a path to those neighbors through the current node
        new_risk = tentative_risk[pos] + risk_list[new_pos[0]][new_pos[1]]
        
        # If the neighbor is not where we came from previously, 
        # or the risk that we calculated is smaller than the 
        # risk we saw at the neighbor node before
        if new_pos not in came_from or new_risk < tentative_risk[new_pos]:

          # Update the risk dictionary with this new value
          tentative_risk[new_pos] = new_risk

          # Calculate the priority of this node, using the taxicab metric as a heuristic
          new_priority = new_risk + taxicab_dist(new_pos, end)

          # And put it on the queue
          unvisited_queue.put((new_priority, new_pos))

          # Record that we traveled to this neighbor through the current node
          came_from[new_pos] = pos

  # Return the total risk of a path from start to end
  return tentative_risk[end]


# Extend the initial list
ex_risk_list = extend_risk_list(risk_list)

# Find lowest-risk path and print result
print(lowest_risk_path(ex_risk_list))