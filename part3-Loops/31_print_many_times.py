# print the word as many as you want
def print_many_times(text, times):
    i=0
    while i < times:
        print(text)
        i+=1

if __name__ == "__main__":
    text=input("enter a word")
    times=int(input("how many times"))
    print_many_times(text, times)
