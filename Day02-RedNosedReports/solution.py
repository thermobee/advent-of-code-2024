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