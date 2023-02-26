#以Python爬蟲爬網站中有iron man關鍵字的筆數
import requests
import json
import math
from collections import Counter

OMDB_URL = 'http://www.omdbapi.com/?apikey=c5e25d97'

def get_data(url):
    re = requests.get(url)
    data = json.loads(re.text)
    if data['Response']== 'True':
        return data
    else:
        return None
    
def search_id_by_keyword(keyword):
    movie_ids=[]
    numpage = math.ceil(101/10)
    query = '+'.join(keyword.split())
    for i in range(1,numpage+1):
        url = OMDB_URL + '&s='+ query + '&page='+ str(i)
        data = get_data(url)
        if data:
            for j in data['Search']:
                movie_ids.append(j['imdbID'])
    return movie_ids

def search_by_id(movie_id):
    url = OMDB_URL + '&i=' + movie_id
    data = get_data(url)
    return data if data else None

keyword = 'iron man'
movie_ids = search_id_by_keyword(keyword)
movielist=[]
for m_id in movie_ids:
    movie = search_by_id(m_id)
    movielist.append(movie)
    
typelist = [m['Type'] for m in movielist if m['Type']!= 'N/A']
typedict = Counter(typelist)
for i in typedict:
     print('type:',i,'numbers:',typedict[i])
'''
type: movie numbers: 88
type: series numbers: 8
type: game numbers: 5
'''
    

            
            
            
    
