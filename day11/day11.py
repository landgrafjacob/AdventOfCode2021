# Given the size m x n of an array and coordinates (i,j) of that array, 
# returns all smaller adjacent coordinates (sorted lexicographically).
# e.g. adjacent_smaller_entries(3, 4, 10, 10) = [[2,3], [2,4], [2,5], [3,3]]
def adjacent_smaller_entries(i, j, m, n):
    adj_coords = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1]]

    return filter(lambda x: 0 <= x[0] and x[0] <= m-1 and 0 <= x[1] and x[1] <= n-1, adj_coords)

    
PULSES = 0

# A class modeling the individual octopi
class Octopus:

    # Creates a new octopus with given energy level
    def __init__(self, energy):
        self.energy = energy
        self.neighbors = []
        self.pulsed = False

    # Makes this octopus and another octopus neighbors
    def make_neighbors(self, other):
        self.neighbors.append(other)
        other.neighbors.append(self)

    # Resets the octopus after a step. If the octopus pulsed, set its energy back to 0. 
    # Also returns True if the octopus pulsed this step
    def reset(self):
        did_pulse = self.pulsed
        if self.pulsed:
            self.energy = 0
        self.pulsed = False
        return did_pulse

    # Increases the energy level by one. If the energy becomes large enough, pulse
    def increase(self):
        self.energy += 1
        if self.energy > 9 and not self.pulsed:
            self.pulsed = True
            self.pulse()

    # Increments all neighbor octopus's energy level by 1.
    def pulse(self):
        global PULSES
        PULSES += 1
        for neighbor in self.neighbors:
            neighbor.increase()

# Open file and make a 2d array of energy levels (as ints)
with open('input.txt', 'r') as in_file:
    energy_array = map(lambda x: map(int,list(x.strip())), in_file.readlines())

# Turn the array of energy levels into an array of octopi
octo_array = map(lambda x: map(Octopus, x), energy_array)


num_rows = len(octo_array)
num_cols = len(octo_array[0])


# Loop through the octopus array making all neighbor relationships
for i in range(num_rows):
    for j in range(num_cols):
        neighbor_ind = adjacent_smaller_entries(i,j,num_rows,num_cols)
        for coord in neighbor_ind:
            octo_array[i][j].make_neighbors(octo_array[coord[0]][coord[1]])

num_steps = 1
# Perform steps until all octopi pulse on the same step
while True:
    # Begin by increasing all octopi (this handles pulsing as well)
    for row in octo_array:
        for octopus in row:
            octopus.increase()

    # Loop through and reset the octopi, while checking if any octopus did not pusle
    all_pulsed = True

    for row in octo_array:
        for octopus in row:
            # If an octopus did not pulse, set all_pulsed flag to False
            if not octopus.reset():
                all_pulsed = False

    # If all octopi pulsed, break and print the number of steps 
    if all_pulsed:
        print(num_steps)
        break

    num_steps += 1



            

