import json
from pprint import pprint

# A. 제공되는 영화 데이터의 주요내용 수집 (problem_a)

def movie_info(movie):
    # movie_dict = {
    #     'genre_ids' : movie.get('genre_ids'),
    #     'id' : movie.get('id'), 
    #     'overview' : movie.get('overview'),        
    #     'poster_path' : movie.get('poster_path'), 
    #     'title' : movie.get('title'), 
    #     'vote_average' : movie.get('vote_average'), 
    # }

    movie_dict = {}
    info_lst = ['genre_ids', 'id', 'overview', 'poster_path', 'title', 'vote_average']
    for info in info_lst:
        movie_dict[info] = movie.get(info)
        
    return movie_dict 



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
