# List Manipulation
# You take a list of integers.
# You loop through each number.
# If the number is even (n % 2 == 0), you keep it.
# Finally, you sort the even numbers in descending order.
# Main idea: Filtering + sorting.

def even_numbers(nums):
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)

    evens.sort(reverse=True)
    return evens

# Example
print(even_numbers([5, 2, 8, 3, 10, 7]))