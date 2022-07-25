# PJT 01

### 이번 plt를 통해 배운 내용
- json 파일을 가져와서(open), json.load를 통해 딕셔너리 형태로 변환하고 pprint이라는 출력함수를 통해 보기 편하게 읽는 방법을 배웠습니다.
- 딕셔너리 형태에서 정보를 가져오는 방법이 dict['key']라는 방법 뿐만 아니라, dict.get('key')라는 방법도 존재한다는 것을 배웠습니다.
- dict.key(), dict.values()에서는 인덱스로 정보를 가져오면 에러가 발생했음.

## A. 제공되는 영화 데이터의 주요내용 수집
- 요구 사항 
    1. movie.json에서 id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 값을 추출
    2. 새로운 dictionary로 반환하는 함수 movie_info 생성

- 결과 
    ![](README.assets\problem_a.png)

- 문제 접근 방법 및 코드 설명:
    ```python

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
        # 파일 내용을 가져오는 방법 : open
        movie_json = open('data/movie.json', encoding='utf-8')
        # json형태로 가져오는 방법 : json.load
        movie_dict = json.load(movie_json)
        
        # pprint : json이나 딕셔너리 형태를 보기 편하게 출력하는 함수
        #          key값은 무조건 왼쪽 정렬.
        pprint(movie_info(movie_dict))
    ```

- 어려웠던 점 및 문제의 포인트
    - 어려웠던 점
        - 처음에 그냥 정보를 하나씩 적었는데, 리스트에 가져올 정보를 적고 for문으로 반복해서 가져오는 방법을 한 번에 생각하지 못했음.
    - 문제의 포인트 
        - json파일을 가져와서 형태를 알아보고, 원하는 정보를 추출해서 출력하는 방법


## B. 제공되는 영화 데이터의 주요내용 수정
- 요구 사항 : genre_ids를 장르 이름 리스트 genre_names로 바꿔 반환하는 함수 생성

- 결과 
    ![](README.assets\problem_b.png)

- 문제 접근 방법 및 코드 설명
    ```python
    def movie_info(movie, genres):
        # ids가 리스트에 들어 있었기 때문에 그냥 변수에 넣기
        genre_ids = movie.get('genre_ids')
        genre_name = []

        # id를 하나씩 가져와서 genres.json에서 장르 이름을 가져오기
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
            
        return movie_dict

    # 아래의 코드는 수정하지 않습니다.
    if __name__ == '__main__':
        movie_json = open('data/movie.json', encoding='utf-8')
        movie = json.load(movie_json)

        genres_json = open('data/genres.json', encoding='utf-8')
        genres_list = json.load(genres_json)

        pprint(movie_info(movie, genres_list))
    ```

- 어려웠던 점 및 문제의 포인트
    - 어려웠던 점
        1. id를 가지고 장르 이름을 가져올 때, `if id in genre_ids`로 장르이름을 가져왔는데, id의 순서와 장르 이름이 맞지 않아서 for문을 하나 더 생성해서 다시 가져왔음.
        - 이중 for문을 자제하려고 했는데 그 방법밖에 생각이 나지 않았음.

    - 문제의 포인트
        1. 문서의 정보를 가지고 다른 문서에서의 정보를 추출하는 방법
        2. 리스트에 id 순서에 맞는 장르 이름을 가져오는 방법


## C. 다중 데이터 분석 및 수정
- 요구 사항 : movies.json에 있는 평점이 높은 20개의 영화 데이터를 활용하여 영화목록을 생성

- 결과 
    ![](README.assets\problem_c.png)

- 문제 접근 방법 및 코드 설명
    ```python
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
    ```

- 어려웠던 점 및 문제의 포인트
    - 어려웠던 점
        1. 함수의 파라미터 이름이 movie, genre로 되어 있고, 함수 호출 인자에는 movies_list, genres_list로 되어 있어서 헷갈렸음.
        - 그래서, 파라미터 이름과, 호출인자 이름을 하나로 통일.
        - 호출인자로 통일한 이유는 변수명에 list라는 자료형을 표시해서 뭐가 들어있는지 유추가능하기 때문에
    - 문제의 포인트
        - 문서의 정보를 가지고 다른 문서의 정보를 가져오는데, 앞선 문제와는 달리 for문을 통해서 여러가지의 똑같은 정보를 가지고 오는 방법 


