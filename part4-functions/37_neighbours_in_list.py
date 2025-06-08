# Function to find the length of the longest consecutive series 
# where each number is a neighbor (difference of ±1) to the previous one
def longest_series_of_neighbours(numbers):
    max_len = 1          # Stores the length of the longest valid series found
    current_len = 1      # Tracks the current sequence length

    for i in range(1, len(numbers)):
        # Check if current number is a neighbor (±1) of the previous number
        if numbers[i] - numbers[i-1] == 1 or numbers[i] - numbers[i-1] == -1:
            current_len += 1
            # Update max_len if a longer series is found
            if current_len > max_len:
                max_len = current_len
        else:
            # Reset current_len if sequence is broken
            current_len = 1
    return max_len

# Test the function with a sample list
if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
