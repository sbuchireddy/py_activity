# List of tuples with varying lengths
data = [
    ('A', 1, 2),       # Length 3
    ('B', 3),          # Length 2
    ('C', 4, 5, 6),    # Length 4
    ('D',),            # Length 1
    ('E', 7, 8)        # Length 3
]

# Sort the list of tuples based on their length (number of elements in each tuple)
sorted_data = sorted(data, key=len)

# Extract the first element (usually a label or identifier) from each tuple in the sorted list
result = [items[0] for items in sorted_data]

# Print the list of first elements in order of increasing tuple length
print(result)
