# Write your solution here
def longest(strings: list):
    longest_string=""
    for i in strings:
        if len(i) > len(longest_string):
            longest_string = i
    return longest_string

if __name__ == "__main__":
    strings = ['first', 'second', 'third']
    print(longest(strings))
