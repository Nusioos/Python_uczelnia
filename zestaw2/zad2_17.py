line = "Python jest wspaniałym językiem programowania do nauki"

words = line.split()

sorted_alphabetical = sorted(words)

sorted_by_length = sorted(words, key=len)

print("Oryginalny tekst:", line)
print("Alfabetycznie:", sorted_alphabetical)
print("Pod względem długości:", sorted_by_length)