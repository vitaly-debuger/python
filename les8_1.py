class Data:
    def __init__(self, date, month, year):
        self.data = date
        self.month = month
        self.year = year

    @classmethod
    def extract(cls, data):

        d = data.split("-")

        return cls(int(d[0]), int(d[1]), int(d[2]))

    @staticmethod
    def validation(obj):
        if 1 <= obj.data <= 31:
            if 1 <= obj.month <= 12:
                if 9999 >= obj.year >= 0:
                    return f'Лучший!'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


m_1 = Data.extract("05-04-1992")

print(f"Число {m_1.data},\tмесяц {m_1.month},\tгод {m_1.year}")
print(type(m_1.data))
print(Data.validation(m_1))

