'''
	[문제]
		아래와 같이 구구단을 가로로 출력해보시오.
		2 * 1 = 2	3 * 1 = 3    ...  	9 * 1 = 9
		2 * 2 = 4  	3 * 2 = 6	 ...	9 * 2 = 18
		2 * 3 = 6  	3 * 3 = 9	 ...	9 * 3 = 27
		...      	...				    ...
		...      	...				    ...
		2 * 9 = 18	3 * 9 = 27 	 ...	9 * 9 = 81
'''

print('===[2023-01-30 (월)]===')

for i in range(1, 9 + 1):

	for j in range(2, 9 + 1):

		print(j, "*", i, "=", j * i, end = "\t")

	print()