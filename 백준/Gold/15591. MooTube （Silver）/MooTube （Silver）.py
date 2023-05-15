import sys


# 연관된 비디오들을 확인하면서 추천되는 동영상의 수를 반환
def dfs(k, v):
    visited = [False] * (n + 1)  # 해당 비디오를 이미 추천했는지 여부 확인
    need_visit = [[v, 1000000000]]  # 연관된 비디오를 확인할 리스트 (초기에는 기준이 되는 비디오 번호와 임시 유사도(최대 유사도)를 추가합니다.)

	# 연관된 비디오를 순차적으로 확인하면서
    while need_visit:
        cv, usado = need_visit.pop()
        if not visited[cv] and usado >= k:  # 해당 비디오가 아직 추천되지 않았고, 그 비디오의 유사도가 K 보다 크거나 같은 경우
            visited[cv] = True  # 해당 비디오를 추천하고
            need_visit.extend(videos[cv])  # 그 비디오와 연관된 비디오들을 확인 리스트에 추가합니다.

    count = visited.count(True)  # 추천된 비디오의 수를 세서
    return count - 1  # 기준이 되었던 비디오를 뺀 나머지 추천 비디오 수를 반환합니다.


n, q = map(int, sys.stdin.readline().split())
videos = dict()
# 비디오의 연관 관계를 dictionary 형태로 저장
for _ in range(n-1):
    a, b, r = map(int, sys.stdin.readline().split())
    if a in videos.keys():
        videos[a].append([b, r])
    else:
        videos[a] = [[b, r]]

    if b in videos.keys():
        videos[b].append([a, r])
    else:
        videos[b] = [[a, r]]

answer = []
# 질문을 하나씩 확인하면서, dfs 를 수행하여 추천 비디오 수 저장
for _ in range(q):
    k, v = map(int, sys.stdin.readline().split())
    answer.append(dfs(k, v))

# 결과 출력
print('\n'.join(map(str, answer)))