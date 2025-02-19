class SquaresUpToN:
    def _init_(self, N):
        self.N = N
        self.current = 0

    def _iter_(self):
        return self

    def _next_(self):
        if self.current >= self.N:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

squares = SquaresUpToN(5)
for square in squares:
    print(square)