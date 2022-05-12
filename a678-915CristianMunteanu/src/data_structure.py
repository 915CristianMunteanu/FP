class DataStructure:
    def __init__(self, new_list=None):
        if new_list is None:
            new_list = dict()
        self._data_structure = new_list

    def __len__(self):
        return len(self._data_structure)

    def __setitem__(self, key, value):
        self._data_structure[key] = value

    def __getitem__(self, item):
        return self._data_structure[item]

    def __delitem__(self, key):
        del self._data_structure[key]

    def __iter__(self):
        self.key = -1
        return self

    def __next__(self):
        self.key += 1
        if self.key >= len(self._data_structure):
            raise StopIteration
        return self._data_structure[self.key]

    def append(self, item):
        self._data_structure.append(item)

    def remove(self, item):
        self._data_structure.remove(item)

    def values(self):
        return self._data_structure.values()
    def keys(self):
        return self._data_structure.keys()

def filter_function(iterable, accept):
    new_list = type(iterable)()
    for x in iterable:
        if accept(x):
            new_list.append(x)
    return new_list


def shell_sort(data_structure_to_be_sorted, compare_function):
    gap = len(data_structure_to_be_sorted) // 2
    while gap > 0:
        for first_index in range(gap, len(data_structure_to_be_sorted)):
            auxiliary = data_structure_to_be_sorted[first_index]
            second_index = first_index
            while second_index >= gap and compare_function(data_structure_to_be_sorted[second_index - gap],
                                                           auxiliary) == 1:
                data_structure_to_be_sorted[second_index] = data_structure_to_be_sorted[second_index - gap]
            data_structure_to_be_sorted[second_index] = auxiliary
        gap //= 2
    return data_structure_to_be_sorted
