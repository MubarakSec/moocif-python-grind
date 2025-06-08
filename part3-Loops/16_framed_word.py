# A word in a box
name = input("Enter a word: ")
box_width = 30
content_width = box_width - 2  # account for the '*' borders

if len(name) > content_width:
    print("Word is too long for the box.")
else:
    total_padding = content_width - len(name)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding

    print("*" * box_width)
    print("*" + " " * left_padding + name + " " * right_padding + "*")
    print("*" * box_width)
    
