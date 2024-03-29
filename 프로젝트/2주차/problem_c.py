import requests
from pprint import pprint

# from problem_b import vote_average_movies
# 이건 왜??


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
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
    