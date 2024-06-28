def print_params(a = 2, b = 'string', c = False):
    print(a, b, c)
value_list2 = [1.11, "wow"]
print_params(*value_list2, 42)