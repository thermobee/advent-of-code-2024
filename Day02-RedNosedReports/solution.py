"""
    Example input file:
    6 8 9 10 12 13 12
    76 77 80 82 84 86 88 88
    84 86 88 90 93 97
    21 24 26 29 30 33 36 42
    23 24 25 26 24 25 27
    ...
    ...
    ...
"""

file = open("input.txt")
safe_reports_counter = 0

# Function to shuffle through the numbers and compare
def compare_numbers(my_list):
    # Compare existing line to a sorted/reverse sorted to confirm ascending/descending order
    if my_list == sorted(my_list, reverse=False) or my_list == sorted(my_list, reverse=True):
        # Compare each pair of numbers
        for i in range(len(my_list) - 1):
            a, b = my_list[i], my_list[i + 1]
            if (abs(a - b) > 3) or (abs(a - b) < 1):
                return(False)
        return(True)

    return(False)

# Function that creates a new list and removes the given index
def check_tolerance(my_list, index):
    list_copy = my_list[:]
    list_copy.pop(index)

    return(list_copy)

# Brake down the problem to individual lists
for line in file:
    reports = [int(i) for i in line.split(' ')]

    index = 0

    if compare_numbers(reports) == True:
        safe_reports_counter +=1
    else:
        for i in range(len(reports)):
            tolerated_report = check_tolerance(reports, i)
            if compare_numbers(tolerated_report):
                index += 1
        if index >= 1:
            safe_reports_counter +=1

print(safe_reports_counter)