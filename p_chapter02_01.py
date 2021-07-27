#Chapter02-01
#객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩

# 차량1
car_company1 = 'Ferrari'
car_detail1 = [
    {'color':'white'},
    {'horsepower':400},
    {'prince':8000}
]

# 차량2
car_company1 = 'Bmw'
car_detail1 = [
    {'color':'Black'},
    {'horsepower':270},
    {'prince':5000}
]

# 차량3
car_company1 = 'Audi'
car_detail1 = [
    {'color':'Silver'},
    {'horsepower':300},
    {'prince':6000}
]

# 리스트 구조
# 관리하기가 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color':'white', 'horsepower':400, 'prince':8000},
    {'color':'Black', 'horsepower':270, 'prince':5000},
    {'color':'Silver','horsepower':300, 'prince':6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등

car_dicts = [
    {'car_company':'Ferrari', 'car_detail':{'color':'white', 'horsepower':400, 'price':8000}},
    {'car_company':'Bmw', 'car_detail':{'color':'Black', 'horsepower':270, 'price':5000}},
    {'car_company':'Audi', 'car_detail':{'color':'Silver', 'horsepower':300, 'price':6000}}

]

del car_dicts[1]
print(car_dicts)

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def __reduce__(self):
        pass

car1 = Car('Ferrari', {'color':'white', 'horsepower':400, 'price':8000})
car2 = Car('Bmw', {'color':'Black', 'horsepower':270, 'price':5000})
car3 = Car('Audi', {'color':'Silver', 'horsepower':300, 'price':6000})

print(f"car1:\t{car1}")
print(f"car2:\t{car2}")
print(f"car3:\t{car3}\n")

print(f"attribute of car1:\t{car1.__dict__}")
print(f"attribute of car2:\t{car2.__dict__}")
print(f"attribute of car3:\t{car3.__dict__}\n")

print(f"every attribute of instance:\t{dir(car1)}")

# 리스트 선언
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(f"car_list:\t{car_list}\n")

for x in car_list:
    print(f"reperenc of cars:\t{repr(x )}")
    print(f"string of cars:\t{x}\n")
