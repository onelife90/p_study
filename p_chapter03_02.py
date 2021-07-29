# Chapter03-02
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Ieterator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# what is python special method
# https://docs.python.org/3/reference/datamodel.html

# 클래스 예제2
# 벡터(x,y) (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50,15)
# Max((5,10)) = 10

class Vector(object):
    def __init__(self, *args):
        '''
        Crate a vector, example: v = Vector(5, 10)
        '''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''Return the vector informations.'''
        return 'Vector(%r, %r)' %(self._x, self._y)

    def __add__(self, other):
        '''Return the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, num):
        '''Return the vector mul of self and num'''
        return Vector(self._x * num, self._y * num)

    def __bool__(self):
        return bool(max(self._x, self._y))

# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

# 매직메소드 출력
print(f"docstring of Class Vector:\t{Vector.__doc__}")        # Class Vector 이후에 docstring은 없으므로 None 출력
print(f"docstring of __init__:\t{Vector.__init__.__doc__}")   # __init__ 초기화 부분에 있는 docsting이기 때문에 접근법이 다르다
print(f"docstring of __repr__:\t{Vector.__repr__.__doc__}")
print(f"docstring of __add__:\t{Vector.__add__.__doc__}\n")

print(f"invoked instance:\t{v1, v2, v3}")
print(f"__add__ v1, v2:\t{v1 + v2}")
print(f"__mul__ v1, 3:\t{v1 * 3}")
print(f"__mul__ v2, 10:\t{v2 * 10}\n")
print(f"__bool__ v1, v2:\t{bool(v1), bool(v2)}")
print(f"__bool__ v3:\t{bool(v3)}\n")
