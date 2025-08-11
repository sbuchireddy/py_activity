#Define sets a, b, c, and d
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
c = {5, 6, 7, 8, 9}
d = {1, 3, 7, 9, 10}

# Perform complex set operations:
# Each part computes intersections and differences between sets,
# then combines them using union (|)

print((a&b-c-d)|(a&c-b-d)|(a&d-b-c)|(b&c-a-d)|(b&d-a-c)|(c&d-a-b))


