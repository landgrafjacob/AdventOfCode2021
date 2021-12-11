risk = 0


height_list = []
with open('input.txt') as in_file:
    for line in in_file:
        height_list.append(list(map(int, list(line.strip()))))

num_rows = len(height_list)
num_cols = len(height_list[0])

# Function to check if given coordinates are a local minimum
def is_min(row, col):
    if row > 0 and height_list[row-1][col] <= height_list[row][col]:
        return False

    if row < num_rows-1 and height_list[row+1][col] <= height_list[row][col]:
        return False

    if col > 0 and height_list[row][col-1] <= height_list[row][col]:
        return False

    if col < num_cols-1 and height_list[row][col+1] < height_list[row][col]:
        return False

    return True


# Part A
for i, row in enumerate(height_list):
    for j, col in enumerate(row):
        if is_min(i,j):
            risk += height_list[i][j] + 1

print(risk)

# Function for merging two basins together as we are building them
def merge_basins(first, second, new_basin):
    for i in range(len(basin_list)):
        for j in range(len(basin_list[i])):
            if basin_list[i][j] in [first, second]:
                basin_list[i][j] = new_basin

def insert_or_increment(val, dictionary):
    if val in dictionary.keys():
        dictionary[val] += 1
    else:
        dictionary[val] = 1


# Basin list will be a 2D array of the same size as height_list, whose 
# entries will be numbers corresponding to the basin in which that coordinate 
# belongs (e.g. a 1 in basin_list[i][j] means the coordinate (i,j) lies in basin 1).
basin_list = []
current_basin = 1
for i in range(num_rows):
    new_row = []
    for j in range(num_cols):
        # If the coordinate is on a ridge, it does not belong to a basin (represented by a -1)
        if height_list[i][j] == 9:
            new_row.append(-1)
        # At (1,1), start the first basin
        elif i == 0 and j == 0:
            new_row.append(1)
        # In the first row, either continue the basin from the left, or start a new basin if the coordinate to the left was a ridge
        elif i == 0:
            if height_list[i][j-1] != 9:
                new_row.append(new_row[j-1])
            else:
                current_basin += 1
                new_row.append(current_basin)
        # In the first column, either continue the basin from above, or start new basin
        elif j == 0:
            if height_list[i-1][j] != 9:
                new_row.append(basin_list[i-1][j])
            else:
                current_basin += 1
                new_row.append(current_basin)

        # Consider when coordinate is not first in row or column 
        else:
            # If there were ridges above and to the left, start new basin
            if height_list[i-1][j] == 9 and height_list[i][j-1] == 9:
                current_basin += 1
                new_row.append(current_basin)
            # If there was only a ridge above, continue the basin from the left
            elif height_list[i-1][j] == 9:
                new_row.append(new_row[-1])
            # If there was only a ridge to the left, continue the basin from above
            elif height_list[i][j-1] == 9:
                new_row.append(basin_list[i-1][j])

            # Consider when coordinates above and to the left are not ridges 
            else:
                # If the above and left coordinates are part of the same basin, continue that basin
                if new_row[j-1] == basin_list[i-1][j]:
                    new_row.append(new_row[j-1])
                # Otherwise, merge the two different basins into a new basin
                else:
                    current_basin += 1
                    # merge_basins loops through basin_list and changes both basins into the new basin
                    merge_basins(basin_list[i-1][j], new_row[j-1], current_basin)
                    # Loop through new_row merging these basins as well
                    for k in range(len(new_row)):
                        if new_row[k] == basin_list[i-1][j] or new_row[k] == new_row[j-1]:
                            new_row[k] = current_basin
                    new_row.append(current_basin)
    basin_list.append(new_row)

# Dictionary to record the sizes of each basin
basin_dict = dict()

# Loop through basin_list to fill basin_dict
for row in basin_list:
    for entry in row:
        if entry != -1:
            insert_or_increment(entry, basin_dict)


# Get sorted basin sizes
sorted_basin_sizes = sorted(basin_dict.values(), reverse=True)
answer = 1
# Multiply largest three
for i in range(3):
    answer *= sorted_basin_sizes[i]
print(answer)




            
        


