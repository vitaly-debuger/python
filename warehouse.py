""" Office Equipment Warehouse"""


class Warehouse:
    stats = {"Printer": 0, "Scanner": 0, "Xerox": 0}
    printers = []

    def __int__(self):
        self.ml = []

    def __str__(self):
        return '\n'.join('\n'.join(map(str, self.printers)))


    @staticmethod
    def get_item(obj):
        if isinstance(obj, Printer):
            Warehouse.stats["Printer"] += 1
            Warehouse.printers.append(obj.__dict__)
        if isinstance(obj, Scanner):
            Warehouse.stats["Scanner"] += 1
        if isinstance(obj, Xerox):
            Warehouse.stats["Xerox"] += 1
            Warehouse.printers.append(vars(obj))

    @staticmethod
    def transfer_to(obj):
        if isinstance(obj, Printer):
            Warehouse.stats["Printer"] -= 1
            Warehouse.printers.append(obj.__dict__)
        if isinstance(obj, Scanner):
            Warehouse.stats["Scanner"] -= 1
        if isinstance(obj, Xerox):
            Warehouse.stats["Xerox"] -= 1
            Warehouse.printers.append(vars(obj))


class OfficeEquipment:
    def __init__(self, name, model, color, year):
        self.n = name
        self.m = model
        self.c = color
        self.y = year


class Printer(OfficeEquipment):
    def __init__(self, name, model, color, year, print_type):
        super().__init__(name, model, color, year)
        self.p_t = print_type


class Scanner(OfficeEquipment):
    def __init__(self, name, model, color, year, sensor_type):
        super().__init__(name, model, color, year)
        self.s_t = sensor_type


class Xerox(OfficeEquipment):
    def __init__(self, name, model, color, year, lights_type):
        super().__init__(name, model, color, year)
        self.l_t = lights_type


item_1 = Printer("Canon", "LTX250", "Black", 2007, "Jet")
item_2 = Xerox("Xerox", "XT20", "Black", 2003, "Halogen")
item_4 = Scanner("Scan Jet", "Armada", "White", 2009, "BlaBla")
item_3 = Xerox("Xerox", "XT222", "White", 2003, "Halogen")
Warehouse.get_item(item_1)
Warehouse.get_item(item_2)
Warehouse.get_item(item_3)
Warehouse.get_item(item_4)
print(f"Актуальное состояние склада {Warehouse.stats}")
Warehouse.transfer_to(item_3)
print(f"Актуальное состояние склада {Warehouse.stats}")
print(f"{Warehouse.printers}")
