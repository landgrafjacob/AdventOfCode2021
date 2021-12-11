
# Dictionary connecting opening brackets with closing brackets
bracket_dict = {'{': '}', '(': ')', '<': '>', '[': ']'}

# Dictionary storing the error scores of different closing brackets in corrupt lines
score_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}

#Dictionary storing error scores in incomplete lines 
unclosed_dict = {'(': 1, '[': 2, '{': 3, '<': 4}

error_score = 0
incomplete_list = []

with open('input.txt', 'r') as in_file:
    for line in in_file:
        # Create stack keeping track of opening brackets
        bracket_stack = []

        # Create flag for corrupt line
        corrupt = False

        # Loop through characters in line
        for char in line.strip():
            # If character is an opening bracket, put it on the stack
            if char in bracket_dict.keys():
                bracket_stack.append(char)

            # Otherwise, check that it matches the last opening bracket
            else:
                last_opened = bracket_stack.pop()

                #If it does not, then compute the error score, set the corrupt flag, and stop looping through line
                if bracket_dict[last_opened] != char:
                    error_score += score_dict[char]
                    corrupt = True
                    break

        # Incomplete line score 
        score = 0

        # If the line is not corrupt (and thus incomplete), then loop through the 
        # opening brackets that weren't closed and compute the incomplete line score
        while not corrupt and len(bracket_stack) > 0:
            last_opened = bracket_stack.pop()
            score = (score * 5) + unclosed_dict[last_opened]

        # If the score is positive, append it to the incomplete line score list
        if score > 0:
            incomplete_list.append(score)

    # Sort the incomplete line score list
    incomplete_list.sort()

    # Print the middle entry
    print(incomplete_list[(len(incomplete_list)-1)/2])


                    
