#Chapter02-02
#객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author: Kim
    Date: 2021.07.26
    """

    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self.car_count = 10
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        print("del?")
        Car.car_count -= 1

    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print('Car Detail Info: {} {}'.format(self._company, self._details.get('price')))

# self 의미
car1 = Car('Ferrari', {'color':'white', 'horsepower':400, 'price':8000})
car2 = Car('Bmw', {'color':'Black', 'horsepower':270, 'price':5000})
car3 = Car('Audi', {'color':'Silver', 'horsepower':300, 'price':6000})

# ID 확인
print(f"reference of car1:\t{id(car1)}")
print(f"reference of car2:\t{id(car2)}")
print(f"reference of car3:\t{id(car3)}\n")

print(f"Is same company name between car1 and car2?:\t{car1._company == car2._company}")   # False
print(f"Is same instance between car1 and car2?:\t{car1 is car2}\n")                     # False

# dir & __dict__ 확인
print(f"every attribute of instance car1:\t{dir(car1)}")
print(f"every attribute of instance car2:\t{dir(car2)}\n")

print(f"attribute of car1:\t{car1.__dict__}")
print(f"attribute of car2:\t{car2.__dict__}\n")

# Docstring
print(f"docsting of Class Car:\t{Car.__doc__}\n")

# 실행
car1.detail_info()
Car.detail_info(car1)
car2.detail_info()
Car.detail_info(car2)
print()

# 비교
print(f"what is car1, car2?:\t{car1.__class__, car2.__class__}")
print(f"Is same reference of class instance(car1, car2, car3)?:\t{id(car1.__class__), id(car2.__class__), id(car3.__class__)}\n")

# 에러
# Car.detail_info()

# 공유확인
print(f"car1 instance variable(car_count):\t{car1.car_count}")
print(f"car2 instance variable(car_count):\t{car2.car_count}\n")

print(f"attribute of car1:\t{car1.__dict__}")
print(f"attribute of car2:\t{car2.__dict__}\n")

print(f"every attribute of instance:\t{dir(car1)}\n")           # exist car_count

# 접근
print(f"car1 instance variable(car_count):\t{car1.car_count}")
print(f"Car Class variable(car_count):\t{Car.car_count}\n")     # __init__ Car.car_count += 1

del car2            # Method of del: __del__, so that print

# 삭제 확인
print(f"after delete car2, car1 instance variable(car_count):\t{car1.car_count}")
print(f"after delete car2, Car Class varicable:\t{Car.car_count}\n")

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래 변수))
