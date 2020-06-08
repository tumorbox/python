# 01_operations.py
# 논리 연산자
# and, or, not
print("____and____")
print(True and True)
print(True and False)
print(False and False)
print(False and True)

print("____or____")
print(True or True)
print(True or False)
print(False or False)
print(False or True)

print("____not____")
print(not True)
print(not False)
print(not [])

# in, not in
print("_____")
print('a' in 'apple')
print(1 not in [1,2,3])


# 단축 평가
# or의 조건에 맞는 순간 연산이 종료되어서 Text만 출력된다.
print ('' or 'Text' or 'Text_2')
print ('Text' and '' or 'Text_2')

