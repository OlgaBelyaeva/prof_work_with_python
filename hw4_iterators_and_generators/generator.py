# Задача 2
# Генератор, который принимает список списков, и возвращает их плоское представление

def flat_generator(lists_in_list):
	for item in lists_in_list:
		yield from item

nested_list_1 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

for item in flat_generator(nested_list_1):
	print(item)

print('--------------------------------------------------')

# Задача 4
# Генератор, который принимает список списков с любым уровнем вложенности, и возвращает их плоское представление

def recursive_flat_generator(lists_in_list):
    for item in lists_in_list:
        if isinstance(item, list):
            yield from recursive_flat_generator(item)
        else:
            yield item

nested_list_2 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None, [9, 8, 'z', [5, 6, 'p', ['Y', 'Y']]]],
]

for item in recursive_flat_generator(nested_list_2):
	print(item)