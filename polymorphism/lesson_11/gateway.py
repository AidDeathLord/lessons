KOSTROVOK_FEE = 0.12
BOOKKING_CONVERT_RATE = 75

# BEGIN (write your solution here)
def find_all_matching(data):
    for 
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
