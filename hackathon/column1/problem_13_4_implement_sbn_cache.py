from collections import OrderedDict


class Cache:
    def __init__(self, size):
        self.size = size
        self.cache = OrderedDict()

    def insert(self, item, price):
        if len(self.cache.keys()) == self.size:
            self.cache.popitem(last=False)

        if item in self.cache:
            original_item = self.cache[item]
            self.cache.pop(item)
            self.cache[item] = original_item
        else:
            self.cache[item] = (item, price)

    def get(self, item):
        if item not in self.cache:
            return None

        inserted_item = self.cache[item]
        self.cache.pop(item)
        self.cache[item] = inserted_item

        return inserted_item

    def delete(self, item):
        self.cache.pop(item)

