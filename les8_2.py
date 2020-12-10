class MyDevByZero(Exception):
    def __init__(self, text):
        self.text = text

in_data = input("Введите первое число")
in_data_2 = input("Введите второе число")
try:
    in_data = int(in_data)
    in_data_2 = int(in_data_2)
    if in_data_2 == 0:
        raise MyDevByZero("Не делите на ноль, да не делимы будете!")
except ValueError:
    print("Вы ввели не число")
except MyDevByZero as err:
    print(err)
else:
    print((round(in_data / in_data_2, 2)))


