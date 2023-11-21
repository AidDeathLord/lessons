from user import User
from guest import Guest


def greet(person):
    if person.get_access() == 'User':
        return f'Hello {person.get_name()}!'
    elif person.get_access() == 'Guest':
        return f'Nice to meet you {person.get_name()}!'



guest = Guest()
assert greet(guest) == 'Nice to meet you Guest!'
user1 = User('Petr')
assert greet(user1) == 'Hello Petr!'
user2 = User('Anna')
assert greet(user2) == 'Hello Anna!'
user3 = User('Guest')
assert greet(user3) == 'Hello Guest!'
