class Squares:
    def _init_(self, a, b):
        self.a = a
        self.b = b
        self.current = a

    def _iter_(self):
        return self

    def _next_(self):
        if self.current > self.b:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

for square in Squares(1, 5):
    print(square)