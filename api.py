# -*- enconding: UTF-8 -*-
import requests
from datetime import date

def dia_um_mes_atras():
    hoje = date.today()
    passado = date.fromordinal(hoje.toordinal()-30) 
    return passado

def hoje():
    return date.today()



params = {
	'api_key': '8c348d8df5000d4848560eee211505ca',
	'sort_by': 'popularity.desc',
	'language': 'pt',
	'primary_release_date.gte': dia_um_mes_atras(),
	'primary_release_date.lte': hoje()
}

response = requests.get("http://api.themoviedb.org/3/discover/movie", params=params)
filmes = response.json()
principais_filmes = filmes['results'][:10]
for filme in principais_filmes:
    print(filme['title'])