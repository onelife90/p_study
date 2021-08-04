# Chapter04-02
# 시퀀스형

# python에서는 자료형을 두가지로 나눈다 (시퀀스형 / 비시퀀스형)
# 1.컨테이너(Container: 서로 다른 자료형[List, tuple, collections.deque])
# 2.플랫(Flat: 한개의 자료형[str, bytes, bytearray, array.array, memoryview])

# 추가 설명
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking
# b, a = a, b

# divmod(): 몫과 나머지 반환하는 함수
print(f"share, division of tuple(100/9):\t{divmod(100, 9)}")

# 인자가 튜플이면 앞에 asterisk(*) 붙여서 Unpacking
# what is python asterlisk
# https://mingrammer.com/understanding-the-asterisk-of-python/
print(f"used asterisk to tuple(100/9):\t{divmod(*(100, 9))}")
# print(divmod((100, 9)))         # TypeError: divmod expected 2 arguments, got 1
print(f"used asterisk to 100/9 result(tuple):\t{*(divmod(100,9)),}\n")      # (*tuple, ) = Unpacking

# x, y, rest = range(10)          # ValueError: too many values to unpack (expected 3)
x, y, *rest = range(10)
print("make list to rest vlaues(2~9):\t {}, {}, {}".format(x, y, rest))
x, y, *rest = range(2)
print("make list to rest vlaues(None):\t {}, {}, {}".format(x, y, rest))
x, y, *rest = 1, 2, 3, 4, 5
print("make list to rest vlaues(3~5):\t {}, {}, {}\n".format(x, y, rest))

# Mutable(가변) vs Immutable(불변)
immutable = (5, 20, 25)
mutable = [15, 20, 25]
print("immutable tuple value, immutable tuple id:\t {}, {}".format(immutable, id(immutable)))   # tuple(immutable)
print("mutable list value, mutable list id:\t {}, {}\n".format(mutable, id(mutable)))

immutable = immutable * 2
mutable = mutable * 2
print("immutable tuple value, immutable tuple id:\t {}, {}".format(immutable, id(immutable)))   # tuple(immutable)
print("mutable list value, mutable list id:\t {}, {}\n".format(mutable, id(mutable)))

immutable *= 2
mutable *= 2
print("immutable tuple value, immutable tuple id:\t {}, {}".format(immutable, id(immutable)))   # tuple(immutable)
print("mutable list value, mutable list id:\t {}, {}\n".format(mutable, id(mutable)))           # list(mutable) assignment

# 위 예제에서 알 수 있듯이 효율적인 메모리 공간을 위해서 python list 상당 부분 사용
