import json

# D. 알고리즘을 사용한 데이터 출력 (problem_d)
# 요구사항 : 모든 영화 중 가장 높은 수익을 낸 영화를 출력하는 알고리즘 작성

def max_revenue(movies_list):
    movie_dict= {}
    for movie in movies_list:
        movie_title = movie.get('title')
        movie_id = movie.get('id')
        
        movies_json = open(f'data/movies/{movie_id}.json', encoding='utf-8')
        movies_dict = json.load(movies_json)

        movie_dict[movie_title] = movies_dict.get("revenue")

    max_revenue = max(movie_dict.values())
    for title in movie_dict:
        if movie_dict[title] == max_revenue:
            return title 
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
