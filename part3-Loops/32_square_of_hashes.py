# Upgraded version of square of hashes
def hash_square(hashmany):
    i = hashmany
    while i > 0:
        print("#"*hashmany)
        i -= 1
if __name__ == "__main__":
    hash_square(5)
