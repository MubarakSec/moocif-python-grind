# Write your solution here
def longest_series_of_neighbours(numbers):
    max_len = 1
    current_len = 1

    for i in range(1,len(numbers)):
        if numbers[i] - numbers[i-1] == 1 or numbers[i] - numbers[i-1] == -1:
            current_len += 1
            if current_len > max_len:
                
                max_len = current_len
        else:
            current_len = 1
    return max_len

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
