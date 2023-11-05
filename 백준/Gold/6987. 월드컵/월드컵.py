def possible(n): #파라미터는 이번 함수에서 진행할 경기 인덱스
	global match_seq,team_lst
	# 모든 경기 다 수행 했을때 체크
	if n==15:
		flag = True
		for score in team_lst:
			if score[0]!=0 or score[1]!=0 or score[2]!=0:
				flag = False
				break
		
		return flag
	else:
		temp=False
		#승,무,패 모든 케이스
		for i in range(3):
			#불가능한 경우
			if team_lst[match_seq[n][0]][i]==0 or team_lst[match_seq[n][1]][2-i]==0:
				continue

			team_lst[match_seq[n][0]][i]-=1
			team_lst[match_seq[n][1]][2-i]-=1
			
			temp = possible(n+1)
			if temp: return True #가능한 케이스가 하나라도 있으면 더 볼 필요없음

			team_lst[match_seq[n][0]][i]+=1
			team_lst[match_seq[n][1]][2-i]+=1
		
		#다 불가능 할때
		return False

ans = []
match_seq = []
#경기 순서
for i in range(5):
	for j in range(i+1,6):
		match_seq.append((i,j))

for _ in range(4):
	temp = list(map(int,input().split()))
	team_lst = []
	
	for i in range(6):
		team_lst.append(temp[i*3:i*3+3])
	if possible(0):
		ans.append(1)
	else:
		ans.append(0)

print(*ans)