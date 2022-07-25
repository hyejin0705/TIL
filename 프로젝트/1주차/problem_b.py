import json
from pprint import pprint

# B. 제공되는 영화 데이터의 주요내용 수정 (problem_b)
# 요구사항 : genre_ids를 장르 이름 리스트 genre_names로 바꿔 반환하는 함수 생성

def movie_info(movie, genres):
    genre_ids = movie.get('genre_ids')
    genre_name = []
    for idx in range(len(genre_ids)):
        for genre_dict in genres:
            if genre_dict['id'] == genre_ids[idx]:
                genre_name.append(genre_dict['name'])

    movie_dict = {}
    movie_dict['genre_names'] = genre_name

    info_lst = ['id', 'overview', 'poster_path', 'title', 'vote_average']
    for info in info_lst:
        movie_dict[info] = movie.get(info)
        
    return movie_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
