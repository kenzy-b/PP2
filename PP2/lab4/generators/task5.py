class Countdown:
    def _init_(self, n):
        self.n = n

    def _iter_(self):
        return self

    def _next_(self):
        if self.n < 0:
            raise StopIteration
        result = self.n
        self.n -= 1
        return result

for num in Countdown(5):
    print(num)