import requests

# api_key=3cd8e0319cee80069c4b85f6cf42fded
# 'language' : 'ko'
# 'regions' : 'KR'

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
