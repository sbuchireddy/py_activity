def make_func(val):
    return lambda: val * 3

funcs = [make_func(i) for i in range(1, 4)]
print("Results: " + ", ".join(str(f()) for f in funcs))
