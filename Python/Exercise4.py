# Dictionary Comprehension
words = ["apple", "sky", "orange"]

vowels = "aeiou"
output = {}

for w in words:
    count = 0
    for char in w.lower():
        if char in vowels:
            count += 1
    output[w] = count

print(output)