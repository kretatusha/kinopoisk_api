import requests
import random
import urllib.parse

headers = {'accept': 'application/json', 'X-API-KEY': 'b847aebd-dfb9-48ed-ae8a-860d61cc28d3'}


def info_about_film(film):
    if 'nameRu' in film:
        print(film['nameRu'])
    else:
        print(film['nameEn'])
    print('Год:{0}'.format(film['year']))
    genres = "Жанр(ы): "
    for i in film['genres']:
        genres += i['genre'] + " "
    print(genres)
    print("Рейтинг: {0}".format(film['rating']))
    print('Ссылка на фильм: https://www.kinopoisk.ru/film/{0}/'.format(film['filmId']))


def get_answer():
    print('Сегодня вы будете смотреть...')
    response = requests.get("https://kinopoiskapiunofficial.tech/api/v2.2/films/top?type=TOP_250_BEST_FILMS&page=13",
                            headers=headers)
    pageCount = response.json()['pagesCount']
    page = random.randint(1, pageCount)
    response = requests.get(
        'https://kinopoiskapiunofficial.tech/api/v2.2/films/top?type=TOP_250_BEST_FILMS&page=' + str(page),
        headers=headers)
    film = random.choice(response.json()['films'])
    info_about_film(film)


def search(film):
    response = requests.get(
        'https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword=' + urllib.parse.quote_plus(
            film) + '&page=1', headers=headers)
    answer = response.json()
    if answer['searchFilmsCountResult'] == 0:
        print('К сожалению мы ничего не нашли')
    else:
        films = answer['films']
        for i in range(min(10, answer['searchFilmsCountResult'])):
            film = films[i]
            info_about_film(film)
            print('\n')


if __name__ == "__main__":
    while True:
        print('Для того, чтобы найти фильм напишите 1, если не знаете, что хотите найти - напишите 2')
        answer = input()
        if answer == '1' or answer == '2':
            break
        print('Не поняли, что вы хотите')
    if answer == '1':
        print('Напишите фильм и если вы знаете год его создания')
        search(input())
    else:
        get_answer()
