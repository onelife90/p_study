# Chapter04-04
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# immutable Dict
from types import MappingProxyType

d = {'key1':'value1'}

# Read Only
d_frozen = MappingProxyType(d)
print("dict: {}, id of dict: {}".format(d, id(d)))                                        # hash(d) TypeError: unhashable type: 'dict'
print("read only dict: {}, id of read only dict: {}".format(d_frozen, id(d_frozen)))      # hash(d) TypeError: unhashable type: 'dict'

# 수정 불가
# d_frozen['key2'] = 'value2'     # TypeError: 'mappingproxy' object does not support item assignment

# 수정 가능
d['key2'] = 'value2'
print("edit dict: {}\n".format(d))

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

s1.add('Melon')
print(f"not duplicated set add Melon:\t{s1}")

# 추가 불가
# s5.add('Melon')     # AttributeError: 'frozenset' object has no attribute 'add'

print("not duplicated set(s1): {}, type of s1: {}".format(s1, type(s1)))
print("not duplicated set(s2): {}, type of s2: {}".format(s2, type(s2)))
print("set(s3): {}, type of s3: {}".format(s3, type(s3)))
print("empty set(s4): {}, type of s4: {}".format(s4, type(s4)))
print("frozenset(s5): {}, type of s5: {}".format(s5, type(s5)))

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis

print('----------')
print(dis('{10}'))
print('----------')
print(dis('set([10])'))

# 지능형 집합(Comprehending Set)
print('--------')

from unicodedata import name

print({name(chr(i), '') for i in range(0,256)})
