import json

# E. 알고리즘을 사용한 데이터 출력 (problem_e)
# 요구사항 : 12월에 개봉한 영화들의 제목 리스트를 출력하는 알고리즘을 작성
# "release_date": "1995-01-28"

def dec_movies(movies_list):
    movie_title = []
    for movies in movies_list:
        movies_date = movies.get("release_date")
        if movies_date[5:7] == '12':
            movie_title.append(movies.get('title'))
    
    return movie_title


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
