KOSTROVOK_FEE = 0.12
BOOKKING_CONVERT_RATE = 75


# BEGIN (write your solution here)
MAPPING = {
    'kostrovok': lambda x: x * KOSTROVOK_FEE + x,
    'book-king': lambda x: x * BOOKKING_CONVERT_RATE,
    'airdnb': lambda x: x
}


def find_all_matching(data, price={}):
    min_max_price = {'min': float('-inf'), 'max': float('inf')}
    for keys, values in price.items():
        min_max_price[keys] = values
    result = []
    for elem in data:
        for hotel in elem.get('hotels'):
            cost = MAPPING[elem.get('service')](hotel['cost'])
            if min_max_price['min'] <= cost <= min_max_price['max']:
                result.append({'hotel': {'cost': cost, 'name': hotel.get('name')}, 'service': elem.get('service')})

    return result

# END


a = [
  {'service': 'kostrovok', 'hotels': [{'name': '$JSInn', 'cost': 200}]},
  {'service': 'book-king', 'hotels': [{'name': '$phpInn', 'cost': 10}]}
]
# Цены на отели возвращаются уже в нормализованном виде
# возвращается массив отелей объединенных с именем сервиса из которого они извлекаются
hotel_infos = find_all_matching(a)
# [
# {"hotel": {"cost": 224, "name": 'JSInn'}, "service": 'kostrovok'},
# {"hotel": {"cost": 750, "name": '$phpInn'}, "service": 'book-king'}
# ]
