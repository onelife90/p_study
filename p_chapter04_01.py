# Chapter04-01
# 시퀀스형
# what is python sequence
# https://docs.python.org/3/library/stdtypes.html

# python에서는 자료형을 두가지로 나눈다 (시퀀스형 / 비시퀀스형)
# 1.컨테이너(Container: 서로 다른 자료형[List, tuple, collections.deque])
container = [3, 3.0, 'a']
print(f"container:\t{container}\n")
# 2.플랫(Flat: 한개의 자료형[str, bytes, bytearray, array.array, memoryview])

# 추가 설명
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 리스트 및 튜플 고급
# 지능형 리스트(Comprehending Lists)
chars = '+_)(*&^$#@!)'
# chars[2] = 'h'  # TypeError: 'str' object does not support item assignment
code_list1 = []
print(f"every attributes of chars:\t{dir(chars)}\n")   # __iter__: 순회, 반환 가능(for문 등에서 사용 가능)

for s in chars:
    # 유니코드 리스트
    # ord(): 문자열을 유니코드로 변환하는 함수
    code_list1.append(ord(s))
print(f"ascii code of code_list1(empty list append):\t{code_list1}")   # ascii

# Comprehending Lists
# for문(append) 보다 속도가 우세
code_list2 = [ord(s) for s in chars]
print(f"list comprehension of code_list1:\t{code_list2}")

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
# filter(함수, 자료구조)
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

# 전체 출력
print(f"s > 40 in code_list3(for문):\t{code_list3}")
print(f"used filter def(lambda, map):\t{code_list4}\n")

print(f"string of code_list1(empty list append):\t{[chr(s) for s in code_list1]}")
print(f"string of code_list2(list comprehension):\t{[chr(s) for s in code_list2]}")
print(f"string of code_list3(s > 40 list comprehension):\t{[chr(s) for s in code_list3]}")
print(f"string of code_list4(used filter def){[chr(s) for s in code_list4]}\n")

# what is python generator
# https://bluese05.tistory.com/56
# 로컬 상태를 유지 (다음번에 반환할 값의 위치를 정확히 갖고 있다는 뜻)

# python generator strength
# https://niceman.tistory.com/137
# Generator 생성
import array

# Generator: 한 번에 한 개의 항목을 생성(메모리 유지X)
tuple_g = (ord(s) for s in chars)

print(f"tuple generator:\t{tuple_g}")
print(f"type of tuple generator:\t{type(tuple_g)}")
print(f"first element of tuple generator:\t{next(tuple_g)}")
print(f"second element of tuple generator:\t{next(tuple_g)}\n")

# 'I' = int type
array_g = array.array('I', (ord(s) for s in chars))
print(f"array generator:\t{array_g}")
print(f"type of array generator\t{type(array_g)}")
print(f"converting from array to list:\t{array_g.tolist()}\n")

# 제너레이터 예제
print(f"make students generator:\t{('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21))}")

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)):
    print(f"students generator(for문):\t{s}")

# 리스트 주의
# 깊은 복사 얕은 복사
# python shallow copy deep copy
# https://docs.python.org/3/library/copy.html
