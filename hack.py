"""
Задание:
1. Создайте класс Cars со следующими атрибутами объекта:
● марка (строка)
● модель (строка)
● год выпуска (целое число)
● объем двигателя (decimal, точность 1 знак)
● цвет (строка)
● тип кузова (поле одиночного выбора.
варианты: седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап)
● пробег (целое число)
● цена (decimal, точность 2 знака)
2. Добавьте views:
● create для создания записей
● listing для получения списка записей
● retrieve для получения одной записи
● update для обновления записей
● delete для удаления записей
Extra функционал:
● Создайте urls, чтобы можно было взаимодействовать через терминал.
● Сохранение данных в бд (json / sqlite / postgresql)
● Сделайте комментарии
● Сделайте лайки
"""
import json


class Cars:
    FILE = 'data.json'
    id = 0

    def __init__(self, brand, model, year, volume, color, type_of_body, mileage, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.volume = volume
        self.color = color
        self.type_of_body = type_of_body
        self.mileage = mileage
        self.price = price
        self.send_product_to_json()

    @classmethod
    def get_id(cls):
        cls.id += 1
        return cls.id

    @classmethod
    def get_data(cls):
        with open(cls.FILE) as file:
            return json.load(file)

    @staticmethod
    def get_one_car(data, id):
        car = list(filter(lambda x: x['id'] == id, data))
        if not car:
            return 'нет такой машины'
        return car[0]

    @classmethod
    def send_data_to_json(cls, data):
        with open(cls.FILE, 'w') as file:
            json.dump(data, file)

    def send_product_to_json(self):
        data = Cars.get_data()
        car = {
            'id': Cars.get_id(),
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'volume': self.volume,
            'color': self.color,
            'type_of_body': self.type_of_body,
            'mileage': self.mileage,
            'price': self.price,
        }
        data.append(car)

        with open(Cars.FILE, 'w') as file:
            json.dump(data, file)

        return {'status': '201', 'msg': car}

    @classmethod
    def retrieve_data(cls, id):
        data = cls.get_data()
        car = cls.get_one_car(data, id)
        return car

    @classmethod
    def update_data(cls, id, **kwargs):
        data = cls.get_data()
        car = cls.get_one_car(data, id)
        if type(car) != dict:
            return car
        index = data.index(car)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return {'status': 200, 'msq': 'Updated'}

    @classmethod
    def delete_data(cls, id):
        data = cls.get_data()
        car = cls.get_one_car(data, id)
        if type(car) != dict:
            return car
        index = data.index(car)
        data.pop(index)
        cls.send_data_to_json(data)
        return {'status': 204, 'msq': 'Deleted'}


with open(Cars.FILE, 'w') as file:
    json.dump([], file)

FILE = 'data.json'


def get_data():
    with open(FILE) as file:
        return json.load(file)


def list_of_cars():
    data = get_data()
    return data


def retrieve_data():
    data = get_data()
    id = int(input('enter id car: '))
    product = list(filter(lambda x: x['id'] == id, data))
    return product[0]



def get_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())

        id += 1
    with open('id.txt', 'w') as file:
        file.write(str(id))
        return id


def create_car():
    data = get_data()
    car = {
        'id': get_id(),
        'brand': input('brand:'),
        'model': input('model:'),
        'year': input('year:'),
        'volume': input('volume:'),
        'color': input('color:'),
        'type_of_body': input('type_of_body:'),
        'mileage': input('mileage:'),
        'price': input('price:'),
    }
    data.append(car)

    with open(FILE, 'w') as file:
        json.dump(data, file)
    result = {'msg': 'created', 'product': car}
    return result


def update_car():
    data = get_data()
    flag = False
    id = int(input('vvedite id producta: '))
    car = list(filter(lambda x: x['id'] == id, data))

    if not car:
        return {'msq': 'invalid id! product does not exist!'}
    index = data.index(car[0])
    choice = input('что измените\'?(марка-1, модель-2, год-3, обьем-4, цвет-5, кузов-6: ')
    if choice == '1':
        data[index]['brand'] = input('enter new brand: ')
        flag = True
    elif choice == '2':
        data[index]['model'] = input('enter new model: ')
        flag = True
    elif choice == '3':
        data[index]['year'] = input('enter new year: ')
        flag = True
    elif choice == '4':
        data[index]['volume'] = input('enter new volume: ')
        flag = True
    elif choice == '5':
        data[index]['color'] = float(input('enter new color: '))
        flag = True
    elif choice == '6':
        data[index]['type_of_body'] = input('enter new kuzov: ')
        flag = True
    elif choice == '7':
        data[index]['mileage'] = input('vvedite new mileage: ')
        flag = True
    elif choice == '8':
        data[index]['price'] = input('vvedite new price: ')
        flag = True
    else:
        print('invalid choice to update!!!')

    with open(FILE, 'w') as file:
        json.dump(data, file)
    if flag:
        return {'msg': 'updated', 'product':
            data[index]}
    else:
        return {'msg': 'not UPDATE!'}


def delete_car():
    data = get_data()
    id = int(input('vvedite id producta: '))
    car = list(filter(lambda x: x['id'] == id, data))
    if not car:
        return {'msq': 'invalid id! product does not exist!'}
    index = data.index(car[0])
    deleted = data.pop(index)

    json.dump(data, open(FILE, 'w'))
    return {'msg': 'deleted!', 'product': deleted}

