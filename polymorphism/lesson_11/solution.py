from gateway import find_all_matching


def find_the_cheapest_service(data, predicates={}):
# BEGIN (write your solution here)
    hotels_info = find_all_matching(data, predicates)
    print(hotels_info)
    result = {}
    for elem in hotels_info:
        if result == {}:
            result.update(elem)
        if elem['hotel']['cost'] < result['hotel']['cost']:
            result.update(elem)
    return result
# END

data = [
    {'service': 'kostrovok', 'hotels': [{'name': '$JSInn', 'cost': 200}]},
    {'service': 'book-king', 'hotels': [{'name': '$phpInn', 'cost': 10}]}
]

print(find_the_cheapest_service(data))
# {'hotel': {'cost': 224, 'name':'JSInn'}, 'service': 'kostrovok'}