## D. 알고리즘을 사용한 데이터 출력
- 요구 사항 : 모든 영화 중 가장 높은 수익을 낸 영화를 출력하는 알고리즘 작성


- 결과 
    ![](README.assets\problem_d.png)

- 문제 접근 방법 및 코드 설명
    ```python
    def max_revenue(movies_list):
        # 영화 이름과, 수입를 같이 가져오기 위해 빈 딕셔너리 생성
        movie_dict= {}
        for movie in movies_list:
            movie_title = movie.get('title')  # 영화이름 가져오기
            movie_id = movie.get('id')   # 영화 id 가져오기
            
            # 영화 id를 가지고 id.json 파일을 열고, 수입 정보 가져오기
            movies_json = open(f'data/movies/{movie_id}.json', encoding='utf-8')
            movies_dict = json.load(movies_json)

            movie_dict[movie_title] = movies_dict.get("revenue")

        # max() : 함수를 통해 최고 수입액을 찾음
        max_revenue = max(movie_dict.values())
        for title in movie_dict:
            # 최고 수입액과 맞는 값을 찾고, 그 키값인 영화제목 출력
            if movie_dict[title] == max_revenue:

                return title 
            

    # 아래의 코드는 수정하지 않습니다.
    if __name__ == '__main__':
        movies_json = open('data/movies.json', encoding='utf-8')
        movies_list = json.load(movies_json)
        
        print(max_revenue(movies_list))

    ```
- 어려웠던 점 및 문제의 포인트
    - 어려웠던 점
        1. json파일을 open하고 load까지 해야 읽을 수 있음.
            - open만 했더니 오류가 나옴.

        2. 딕셔너리에는 index, find를 통해 최고값을 가진 인덱스 번호를 출력할 수 없었기 때문에 for문과 if문을 통해 최고값과 값들을 비교하여 이름을 추출했음.
            - 위의 방법 말고 다른 방법이 있는지 추가적으로 알아보기

    - 문제의 포인트
        1. 영화들의 id들을 가져오고 id이름의 json파일을 가져오기.
            - f-string활용하여, 중간의 이름만 바꿔주기.
        2. 최고의 수입액을 가진 영화 제목을 출력하기


## E. 알고리즘을 사용한 데이터 출력
- 요구 사항 : 12월에 개봉한 영화들의 제목 리스트를 출력하는 알고리즘을 작성

- 결과
    ![](README.assets\problem_e.png)

- 문제 접근 방법 및 코드 설명
    ```python

    def dec_movies(movies_list):
        movie_title = []
        # 출시 날짜를 가져오기
        for movies in movies_list:
            movies_date = movies.get("release_date")
            # 12월(인덱싱으로 가져오기)에 개봉한 영화 제목 출력
            # "release_date": "1995-01-28"
            if movies_date[5:7] == '12':
                movie_title.append(movies.get('title'))
        
        return movie_title

    # 아래의 코드는 수정하지 않습니다.
    if __name__ == '__main__':
        movies_json = open('data/movies.json', encoding='utf-8')
        movies_list = json.load(movies_json)
        
        print(dec_movies(movies_list))
    ```
- 어려웠던 점 및 문제의 포인트
    - 어려웠던 점
        - 함수 파라미터와 호출인자 통일하기
    - 문제의 포인트
        - 개봉 날짜가 어떤 형식으로 되어 있는지 확인하고,
          개봉 날짜에서 월 부분에 해당하는 부분을 가져와서 12월에 개봉한 영화만 찾기


## F. 선택과제  
### 1. 90년대 개봉작 중 많은 수입을 올린 영화 순위
- 요구 사항 : 90년대 개봉작 중 많은 수입을 올린 영화 순위

- 결과 
    ![](README.assets\problem_f.png)

