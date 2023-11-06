import array # Зачем?
import json
from pprint import pprint # Зачем?

# Почему исключение именно так прописано?
class myException(Exception):
    def __str__(self):
        return "Введено недопустимое значение"

# Так ну тут чтение файла типа
def read(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return (data)

# Тут типа запись
def write(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

# Что тут удаляется?
def delete(data, filename, whatToDelete):
    min = 0
    for txt in data['menu']:
        if txt['name'] == whatToDelete:
            data['menu'].pop(min)
        min = min+1
    return(data)

# Тут именно абстрактный класс меню
class menu():
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        if price < 0:
            raise myException() # Почему то ислкючение появлиось
        self.ingredients = ingredients

    def description(self): pass # Абстрактный метод описания

# Ниже два производных класса от меню
class dishes(menu):
    def description(self):
        print("You can eat the ", self.name, " by ", self.price, "$ with some", *self.ingredients)


class drinks(menu):
    def description(self):
        print("You can drink the ", self.name, " by ", self.price, "$ with some", *self.ingredients)


# Объекты 
chicken = dishes("chicken", 8, ['chiken,', 'soy sauce,', 'paprika'])
chicken.description()

strawberryMilkshake = drinks("strawberry milkshake", 5, ['milk,', 'cream,', 'strawberry'])
strawberryMilkshake.description()


# Что-то непонятное с JSON
data = {'name': 'salad', 'price': 7, 'ingredients': 'tomato, cucumber, salad, sour cream'}
readJsonToAppend = read('JSON_menu.json')
readJsonToAppend['menu'].append(data)
writeJson = write(readJsonToAppend, 'JSON_menu.json')

readJsonToDelete = read('JSON_menu.json')
readJsonToDelete = delete(readJsonToDelete, 'JSON_menu.json', 'tea')
writeJson = write(readJsonToDelete, 'JSON_menu.json')

# По итогу нет записи в XML, а надо