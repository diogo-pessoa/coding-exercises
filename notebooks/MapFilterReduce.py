import math
from functools import reduce
# Map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

my_numbers = [4, 6, 9, 23, 5]

mapping_floats = map(lambda x: math.floor(x), my_floats)

print(type(mapping_floats))
# >>> <class 'map'>
print(list(mapping_floats))
# >>> [18.922, 37.088, 10.562, 95.453, 4.666, 78.854, 21.068]

# Fix all three respectively.
# map_result = list(map(lambda x: x, my_floats))
# filter_result = list(filter(lambda name: name, my_names, my_names))
# reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers, 0)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)
