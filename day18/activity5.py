def find_pythagorean_triplets(limit):
    return [(a, b, c)
            for a in range(1, limit)
            for b in range(a + 1, limit)
            for c in range(b + 1, limit)
            if a * a + b * b == c * c]

print(find_pythagorean_triplets(31))
