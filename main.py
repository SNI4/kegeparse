import requests
from random import choice
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

user = UserAgent().random

def main(i):

    url = f'https://kompege.ru/api/v1/task?number={i}'

    task = choice((requests.get(url, headers={
        'User-Agent': user
    }).json()))

    text = BeautifulSoup(task["text"], "html.parser").text
    return f'-#-#-#-\nНомер задания: {task["number"]}, {task["comment"]}\n\n{text}\n\nОтвет: {task["key"]}\n'


if __name__ == '__main__':

    i = int(input('Введите номер задания: '))
    k = int(input('Сколько заданий показать?: '))

    for _ in range(k):
        print(main(i))