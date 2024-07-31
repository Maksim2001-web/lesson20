class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        obj = super(House, cls).__new__(cls)
        obj.name = args[0]
        cls.houses_history.append(obj.name)
        return obj

    def __init__(self, name, floors):
        self.floors = floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

del h1

print(House.houses_history)
