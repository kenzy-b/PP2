class DivisibleBy3And4:
    def _init_(self, n):
        self.n = n
        self.current = 0

    def _iter_(self):
        return self

    def _next_(self):
        if self.current > self.n:
            raise StopIteration
        if self.current % 3 == 0 and self.current % 4 == 0:
            result = self.current
            self.current += 1
            return result
        self.current += 1
        return self._next_()

for num in DivisibleBy3And4(20):
    print(num)