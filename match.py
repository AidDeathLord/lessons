def get_number_explanation(number: int) -> str:
    match number:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'
        case 7:
            return 'prime number'
        case _:
            return 'just a number'


print(get_number_explanation(8))
print(get_number_explanation(666))
print(get_number_explanation(42))
print(get_number_explanation(7))
