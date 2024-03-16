def get_max_votes_value_idx(votes):
    target_val = max(votes)  # Get the max value

    # Use list comprehension to catch any multiple max values that may exist
    target_val_indices = [i for i, x in enumerate(votes) if x == target_val]
    # If just 1 max value exists, get its index
    if len(target_val_indices) == 1:
        idx = target_val_indices[0]
        return idx

def get_most_satisfying_product():
