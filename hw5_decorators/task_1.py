# Задача 1
# Декоратор логгер

import datetime
import os
from itertools import chain

def log_func(old_function):

    def new_function(*args, **kwargs):

        result = old_function(*args, **kwargs)
        BASE_PATH = os.getcwd()
        LOGS_FILE_NAME = 'logs.txt'
        file_path = os.path.join(BASE_PATH, LOGS_FILE_NAME)
        log_info = f'{datetime.datetime.now()}\n' \
                   f'вызвана функция {old_function.__name__}\n' \
                   f'с аргументами {args} и {kwargs}\n' \
                   f'вернулось значение {result}\n' \
                   f'\n'
        print(log_info)
        with open(file_path, 'a') as document:
            document.write(log_info)
        return result

    return new_function

@log_func
def flat_generator(lists_in_list):
	for item in lists_in_list:
		yield from item

nested_list_1 = [
	['None', 'c'],
	['z', False],
	[9, 5, None],
]

for item in flat_generator(nested_list_1):
	print(item)