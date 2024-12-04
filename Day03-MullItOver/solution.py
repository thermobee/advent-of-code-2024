import io,re

file = io.open("input", mode="r", encoding="utf-8")
rfile = file.read()
total = 0

pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, rfile)

for i in matches:
    total += (int(i[0]) * int(i[1]))

print(total)