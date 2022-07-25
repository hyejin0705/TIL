import json
from pprint import pprint

# C. 다중 데이터 분석 및 수정 (problem_c)
# 요구사항 : movies.json에 있는 평점이 높은 20개의 영화 데이터를 활용하여 영화목록을 생성


def movie_info(movies_list, genres_list):
    movie_list = []
    for movie in movies_list:
        genre_ids = movie.get('genre_ids')
        genre_name = []
        for idx in range(len(genre_ids)):
            for genre_dict in genres:
                if genre_dict['id'] == genre_ids[idx]:
                    genre_name.append(genre_dict['name'])

        movie_dict = {}
        movie_dict['genre_names'] = genre_name  # 장르 이름은 따로 생성
        
        # 나머지는 for문으로 자동 생성
        info_lst = ['id', 'overview', 'poster_path', 'title', 'vote_average']
        for info in info_lst:
            movie_dict[info] = movie.get(info)

        movie_list.append(movie_dict)  # 영화 정보를 하나의 리스트에 담기

    return movie_list
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))

    
