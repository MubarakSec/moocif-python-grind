# Write your solution here
# Write your solution here
def all_the_longest(my_list):
    if not my_list:
        return []
    max_length=max(len(item) for item in my_list)
    return [item for item in my_list if max_length == len(item)]
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
