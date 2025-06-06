# Task: Ask for number of students and desired group size, 
# print number of groups formed using integer division
student=int(input("How many students"))
group=int(input("desired group"))

full_group= (student + group - 1) // group

print(f"Number of groups formed: {full_group}")
