     def move(my_list, direction):
    # Finds the index of the one in the list
    try:
        index_of_one = my_list.index(1)
    except ValueError:
        # Handle case where '1' is not in the list (optional, but robust)
        print("Error: The list does not contain a '1'.")
        return my_list
   
    # Move the one to the left or to the right
    if direction == 'right':
        # Check if '1' is already at the last index
        if index_of_one == len(my_list) - 1:
            return my_list # Cannot move right, return list unchanged
        else:
            # Move right: current position becomes 0, next position becomes 1
            my_list[index_of_one] = 0
            my_list[index_of_one + 1] = 1
           
    elif direction == 'left':
        # 🛑 CORRECTION: Add a check for the left boundary (index 0)
        if index_of_one == 0:
            return my_list # Cannot move left, return list unchanged
        else:
            # Move left: current position becomes 0, previous position becomes 1
            my_list[index_of_one] = 0
            my_list[index_of_one - 1] = 1
           
    return my_list

