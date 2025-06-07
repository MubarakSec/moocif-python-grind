# Write your solution here
# You can test your function by calling it within the following block
def same_chars(string, x, y):
    try:
        return string[x] == string[y]
    except IndexError:
        return False



if __name__ == "__main__":
    print(same_chars("abc", 0, 3))
