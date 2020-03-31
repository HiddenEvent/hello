# colors = ["a","b","c","d"]
# result = ''.join(colors)
# print(result)
#
# # result = ""
# # for s in colors:
# #     result +=s
# # print(result)
#
# # split 함수에 아무것도 없으면 빈칸을 기준으로 나눈다.
# items = 'zero one two three'.split()
# print(items)
#
# example = 'python,jquery,javascript'
# example.split(",")
# print(example)
#
# # 리스트에 있는 값을 a, b, c 변수로 unpacking 한다.
# a, b, c = example.split(",")

# colors = ['red', 'blue', 'green', 'yellow']
# result = ''.join(colors)
# print(result)
#
# ## join 하면서 추가 String을 붙일 수 있는 옵션을 부여 할 수 있음
# result = '-'.join(colors) # 연결 시 "-"로 연결
# print(result)

# # 일반적인 방법
# result = []
# for i in range(10): # range = 0~9
#     result.append(i)
# print(result)
#
# # List compreHensions 방법
# result = [i for i in range(10)]
# print(result)
# even = [i for i in range(10) if i % 2 == 0]
#
# # 중첩 List comprehensions
# word_1 = "Hello"
# word_2 = "World"
# wordCompare = [i+j for i in word_1 for j in word_2]
# # Nested For loop란 : for 내부에 for 루프가 있는 것
# print(wordCompare)

# 중첩 List comprehensions + if 문
# case_1 = ["A", "B", "C"]
# case_2 = ["D", "E", "A"]
#
# result = [[i+j for i in case_1]for j in case_2]
# print(result)

# if 문 추가
# result = [i+j for i in case_1 for j in case_2 if not(i==j)]
#
# print(result)

# for i, v in enumerate(['tic','tack','tok']):
# # list의 있는 index와 값을 unpacking
#     print(i,v)
#
# mylist = ['a','b','c','d']
# # list의 있는 index와 value를 unpacking하여 list로 저장
# enumList = list(enumerate(mylist))
# print(enumList)
#
# # 문장을 list로 만들고 list의 index와 값을 unpacking하여 dict로 저장
# test = {i:j for i, j in enumerate('Hellow World i\'m find thankyou and you?'.split())}
# print(test)

# alist = ['a1','a2','a3']
# blist = ['b1','b2','b3']
# for a, b in zip(alist, blist): # 병렬적으로 값을 추출
#     print(a,b)
#==== 출력 값====
# a1 b1
# a2 b2
# a3 b3

# 각 tuple의 값은 index끼리 묶음
# a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
# print(a,b,c)
# ==== 출력 값====
#(1, 10, 100) (2, 20, 200) (3, 30, 300)

#각 Tuple 같은 index를 묶어 합을 List로 변환
# zipTupleSum = [sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))]
# print(zipTupleSum)
# ==== 출력 값====
#[111, 222, 333]


alist = ['a1','a2','a3']
blist = ['b1','b2','b3']
for i, (a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)
# ==== 출력 값====
# 0 a1 b1
# 1 a2 b2
# 2 a3 b3