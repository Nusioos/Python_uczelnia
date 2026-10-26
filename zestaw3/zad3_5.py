x = 12

ruler_line = "|" + "....|" * x

total_length = len(ruler_line)
num_chars = [' '] * total_length

for i in range(x + 1):
    s_val = str(i)
    pos = i * 5  
    
    for j, char in enumerate(s_val):
        idx = pos - len(s_val) + 1 + j
        if 0 <= idx < total_length:
            num_chars[idx] = char

numbers_line = "".join(num_chars)

full_string = ruler_line + "\n" + numbers_line
print(full_string)