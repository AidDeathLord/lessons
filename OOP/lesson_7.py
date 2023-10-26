class Counter:
    def __init__(self, value=0):
        self.value = max(value, 0)

    def inc(self, delta=1):
        a = self.value + delta
        return Counter(a)

    def dec(self, delta=1):
        self.value -= delta
        if self.value < 0:
            self.value = 0
        return self


c = Counter()
print(c.inc().inc(5).dec(2).value)
print(c.inc().inc().dec().value)
d = c.inc(100)
print(d.dec(1).value)
