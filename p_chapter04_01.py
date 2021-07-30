# Chapter04-01
# 시퀀스형
# what is python sequence
# https://docs.python.org/3/library/stdtypes.html

# 컨테이너(Container: 서로 다른 자료형[List, tuple, collections.deque])
container = [3, 3.0, 'a']
print(container)

# 플랫(Flat: 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending Lists)
chars = '+_)(*&^$#@!)'
code_list1 = []

print(dir(chars))   # __iter__: 순회, 반환 가능(for문 등에서 사용 가능)
# chars[2] = 'h'  # TypeError: 'str' object does not support item assignment

for s in chars:
    # 유니코드 리스트
    # ord(): 문자열을 유니코드로 변환하는 함수
    code_list1.append(ord(s))

print(code_list1)   # ascii

# Comprehending Lists
code_list2 = [ord(s) for s in chars]
print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

# 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)

print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

# what is python generator
# https://bluese05.tistory.com/56
# python generator strength
# Generator 생성
import array

# Generator: 한 번에 한 개의 항목을 생성(메모리 유지X)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(tuple_g)
print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))

print(array_g)
print(type(array_g))
print(array_g.tolist())

# 제너레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)):
    print(s)
