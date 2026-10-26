x = 4
y = 2

horizontal_line = "+" + "---+" * x
vertical_line = "|" + "   |" * x

lines = []
for _ in range(y):
    lines.append(horizontal_line)
    lines.append(vertical_line)

lines.append(horizontal_line)
full_string = "\n".join(lines)
print(full_string)