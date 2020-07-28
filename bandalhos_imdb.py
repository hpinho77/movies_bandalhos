import json
import requests
from bs4 import BeautifulSoup
from time import sleep

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getMovieData(data_url):
    r = requests.get(data_url)
    bs2 = BeautifulSoup(r.content, 'html.parser', from_encoding="utf-8")
    #print(bs2)

    for s in bs2.findAll('script', type='application/ld+json'):
        #print(s)
        json_data = json.loads(s.get_text())
        json_actors = json_data['actor']
        actors = ""
        if len(json_actors) > 0:
            for actor in json_actors:
                actors += actor['name'] + ","
            actors = actors[:-1]


        json_directors = json_data['director']
        directors = ""
        if type(json_directors) is list:
            for director in json_directors:
                directors += director['name'] + ","
            directors = directors[:-1]
        else:
            directors = json_data['director']['name']

        json_genres = json_data['genre']
        genres = ""
        if type(json_genres) is list:
            for genre in json_genres:
                genres += genre + ","
            genres = genres[:-1]
        else:
            genres = json_data['genre']

        print('{}; {}; {}; {}; {}; {}; {}; {};'.format(
            json_data['name'], json_data['aggregateRating']['ratingValue'], data_url,
            json_data['duration'][2:], genres, directors, actors,
            json_data['description'], json_data['datePublished']))


def getalldata():
    fname = 'bandalhos_movies_2018.txt'
    with open(fname) as fp:
        data_url = fp.readline().strip()
        while data_url:
            #print(data_url)
            getMovieData(data_url)
            #sleep(1)  # Time in seconds.
            data_url = fp.readline().strip()


def main():
    #data_url = 'https://www.imdb.com/title/tt1974419'
    #data_url = 'https://www.imdb.com/title/tt4613272'
    #data_url = 'https://www.imdb.com/title/tt0475290/'
    #getMovieData(data_url)

    getalldata()


if __name__ == '__main__':
    main()





