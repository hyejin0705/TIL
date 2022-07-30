# pjt02

### 이번 plt를 통해 배운 내용
- TMDB 사이트에서 API 키를 요청하고 API를 통해 어떤 정보들을 어떻게 출력하는지 알아봄. 

- requests 모듈을 통해 API에 요청한 데이터 수집, 가공, 출력

- sorted(), .sort의 메서드에 대해 알아보고, 활용


## A. 인기 영화 조회 (problem_a)
- 요구 사항 
    1. requests 사용하여 TMDB에서 현재 인기있는 영화 목록 [(Get Popular)](https://developers.themoviedb.org/3/movies/get-popular-movies) 데이터를 요청.

    2. 응답 받은 데이터의 영화 개수를 반환


- 결과 

![](README.assets\problem_a.png)


- 문제 접근 방법 및 코드 설명:
    ```python
    def popular_count():
        # 현재 인기있는 영화 목록(Get Popular) 데이터 요청 url
        url = 'https://api.themoviedb.org/3/movie/popular?api_key=3cd8e0319cee80069c4b85f6cf42fded'

        # 지역, 언어를 한국으로 설정하기
        params = {'language' : 'ko',
                'region' : 'KR'}

        # 요청할 때, 옵션들을 사전형식(params)으로 생성하여 넣는다면
        #            주소 뒤에 &구분으로 옵션들이 들어간다.
        response = requests.get(url, params).json()

        # 'results'값들의 길이를 출력.
        return len(response.get('results'))


    # 아래의 코드는 수정하지 않습니다.
    if __name__ == '__main__':
        """
        popular 영화목록의 개수 반환
        """
        print(popular_count())   # 20
    ```


- 어려웠던 점 및 문제의 포인트
- 문제의 포인트 
    - requests를 통해 API로 요청한 데이터를 가져오는 방법

    - Json형식의 데이터에서 결과 부분만 뽑아서 결과의 개수를 도출하는 방법



## B. 특정 조건에 맞는 인기 영화 조회 1 (problem_b)
- 요구 사항 
    1. TMDB에서 현재 인기있는 영화 목록 [(Get Popular)](https://developers.themoviedb.org/3/movies/get-popular-movies) 데이터를 요청.

    2. 평점(vote_average)이 8점 이상인 영화 목록을 반환


- 결과 

![](README.assets\problem_b.png)


- 문제 접근 방법 및 코드 설명
    ```python
    def vote_average_movies():
        # 현재 인기있는 영화 목록(Get Popular) 데이터 요청 url
        url = 'https://api.themoviedb.org/3/movie/popular?api_key=3cd8e0319cee80069c4b85f6cf42fded'

        params = {'language' : 'ko',
                'region' : 'KR'}

        response = requests.get(url, params).json()

        movie_lst = response.get('results')

        result = []
        for movie_info in movie_lst:
            # 평점이 8점 이상이면 리스트에 추가.
            if movie_info.get('vote_average') >= 8:
                result.append(movie_info)

        return result


    # 아래의 코드는 수정하지 않습니다.
    if __name__ == '__main__':
        """
        popular 영화목록중 vote_average가 8 이상인 영화목록 반환
        (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
        """
        pprint(vote_average_movies())
    ```


- 어려웠던 점 및 문제의 포인트
- 문제의 포인트
    1. json으로 요청받은 데이터에서 평점관련 정보를 추출하는 방법.

    2. 평점이 8점 이상인 영화의 정보를 가져오는 방법.



## C. 다중 데이터 분석 및 수정
- 요구 사항 
    1. TMDB에서 현재 인기있는 영화 목록 [(Get Popular)](https://developers.themoviedb.org/3/movies/get-popular-movies) 데이터를 요청.

    2. 평점(vote_average)을 기준으로 평점이 높은 영화 5개의 정보를 리스트로 반환하는 함수 ranking을 작성

    3. sort 메서드 혹은 sorted 함수의 특정 파라미터를 이용


- 결과 

![](README.assets\problem_c.png)


- 문제 접근 방법 및 코드 설명
    ```python
    def ranking():
        # 현재 인기있는 영화 목록(Get Popular) 데이터 요청 url
        url = 'https://api.themoviedb.org/3/movie/popular?api_key=3cd8e0319cee80069c4b85f6cf42fded'

        params = {'language' : 'ko',
                'region' : 'KR'}

        response = requests.get(url, params).json()

        movie_lst = response.get('results')

        # sorted의 파라미터 : key(기준), reverse(역정렬 여부)
        # lambda x(movie_lst에서 한줄씩 가져와서) : 평점부분을 기준으로 잡기
        # reverse = True (내림차순으로 정렬)
        result = sorted(movie_lst, key = lambda x: x['vote_average'], reverse=True)

        return result[:5]  # 상위 5개 추출


    # 아래의 코드는 수정하지 않습니다.
    if __name__ == '__main__':
        """
        popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
        (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
        """
        pprint(ranking())
    ```


- 어려웠던 점 및 문제의 포인트
    - 어려웠던 점
        - sorted()와 .sort()에 대한 파라미터를 알아보기 위해 공식문서를 참고했는데, 설명이 이해되지 않아서, 구글링을 통한 key에 대한 정보를 파악했습니다.

    - 문제의 포인트
        1. 평점순으로 sorted()와 .sort()의 파라미터를 활용하여 정렬하는 방법
        
        2. 평점 순으로 정렬된 리스트에서 상위 5개만 출력하는 방법


## D. 알고리즘을 사용한 데이터 출력
- 요구 사항 
    1. 제공된 영화 제목으로 TMDB에서 영화를 검색[(Search Movies)](https://developers.themoviedb.org/3/search/search-movies)

    2. 첫번째 영화의 id 값을 찾아 해당 영화에 대한 추천 영화 목록 [(Get Recommendations)](file:///C:/Users/multicampus/Desktop/ssafy08/pjt/pjt02/02_pjt_readme.pdf)를 수집

    3. 추천 영화 목록을 구하는 함수를 작성하시오.


- 결과 
![](README.assets\problem_d.png)


- 문제 접근 방법 및 코드 설명
    ```python
    def recommendation(title):
        # 영화를 검색(Search Movies)하는 url
        url = 'https://api.themoviedb.org/3/search/movie?api_key=3cd8e0319cee80069c4b85f6cf42fded'

        params = {'language' : 'ko',
                'query' : title, 
                'region' : 'KR'}

        response = requests.get(url, params).json()

        movie_lst = response.get('results')

        if movie_lst:
            # 영화의 id 값을 찾아서 movie_id에 넣어줌
            movie_id = movie_lst[0]['id']
            
            # 해당 영화에 대한 추천 영화 목록(Get Recommendations) 요청 url
            url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=3cd8e0319cee80069c4b85f6cf42fded'
            
            params = {'language' : 'ko'}

            recommend_response = requests.get(url2, params).json()
            
            result = recommend_response.get('results')

            # 결과값이 존재한다면, 영화 제목들을 리스트에 추가하여 출력
            if result:
                recommend_movie = []
                for idx in range(len(result)):
                    recommend_movie.append(result[idx].get('title'))
                    
                return recommend_movie

            # 추천영화가 존재하지 않으면 그냥 빈 리스트 출력
            else:
                return result

        # 검색한 영화 정보가 없다면 None를 반환.
        else:
            return None


    # 아래의 코드는 수정하지 않습니다.
    if __name__ == '__main__':
        """
        제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
        추천 영화가 없을 경우 []를 반환
        영화 id 검색에 실패할 경우 None을 반환
        (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
        """
        pprint(recommendation('기생충'))
        # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
        pprint(recommendation('그래비티'))
        # []
        pprint(recommendation('검색할 수 없는 영화'))
        # None
    ```

- 어려웠던 점 및 문제의 포인트
    - 어려웠던 점
        - 세가지의 제약조건이 존재하는데 그에 대한 데이터들이 어떻게 출력되는지 계속 확인해야 해서 힘들었습니다.

    - 문제의 포인트
        - 데이터들이 각각 어떻게 출력되는지를 확인하고, 제약조건을 활용하는 방법.
        - 추천 영화 제목들만 모아서 출력하는 방법


## E. 다중 데이터 분석 및 수정
- 요구 사항 
    1. 제공된 영화 제목으로 TMDB에서 영화를 검색[(Search Movies)](https://developers.themoviedb.org/3/search/search-movies)하여 해당 영화에 대한 출연진과 스태프 목록(Get Credits) 데이터를 수집.

    2. 출연진은 cast_id 값이 10 미만인 출연진만 추출하며,
    연출진은 스태프 부서가 Directing인 데이터만 추출


- 결과 

![](README.assets\problem_e.png)


- 문제 접근 방법 및 코드 설명
    ```python
    def credits(title):
        # 영화 제목으로 영화를 검색(Search Movies) 정도를 요청하는 url
        url = 'https://api.themoviedb.org/3/search/movie?api_key=3cd8e0319cee80069c4b85f6cf42fded'

        params = {'language' : 'ko',
                'query' : title, 
                'region' : 'KR'}

        # 요청결과를 json으로 변경하여 가져옴
        response = requests.get(url, params).json()

        movie_lst = response.get('results')

        if movie_lst:
            movie_id = movie_lst[0]['id']
            
            # 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 요청하는 url
            url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=3cd8e0319cee80069c4b85f6cf42fded'

            params = {'language' : 'ko'}

            cast_response = requests.get(url2, params).json()
            
            # 출연진 이름을 담을 리스트 생성
            cast_result = cast_response.get('cast')

            # 연출진 이름을 담을 리스트 생성
            crew_result = cast_response.get('crew')

            actor = []
            for idx in range(len(cast_result)):
                # cast_id를 담은 변수 생성
                id = cast_result[idx].get('cast_id')

                # 배우이고, cast_id가 10미만인 출연진을 출력
                if id < 10:
                    actor.append(cast_result[idx].get('name'))


            director = []    
            for idx in range(len(crew_result)):
                # 부서에 대한 정보를 변수에 담음
                department = crew_result[idx].get('known_for_department')

                # 스태프의 이름을 변수에 담음
                name = crew_result[idx].get('name')
                
                # 스태프 부서가 Directing인 데이터 추출
                # 그리고, 리스트에 스태프의 이름이 없다면 리스트에 추가
                if (department == 'Directing') and (name not in director):
                        director.append(name)
            
            # 사전으로 담아서 출력
            cast = {'cast' : actor, 'directing' : director}

            return cast

        # 검색한 영화 정보가 없다면 None을 반환
        else:
            return None


    # 아래의 코드는 수정하지 않습니다.
    if __name__ == '__main__':
        """
        제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
        영화 id 검색에 실패할 경우 None을 반환
        """
        pprint(credits('기생충'))
        # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
        pprint(credits('검색할 수 없는 영화'))
        # None
    ```

- 어려웠던 점 및 문제의 포인트
    - 어려웠던 점
        - cast_id가 10미만인 사람들을 추출해야 하는데, credit_id로 적어서 str이랑 int는 비교할 수 없다는 에러가 나옴.
        
        - 요청받은 출연진 및 스태프의 목록이 너무 길어서 cast와 crew의 키값이 존재하는지 모르고 cast에서 연출진들의 이름을 출력함.

        - 출연진한테는 Acting이라는 department가 필요없는데 코드를 작성함.

        - 전체적으로 코드가 너무 길어서 
 
    - 문제의 포인트
        - 많은 양의 데이터 중에서 필요한 내용만 추출하는 방법
        
        - 여러 제약조건들을 저절하게 주는 방법

