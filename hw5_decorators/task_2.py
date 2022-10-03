# Задача 2
# Декоратор логгер с параметром - путь к логам

import datetime
import os

def log_func_with_path(file_path):
    def decorator(old_function):

        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            log_info = f'{datetime.datetime.now()}\n' \
                       f'вызвана функция {old_function.__name__}\n' \
                       f'с аргументами {args} и {kwargs}\n' \
                       f'вернулось значение {result}\n' \
                       f' \n'
            with open(file_path, 'a') as document:
                document.write(log_info)
            return result

        return new_function

    return decorator

@log_func_with_path(file_path=os.path.join(os.getcwd(), 'logs.txt'))
def flat_generator(lists_in_list):
	for item in lists_in_list:
		yield from item

nested_list_2 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

for item in flat_generator(nested_list_2):
	print(item)