# same charachters or not
def same_chars(string, x, y):
    try:
        return string[x] == string[y]
    except IndexError:
        return False



if __name__ == "__main__":
    print(same_chars("abc", 0, 3))
