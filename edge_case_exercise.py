def move(positions, direction):
    # Find the current index of the pig (the 1)
    current_index = positions.index(1)
    
    # Create a copy of the list with all zeros
    new_positions = [0] * len(positions)
    
    # Determine the new position
    if direction == 'right':
        # Move one step to the right, if not at the end
        new_index = min(current_index + 1, len(positions) - 1)
    elif direction == 'left':
        # Move one step to the left, if not at the beginning
        new_index = max(current_index - 1, 0)
    else:
        raise ValueError("Direction must be 'left' or 'right'")
    
    # Place the pig (1) in the new position
    new_positions[new_index] = 1
    
    return new_positions

