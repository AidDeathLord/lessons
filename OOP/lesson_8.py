class HourClock:
    def __init__(self):
        self.time = 0

    @property
    def hours(self):
        return self.time % 12

    @hours.setter
    def hours(self, value):
        self.time = value


clock = HourClock()
print(clock.hours)  # 0
clock.hours += 5
# ^ эквивалентно clock.hours = clock.hours + 5
clock.hours += 5
print(clock.hours)  # 10
clock.hours += 5
print(clock.hours)  # 3
clock.hours -= 4
print(clock.hours)  # 11
clock.hours = 123
print(clock.hours)  # 3
