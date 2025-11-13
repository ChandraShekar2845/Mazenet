# List Manipulation
def even_numbers(nums):
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)

    evens.sort(reverse=True)
    return evens

# Example
print(even_numbers([5, 2, 8, 3, 10, 7]))