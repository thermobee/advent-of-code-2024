"""
    Example input file:
    68878   98732
    24519   87903
    73275   70114
    87985   89419
    80485   75440
    ...
    ...
    ...
"""

# Two location lists
location1 = []
location2 = []

# Read input file and create two lists with the locations
with open('input.txt') as file:
    for line in file:
        location1.append(int(line.split()[0]))
        location2.append(int(line.split()[1]))

# Sort the two lists
location1 = sorted(location1)
location2 = sorted(location2)


### Part 1, calculate total distance between all each set of points
# Iterate over the sorted lists, find the distance between each pair, add to the total
total_diff = 0
for count, value in enumerate(location1):
    total_diff += abs(value - location2[count])

print(total_diff)

### Part 2, calculate the similarity score
sim_score = 0

for number in location1:
    sim_score += location2.count(number) * number

#print(sim_score)