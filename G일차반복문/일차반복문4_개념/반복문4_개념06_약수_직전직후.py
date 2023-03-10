'''
[문제] 
    280의 약수 중에
    50바로 전의 값과 바로 뒤의 값을 구하시오.
    만약 50이 약수이면, 바로 뒤의 값은 50이다.
[정답]
    40
    56
'''

print('===[2023-01-23 (월) #01]===')

num = 280
i = 1
while i <= num:
    if num % i == 0:
        if i < 50:
            front = i
        if i > 50:
            back = i
            break
    i += 1

print(front, back)


# print("===[정답풀이]===")

# front = 0
# back = 0

# i = 1
# while i <= 280:
#     if 280 % i == 0:
#         if i < 50:
#             front = i
#         if i >= 50 and back == 0:
#             back = i
#     i += 1

# print(front)
# print(back)



