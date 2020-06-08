# 04_dict_and_set
# 1. dictionary
# key, value로 이루어 져 있음
dict_a = {}
dict_b = dict()
# key가 중복이 불가능 하다.
dict_a = {'삼성':100, '역삼':50, '삼성':30}
print(dict_a)
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())

print(dict_a['삼성'])
print(dict_a.get('삼성'))

# .get과 []접근 차이점
dict_a = {'삼성':100, '역삼':50}
print(dict_a.get('선릉'))
#print(dict_a['선릉'])

# 2. set
# set -> 순서가 없이 저장된다. key값도 순서가 없다.
set_a = {1, 2, 3}
set_b = {3, 6, 8}
print(set_a - set_b)
print(set_a | set_b)
print(set_a & set_b)

list_a = [1, 1, 1, 1]
print(list(set(list_a))[0])

string = "immutable"
list_a = ['imutable?', 'real?']

print(string[0])
print(list_a[0])
# string[0] = 'a'
list_a[0] ='mutable'
print(list_a)

# list_a 자체를 변경
list_a = ['mutable']

list_a = [3, 'real?']
list_b = list_a
print(id(list_a), id(list_b))
