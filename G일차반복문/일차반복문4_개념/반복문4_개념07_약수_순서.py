'''
[문제]
	75의 약수 중에서 작은 수부터 큰 수를 출력했을 때, 
	다섯 번째 약수만 출력하시오.
[정답]
	25
'''

print('===[2023-01-23 (월) #01]===')

num = 75
count = 0

i = 1
while i <= num:
	if num % i == 0:
		count += 1
	if count == 5:
		print(i)
		break
	i += 1

# print("===[정답풀이]===")

# count = 0

# i = 1
# while i <= 75:
# 	if 75 % i == 0:
# 		count += 1

# 		if count == 5:
# 			print(i)
# 	i += 1


