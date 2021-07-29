# Chapter03-02
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Ieterator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# what is python special method
# https://docs.python.org/3/reference/datamodel.html

# 기본형
print(f"type of int:\t{int}")
print(f"type of float:\t{float}\n")

# 모든 속성 및 메소드 출력
print(f"every attributes of int:\t{dir(int)}")
print(f"every attributes of float:\t{dir(float)}\n")


ten = 10

print(f"type of ten:\t{type(ten)}")
print(f"ten + 100:\t{ten + 100}")
print(f"ten.__add__(100):\t{ten.__add__(100)}\n")
# print(n.__doc__)
print(f"boolean of ten:\t{ten.__bool__(), bool(ten)}")
print(f"ten * 100:\t{ten * 100, ten.__mul__(100)}\n")

# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info: {}, {}'.format(self._name, self._price)

    def __add__(self, x):
        print('Called >> __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('Called >> __sub__')
        return self._price - x._price

    def __le__(self, x):
        print('Called >> __le__')
        if self._price <= x._price:
            return True
        else:
            return False


# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(f"orange + banana:\t{s1 + s2}\n")

# 일반적인 계산
# print(s1._price + s2._price)

# 매직메소드
print(f"orange >= banana?:\t{s1 >= s2}")
print(f"orange <= banana?:\t{s1 <= s2}\n")
print(f"orange - banana:\t{s1 - s2}")
print(f"banana - orange:\t{s2 - s1}\n")
print(f"info of orange:\t{s1}")
print(f"info of banana:\t{s2}\n")
