class CacheSystem:

    def __init__(self, size):
        self._cache_size = size
        self._cache_values = {}
        # self._cache_values = dict()
        self.step = 0

    def __setitem__(self, key, value):
        self.step += 1
        return1 = None
        return2 = None

        if len(self._cache_values) == 0:
            self._cache_values.update({key: value})
            return2 = f'{self.step} PUT {str(key)}'
            return return1, return2
        minimum = min(list(self._cache_values.items()), key=lambda x: x[1])[0]
        if value >= self._cache_values[minimum]:
            if (len(self._cache_values) >= self._cache_size) and \
                    (key != minimum) and \
                    (1 == 1):
                if minimum != 'init_min_error_creator':
                    # print(f'{self.step} DELETE {minimum}')
                    return1 = f'{self.step} DELETE {minimum}'
                self._cache_values.pop(minimum)

            if key in self._cache_values.keys():
                if value > self._cache_values[key]:
                    self._cache_values[key] = value
                    # print(f'{self.step} UPDATE {str(key)}')
                    return2 = f'{self.step} UPDATE {str(key)}'
            if key not in self._cache_values.keys():
                self._cache_values.update({key: value})
                # print(f'{self.step} PUT {str(key)}')
                return2 = f'{self.step} PUT {str(key)}'

            return return1, return2

        if value < self._cache_values[minimum]:
            return1 = None
            return2 = None
            if len(self._cache_values) < self._cache_size:
                if key in self._cache_values.keys():
                    if value > self._cache_values[key]:
                        self._cache_values[key] = value
                        # print(f'{self.step} UPDATE {str(key)}')
                        return2 = f'{self.step} UPDATE {str(key)}'
                if key not in self._cache_values.keys():
                    self._cache_values.update({key: value})
                    return2 = f'{self.step} PUT {str(key)}'
                    # print(f'{self.step} PUT {str(key)}')
            return return1, return2


def test1():
    cache = CacheSystem(3)

    cache.__setitem__('status', 1)
    cache.__setitem__('history', 2)
    # print(cache._cache_values)
    cache.__setitem__('status', 3)
    # print(cache._cache_values)
    cache.__setitem__('price', 4)
    # print(cache._cache_values)
    cache.__setitem__('name', 5)
    # print(cache._cache_values)
    cache.__setitem__('card', 6)
    # print(cache._cache_values)


def printer_goes_brrr(inp):
    inp = list(inp)
    if inp[0] and inp[1]:
        print(inp[0])
        print(inp[1])
    if inp[0] and not inp[1]:
        print(inp[0])
    if inp[1] and not inp[0]:
        print(inp[1])
    if not inp[0] and not inp[1]:
        pass


def testret():
    cache = CacheSystem(3)

    printer_goes_brrr(cache.__setitem__('status', 1))
    printer_goes_brrr(cache.__setitem__('history', 2))
    printer_goes_brrr(cache._cache_values)
    printer_goes_brrr(cache.__setitem__('status', 3))
    printer_goes_brrr(cache._cache_values)
    printer_goes_brrr(cache.__setitem__('price', 4))
    printer_goes_brrr(cache._cache_values)
    printer_goes_brrr(cache.__setitem__('name', 5))
    printer_goes_brrr(cache._cache_values)
    printer_goes_brrr(cache.__setitem__('card', 6))
    printer_goes_brrr(cache._cache_values)


def test2():
    cache = CacheSystem(2)

    cache.__setitem__('status', 4)
    cache.__setitem__('history', 2)
    cache.__setitem__('history', 10)
    cache.__setitem__('price', 7)
    cache.__setitem__('status', 3)


def test2ret():
    cache = CacheSystem(2)

    printer_goes_brrr(cache.__setitem__('status', 4))
    printer_goes_brrr(cache.__setitem__('history', 2))
    printer_goes_brrr(cache.__setitem__('history', 10))
    printer_goes_brrr(cache.__setitem__('price', 7))
    printer_goes_brrr(cache.__setitem__('status', 3))


def console_input():
    input_string = input().split(' ')  # 6 3
    cache = CacheSystem(int(input_string[1]))
    for _buffer_ in range(int(input_string[0])):
        input_substring = input().split(' ')
        printer_goes_brrr(cache.__setitem__(input_substring[0], int(input_substring[1])))


console_input()
