class DataCapture:
    def __init__(self):
        self.collection: list = []

    def add(self, n: int):
        self.collection.append(n)

    def less(self, number: int) -> list:
        numbers = [
            n for n in self.collection
            if n < number
        ]
        return numbers

    def greater(self, number: int) -> list:
        numbers = [
            n for n in self.collection
            if n > number
        ]
        return numbers

    def between(self, start: int, end: int) -> list:
        if start > end:
            raise ValueError("Starting number must be less than ending number")
        numbers = [
            n for n in self.collection
            if n >= start
            and n <= end
        ]
        return numbers

    def build_stats(self):
        list_size = len(self.collection)
        for i in range(list_size):
            for j in range(0, list_size -i -1):
                if self.collection[j] > self.collection[j + 1]:
                    self.collection[j], self.collection[j + 1] = self.collection[j + 1], self.collection[j]

    def __find_index_for__(self, n):
        for i, element in enumerate(self.collection):
            if element == n:
                return i
        return -1
