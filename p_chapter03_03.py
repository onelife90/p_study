# Chapter03-03
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Ieterator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# what is python special method
# https://docs.python.org/3/reference/datamodel.html

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(f"distance between two points(index):\t{l_leng1}")

# 네임드 튜플 사용
# what is python namedtuple
# https://docs.python.org/ko/3.7/library/collections.html
# https://www.geeksforgeeks.org/namedtuple-in-python/

from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# print(pt3)
# print(pt4)

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(f"distance between two points(element):\t{l_leng2}\n")

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True)    # Default = False

# 출력
print(f"what is namedtuple:\t{Point1, Point2, Point3, Point4}\n")

# Dict to Unpacking
temp_dict = {'x':75, 'y':55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)

print(f"Point1:\t{p1}")
print(f"Point2:\t{p2}")
print(f"Point3:\t{p3}")
# rename 테스트
print(f"Point4(rename):\t{p4}")             # 중복, 예약어 난수로 표현
print(f"Point5(Dict to Unpacking):\t{p5}")

# 사용
print(f"10 + 40 (index) = \t{p1[0] + p2[1]}")
print(f"10 + 40 (element) = \t{p1.x + p2.y}\n")

# Unpacking
x, y = p3
print(f"Point3.x = 45, Point3.y = 20:\t{x, y}\n")

# 네임드 튜플 메소드
temp = [52, 38]

# _make(): 새로운 객체 생성
p4 = Point1._make(temp)
print(f"new object of Point1:\t{p4}")

#_fields: 필드 네임 확인
print(f"fields name:\t{p1._fields, p2._fields, p3._fields}\n")

# _asdict(): orderedDict 반환
print(f"orderedDict of Point1:\t{p1._asdict()}")
print(f"orderedDict of Point4:\t{p4._asdict()}\n")
