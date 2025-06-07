# Write your solution here
def no_vowels(a):
    vowles="aoeiu"
    string = ""
    for ch in a:
        if ch not in vowles:
            string+=ch
    return string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
