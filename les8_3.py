class MyErr(Exception):
    def __init__(self, text):
        self.text = text

my_list = []

while True:
    in_data = input("Введите число или оставьте строку пустой для выхода: ")
    if in_data == "":
        break
    try:
        if in_data.replace("-", "").replace(".", "").isdigit():
            my_list.append(float(in_data))
        else:
            raise MyErr("Введено не число!")
    except MyErr as err:
        print(err)
        continue

print(my_list)