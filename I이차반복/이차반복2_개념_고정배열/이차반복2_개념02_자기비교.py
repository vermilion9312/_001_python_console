'''
	[문제]
		a리스트는 철수 반 중간고사 점수이다. 
		각 학생들이 다른 학생들과 비교하여 자기보다 크거나 같은 점수를 출력하시오.
	[예시]
		10 보다 큰 점수는 54, 90, 20 이다.
		54 보다 큰 점수는 90 이다.
		90 보다 큰 점수는 없다.
		20 보다 큰 점수는 54, 90 이다. 
'''
a = [10, 54, 90, 20]

print('===[2023-01-30 (월)]===')

for i in range(len(a)):
	print(a[i], "보다 큰 점수는 ", end = "")
	for j in range(len(a)):
		if i != j and a[i] <= a[j]:
			print(a[j], end = " ")
	print()


# print('===[정답풀이]===')
# for i in range(len(a)):
# 	for j in range(len(a)):
# 		if i != j and a[i] <= a[j]: # 본인 인덱스는 제외해야 한다.
# 			print(a[j] , end=" ")
# 	print()