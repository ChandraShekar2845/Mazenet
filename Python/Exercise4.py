# Dictionary Comprehension
# You take a list of words.
# For each word, count how many vowels it has (a, e, i, o, u).
# Store results as: {word: vowel_count}.
# Main idea: Dictionary comprehension + character checking.

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