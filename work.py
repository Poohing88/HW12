import requests
from pprint import pprint


class User:
    def __init__(self, access_token, user_id):
        self.access_token = access_token
        self.user_id = user_id
        self.url = f'https://vk.com/id{self.user_id}'

    def get_params(self):
        return {
            'user_id': self.user_id,
            'access_token': self.access_token,
            'v': 5.101
        }

    def get_friends(self):
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params=params
        )
        return response.json()

    def mutual_friends(self, user2):
        friends1 = set(self.get_friends()['response']['items'])
        friends2 = set(user2.get_friends()['response']['items'])
        all_friends = friends1.intersection(friends2)
        return all_friends

    def mutual_friends_vk(self, user):
        params = {
            'source_uid': self.user_id,
            'target_uid': user.user_id,
            'access_token': access_token,
            'v': 5.101
        }
        URL = 'https://api.vk.com/method/friends.getMutual'
        friends = requests.get(URL, params=params)
        return friends.json()


def interface():
    quantity_users = int(input('Введите количество пользователей '))
    users = []
    for i in range(quantity_users):
        user_id = int(input("Введите id первого пользователя "))
        user = User(access_token, user_id)
        users.append(user)
    print('Список команд\n'
          '1. Показать ссылку на пользователя, введите user(номер пользователя)\n'
          '2, Показать общих друзей пользователей, введите user(номер)&user(номер)\n'
          '3. Вывести все ссылки на пользователейб введите  all')
    comand = input('Введите команду ')
    comand = comand.split()
    comands = []
    for a in comand:
        comands.append(a)
    if comand == 'all':
        counter = 0
        for i in users:
            print(users[counter].url)
            counter += 1
    elif comands[5] == '&':
        i = int(comands[4]) - 1
        i2 = int(comands[10]) - 1
        print(i, i2)
        pprint(users[i].mutual_friends_vk(users[i2]))
    elif len(comands) == 5:
        i = int(comands[4]) - 1
        print(users[i].url)
    else:
        print('Вы ввели неверную команду ')


access_token = 'dcfa5620d11f33e0aa41220939ce3ffbb9a8aa1c61b0588bc9817bed770b997427ad20ed0823fe7985477'

interface()