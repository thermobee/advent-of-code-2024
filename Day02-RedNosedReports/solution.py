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
    for i in range(len(my_list) - 1):
        a, b = my_list[i], my_list[i + 1]
        if (abs(a - b) > 3) or (abs(a - b) < 1):
            return(False)
    return(True)

# Brake down the problem to individual lists
for line in file:
    reports = [int(i) for i in line.split(' ')]

    # Compare existing line to a sorted/reverse sorted to confirm ascending/descending
    if reports == sorted(reports, reverse=False) or reports == sorted(reports, reverse=True) :
        answer = compare_numbers(reports)
        if answer == True:
            safe_reports_counter += 1

print(safe_reports_counter)