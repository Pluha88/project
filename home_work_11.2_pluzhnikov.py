class Exception_Zero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль запрещено!")

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print(Exception_Zero.divide_by_null(number1, number2))
