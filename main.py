def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()


def print_params(*paramets):
    print(*paramets)

print_params(5, 8, 9, 12, 6, 'строка', False)
print_params()

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(c=[1, 2, 3])

values_list = [3, 'Привет', False]
values_dict = {'a': 1, 'b': 'строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)