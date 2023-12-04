from calculator import Calculator


class CalcLogger:
    def __init__(self, function):
        self.acc = function.acc
        self.function = function

    def sum(self, num):
        start_value = self.acc
        result = self.function.sum(num).result()
        print(f'Первое число: {start_value} Второе число: {num} Сумма: {result}')
        self.acc += num
        return self.__class__(self.function)

    def sub(self, num):
        start_value = self.acc
        result = self.function.sub(num).result()
        print(f'Первое число: {start_value} Второе число: {num} Разность: {result}')
        self.acc -= num
        return self.__class__(self.function)

    def mul(self, num):
        start_value = self.acc
        result = self.function.mul(num).result()
        print(f'Первое число: {start_value} Второе число: {num} Результат: {result}')
        self.acc *= num
        return self.__class__(self.function)

    def result(self):
        return self.function.acc


calc = CalcLogger(Calculator(5))
print(calc.sum(5).mul(5).sub(10).result())
assert calc.result() == 40

