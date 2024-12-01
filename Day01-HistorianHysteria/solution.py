# Two location lists
location1 = []
location2 = []

# Read input file and create two lists with the locations
with open('input.txt') as file:
    for line in file:
        #print(line.split())
        location1.append(int(line.split()[0]))
        location2.append(int(line.split()[1]))

# Sort the two lists
location1 = sorted(location1)
location2 = sorted(location2)

# Iterate over the sorted lists, find the distance between each pair, add to the total
total_diff = 0
for count, value in enumerate(location1):
    diff = value - location2[count]
    total_diff += abs(diff)

print(total_diff)