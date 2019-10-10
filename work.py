import requests
from pprint import pprint

access_token = '30deb38527ac08fd3430a3872dc8523b2c0bf26390f1839399f5cbb668872ccc613d3916a2d8a7248235b'


class User:
    def __init__(self, access_token, user_id):
        self.access_token = access_token
        self.user_id = str(user_id)
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

    def __str__(self):
        url = str(self.url)
        return url

    def create(self, friends):
        user_list = []
        for i in friends:
            users = User(self.access_token, i)
            user_list.append(users)
        return user_list

    def __and__(self, User):
        friends = self.mutual_friends_vk(User)
        friends_list = self.create(friends['response'])
        return friends_list


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


# interface()
user = User(access_token, 456951815)
user2 = User(access_token, 15804819)
friends_list = user&user2
print(user)
print(friends_list)
for i in friends_list:
    print(i)
