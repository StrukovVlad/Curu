
from dataclasses import dataclass


@dataclass
class User:
    username: str


class InMemoryUserRepository:
    def __init__(self):
        self._users = []

    def __add__(self, user):
        self._users.append(user)

    def get_by_username(self, username):
        return next(user for user in self._users if user.username == username )
        # user.username == username)


User.username = 'Bitrix'

btx = InMemoryUserRepository()

btx.__add__('Petya')
btx.__add__('Sema')
btx.__add__('Niki')
btx.__add__('Sanya')

print(btx.get_by_username('AutoMarket'))
# Petya