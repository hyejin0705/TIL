import requests
from pprint import pprint

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
