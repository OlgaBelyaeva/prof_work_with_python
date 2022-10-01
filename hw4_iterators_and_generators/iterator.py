# Задача 1

from itertools import chain

# Итератор, который принимает список списков, и возвращает их плоское представление

class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list(chain.from_iterable(nested_list))
        self.start = -1
        self.end = len(self.list_of_lists)


    def __iter__(self):
        self.cursor = self.start
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= self.end:
            raise StopIteration
        return self.list_of_lists[self.cursor]

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

for item in FlatIterator(nested_list):
    print(item)

print('-----------------------------')

# компрехеншн
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)