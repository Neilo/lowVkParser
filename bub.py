import vk  # Импортируем модуль vk
import json
import time
from datetime import date


class user(object):
    def __init__(self, id, sex, firtsName, lastName, relation, age):
        self.id = id
        self.sex = sex
        self.firtsName = firtsName
        self.lastName = lastName
        self.relation = relation
        self.age = age

    def whatIsSex(sex):
        if sex == 1:
            return 'female'
        elif sex == 2:
            return 'male'
        else:
            return 'idk'

    def whatIsRelation(relation):
        if relation == 1:
            return('не женат/не замужем')
        elif relation == 2:
            return('есть друг/есть подруга')
        elif relation == 3:
            return('помолвлен/помолвлена')
        elif relation == 4:
            return('женат/замужем')
        elif relation == 5:
            return('всё сложно')
        elif relation == 6:
            return('в активном поиске')
        elif relation == 7:
            return('влюблён/влюблена')
        elif relation == 8:
            return('в гражданском браке')
        else:
            return('не указано')

    def calculate_age(born):
        pass

    def userInfo(city, sex, relation, ageFrom, ageTo):
        user = vk_api.users.search(city = city, sex = sex, status = relation, age_from = ageFrom, age_to = ageTo, v=5.92)
        for i in range(len(user['items'])):
            generateObj(user['items'][i]['id'], sex, user['items'][i]['first_name'], user['items'][i]['last_name'], relation, ageFrom, ageTo)


def generateObj(id, sex, firtsName, lastName, relation, age1, age2):
    nSex = user.whatIsSex(sex)
    nRelation = user.whatIsRelation(relation)
    age = str(age1) + '-' + str(age2)
    c = user(id, nSex, firtsName, lastName, nRelation, age)
    print(c.__dict__)








if __name__ == "__main__":
    token = "token"
    session = vk.AuthSession('id', 'log', 'pass')
    vk_api = vk.API(session)

user.userInfo(125,1,6, 19,1)
