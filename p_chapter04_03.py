# Chapter04-03
# 시퀀스형
# 1.컨테이너(Container: 서로 다른 자료형[List, tuple, collections.deque])
# 2.플랫(Flat: 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 해시테이블
# what is python hashtable
# https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm

# Key에 Value를 저장하는 구조
# 파이썬 dict 해시테이블 예
# 키 값의 연산 결과에 따라 직접 접근 가능한 구조
# key 값을 해싱 함수 -> 해시 주소 -> key에 대한 value 참조

# Dict 구조
# print(__builtins__.__dict__)        # key-value pair

# what is python hash
# https://www.edureka.co/blog/hash-in-python/#WhatIsHashMethodInPython?
# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(f"hash value of t1(immutable tuple):\t{hash(t1)}\n")
# print(f"hash value of t2(mutable list)\t{hash(t2)}")                     # TypeError: unhashable type: 'list'

# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for key, value in source:
    if key in new_dict1:
        new_dict1[key].append(value)
    else:
        new_dict1[key] = [value]
print(f"no use setdefault:\t{new_dict1}")

# Use Setdefault
for key, value in source:
    new_dict2.setdefault(key, []).append(value)
print(f"use setdefault:\t{new_dict2}")

# 주의
new_dict3 = {key:value for key, value in source}
print(f"duplicated and overwritten:\t{new_dict3}\n")
