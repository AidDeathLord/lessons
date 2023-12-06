from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits as ascii_digits,
    punctuation
)
import random


def generate_password(len, uppercase=False, digits=False, symbols=False):
    gen_pool = ascii_lowercase
    if uppercase:
        gen_pool += ascii_uppercase
        print(1)
    if digits:
        gen_pool += ascii_digits
        print(2)
    if symbols:
        gen_pool += punctuation
        print(3)
    return ''.join(random.choice(gen_pool) for _ in range(len))
