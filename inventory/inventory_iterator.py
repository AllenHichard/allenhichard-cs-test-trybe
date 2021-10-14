from _collections_abc import Iterator
class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = -1
    def __next__(self):
        if self.index < len(self.data):
            self.index += 1
            return self.data[self.index]