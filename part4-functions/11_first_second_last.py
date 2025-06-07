# Write your solution here
# You can test your function by calling it within the following block
def first_word(x):
    i=0
    word = ""
    while i < len(x) and x[i] != " ":
        word += x[i]
        i += 1

    return word
def second_word(y):
    i = 0
    n = len(y)
    while i < n and y[i] != ' ':
        i += 1
    i += 1 

    word = ""
    while i < n and y[i] != ' ':
        word += y[i]
        i += 1

    return word
def last_word(z):
    i=len(z)-1
    word=""
    while i >= 0 and z[i] != " ":
        word += z[i]
        i -= 1

    return word[::-1]
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
