from fake_subscription import FakeSubscription
from subscription import Subscription


class User():
    def __init__(self, email, current_subscription=None):
        self.email = email
        # BEGIN (write your solution here)
        self.current_subscription = current_subscription or FakeSubscription(self)
        # END

    def get_current_subscription(self):
        return self.current_subscription

    def is_admin(self):
        return self.email == 'rakhim@hexlet.io'



user1 = User('vasya@email.com', Subscription('premium'))
print(user1.get_current_subscription().has_premium_access())  # True
print(user1.get_current_subscription().has_professional_access())  # False

user2 = User('vasya@email.com', Subscription('professional'))
print(user2.get_current_subscription().has_premium_access())  # False
print(user2.get_current_subscription().has_professional_access())  # True

# Внутри создается фейковая, потому что подписка не передается
user3 = User('vasya@email.com')
print(user3.get_current_subscription().has_premium_access())  # False
print(user3.get_current_subscription().has_professional_access())  # False

user4 = User('rakhim@hexlet.io')  # администратор, проверяется по емейлу
print(user4.get_current_subscription().has_premium_access())  # True
print(user4.get_current_subscription().has_professional_access())  # True
