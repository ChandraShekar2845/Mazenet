# Tuple and Set Operations
# Start with a list of strings.
# Convert the list → tuple (immutable, cannot change).
# Convert the tuple → set (removes duplicates automatically).
# Convert set → sorted list.
# Main idea: Tuple = fixed data, Set = remove duplicates, List = sorted output.

words = ["apple", "banana", "apple", "cherry", "banana"]

t = tuple(words)    # Convert list to tuple
s = set(t)          # Convert tuple to set
result = sorted(s)  # Convert to sorted list

print(result)
