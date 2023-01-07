class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return self.size()

    def enqueue(self, value):
        self._data.append(value)

    def is_empty(self):
        return self._data == []

    def dequeue(self):
        if not self.is_empty():
            return self._data.pop(0)
        else:
            return None

    def search(self, index):
        if not (index >= 0 and index < self.size()):
            raise IndexError
        else:
            return self._data[index]

    def size(self):
        return len(self._data)
