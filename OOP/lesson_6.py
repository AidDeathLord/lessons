class Counter:
    value = 0

    def inc(self, delta=1):
        self.value += delta

    def dec(self, delta=1):
        self.value -= delta
        if self.value < 0:
            self.value = 0


c = Counter()
c.inc()
c.inc()
c.inc(40)
print(c.value)  # 42
c.dec()
c.dec(30)
print(c.value)  # 11
c.dec(delta=100)
print(c.value)  # 0
