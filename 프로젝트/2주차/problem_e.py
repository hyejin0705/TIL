import requests
from pprint import pprint


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
