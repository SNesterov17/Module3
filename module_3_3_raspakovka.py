def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [4, True, 'Sun']
values_dict = {'a' : 'star', 'b' : 7, 'c' : 15}
values_list_2 = [43.62, 'light']

print_params(b = 25)
print_params(c = [1,2,3])
print_params()
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)



