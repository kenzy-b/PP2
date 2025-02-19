class EvenNumbersUpToN:
    def _init_(self, n):
        self.n = n
        self.current = 0

    def _iter_(self):
        return self

    def _next_(self):
        if self.current > self.n:
            raise StopIteration
        if self.current % 2 == 0:
            result = self.current
            self.current += 1
            return result
        self.current += 1
        return self._next_()

n = int(input("Введите n: "))
even_numbers = EvenNumbersUpToN(n)
print(", ".join(map(str, even_numbers)))