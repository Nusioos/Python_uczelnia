def make_ruler(n): 
    ruler_line = "|" + "....|" * n

    total_length = len(ruler_line)
    num_chars = [' '] * total_length

    for i in range(n + 1):
        s_val = str(i)
        pos = i * 5  
    
        for j, char in enumerate(s_val):
            idx = pos - len(s_val) + 1 + j
            if 0 <= idx < total_length:
                num_chars[idx] = char

    numbers_line = "".join(num_chars)

    full_string = ruler_line + "\n" + numbers_line
    return full_string


def make_grid(rows, cols): 
    horizontal_line = "+" + "---+" * rows
    vertical_line = "|" + "   |" * rows

    lines = []
    for _ in range(cols):
        lines.append(horizontal_line)
        lines.append(vertical_line)

    lines.append(horizontal_line)
    full_string = "\n".join(lines)
    return full_string

print(make_grid(2, 4))
print()
print(make_ruler(12))