- 문제 접근 방법 및 코드 설명
    ```python

    def max_90s_revenue(movies_list):
        movie_90s_id = []  # 90년대 영화만 담을 리스트 생성
        movie_title = []   # 영화 제목 담을 리스트 생성

        for movies in movies_list:
            movies_date = movies.get("release_date")  # 개봉날짜 가져오기

            if movies_date[2:3] == '9':      # 년도의 3번째 자리가 9인 영화 찾기 
                movie_90s_id.append(movies.get('id'))
                movie_title.append(movies.get('title'))

        movie_dict= {}
        # id.json 파일에서 수입액 찾기
        # {영화 제목 : 수입액} 딕셔너리 생성
        for idx, movie in enumerate(movie_90s_id):
            movies_json = open(f'data/movies/{movie}.json', encoding='utf-8')
            movies_dict = json.load(movies_json)
            
            # id의 자리에 있는 영화제목 리스트에서 영화 제목을 가져와서 키값에 넣기
            movie_dict[movie_title[idx]] = movies_dict.get("revenue")

        rank_movies = {}
        # 딕셔너리의 정렬방법
        # value로 정렬하기 위해서 lambda 사용
        # lambda x : x[1]로 딕셔너리의 value 위치로 들어감
        # reverse = True : 내림차순으로 정렬, reverse의 기본값(False)
        rank_movies = dict(sorted(movie_dict.items(), key = lambda x: x[1], reverse=True))

        return rank_movies
            
    # 아래의 코드는 수정하지 않습니다.
    if __name__ == '__main__':
        movies_json = open('data/movies.json', encoding='utf-8')
        movies_list = json.load(movies_json)
        
        # 순위와 영화제목, 수입을 출력하기 위해 변수에 함수 값을 넣음.
        rank_dict = max_90s_revenue(movies_list)
        print('-'*45)
        print(' 90년대 개봉작 중 많은 수입을 올린 영화 순위')
        print('-'*45)

        # 순위는 직접 지정, for문이 돌면서 하나씩 추가
        rank = 1

        # dict.items()를 통해 key(영화제목), value(수입)을 꺼내옴.
        for key, value in rank_dict.items():
            print(f'{rank}위. {key} - 수입 : {value}')
            rank += 1
    ```
- 어려웠던 점 및 문제의 포인트
    - 어려웠던 점
        - 딕셔너리의 정렬할 때 lambda를 통해 value값을 가져와서 정렬하는 방법을 구글링을 찾음.
        - 순위도 출려하고 싶어서 enumerate를 사용하려고 했지만, dict.keys(), dict.values()에는 인덱스로 정보를 꺼내올 수가 없음.
            - 그래서, items()를 통해 key와 value를 가져오고, 순위는 직접 지정해줌.
    - 문제의 포인트
        - 딕셔너리의 값들을 내림차순으로 정렬하는 방법
        - 순위도 같이 출력하는 경우, 딕셔너리의 자료형에서 순위(인덱스 + 1), key(영화제목), value(수입)를 출력하는 방법
        

### 2. 배급한 영화가 많은 순으로 배급사 정렬하기
- 요구 사항 : 배급한 영화가 많은 순으로 배급사 정렬하기

- 결과 
    ![](README.assets\problem_f2.png)

- 문제 접근 방법 및 코드 설명
    ```python

    def max_company(movies_list):
        company_lst = []
        for movie in movies_list:
            movie_id = movie.get('id')
            
            movies_json = open(f'data/movies/{movie_id}.json', encoding='utf-8')
            movies_dict = json.load(movies_json)

            company_info = movies_dict.get("production_companies")
            for idx in range(len(company_info)):
                # 리스트에 배급사들 이름 리스트에 담기
                company_lst.append(company_info[idx]["name"])

        company_dict = {}
        for company in company_lst:
            # {배급사 : 배급사들이 언급된 수} 딕셔너리 생성
            # 딕셔너리의 키는 중복을 자동으로 제거함.
            company_dict[company] = company_lst.count(company)
        
        # 동순위일 경우 이름순으로 순위
        # 회사명으로 오름차순으로 정렬한 후
        rank_company = dict(sorted(company_dict.items()))
        # 영화 수대로 내림차순으로 정렬
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

    ```
- 어려웠던 점 및 문제의 포인트
    - 어려웠던 점
        - 배급한 영화의 수가 동일한 배급사들을 정렬하는 방법으로 회사명을 오름차순으로 정렬했는데, sorted를 두 번 사용해야 했음. (회사명 오름차순, 영화 수 내림차순)
            - pandas의 경우 정렬 기준을 2가지 정도 지정할 수 있는데, 딕셔너리의 경우에는 두번 연속으로 쓰는 방법밖에 없나???
        - 배급사의 영화명도 출력하려고 했지만, 시간부족으로 방법을 찾지 못함.
    - 문제의 포인트
        - 영화 정보에서 배급사의 이름을 가져와서 수를 세기.
        - 동순위의 경우 순위를 어떻게 정할지 고민.