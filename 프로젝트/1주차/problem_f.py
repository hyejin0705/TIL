import json
from pprint import pprint

# 1. 90년대 개봉작 중 많은 수입을 올린 영화 순위
# "release_date": "1995-01-28"

def max_90s_revenue(movies_list):
    movie_90s_id = []
    movie_title = []
    for movies in movies_list:
        movies_date = movies.get("release_date")
        if movies_date[2:3] == '9':
            movie_90s_id.append(movies.get('id'))
            movie_title.append(movies.get('title'))

    movie_dict= {}
    for idx, movie in enumerate(movie_90s_id):
        movies_json = open(f'data/movies/{movie}.json', encoding='utf-8')
        movies_dict = json.load(movies_json)

        movie_dict[movie_title[idx]] = movies_dict.get("revenue")

    rank_movies = dict(sorted(movie_dict.items(), key = lambda x: x[1], reverse=True))

    return rank_movies
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    rank_dict = max_90s_revenue(movies_list)
    print('-'*45)
    print(' 90년대 개봉작 중 많은 수입을 올린 영화 순위')
    print('-'*45)
    rank = 1
    for key, value in rank_dict.items():
        print(f'{rank}위. {key} - 수입 : {value}')
        rank += 1


# 2. 배급한 영화가 많은 순으로 배급사 정렬하기

def max_company(movies_list):
    company_lst = []
    for movie in movies_list:
        movie_id = movie.get('id')
        
        movies_json = open(f'data/movies/{movie_id}.json', encoding='utf-8')
        movies_dict = json.load(movies_json)

        company_info = movies_dict.get("production_companies")
        for idx in range(len(company_info)):
            company_lst.append(company_info[idx]["name"])

    company_dict = {}
    for company in company_lst:
        company_dict[company] = company_lst.count(company)
    
    rank_company = dict(sorted(company_dict.items()))
    rank_company = dict(sorted(rank_company.items(), key = lambda x: x[1], reverse=True))

    return rank_company


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    rank_dict = max_company(movies_list)
    print('-'*45)
    print('         배급한 영화가 많은 배급사')
    print('-'*45)
    rank = 1
    
    for key, value in rank_dict.items():
        print(f'{rank}위. {key} - {value}개 영화')
        rank += 1
