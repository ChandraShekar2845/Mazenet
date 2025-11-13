# Tuple and Set Operations

words = ["apple", "banana", "apple", "cherry", "banana"]

t = tuple(words)    # Convert list to tuple
s = set(t)          # Convert tuple to set
result = sorted(s)  # Convert to sorted list

print(result)
