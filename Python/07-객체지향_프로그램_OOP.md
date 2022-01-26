# 07-객체지향 프로그램 OOP

## 객체지향 프로그래밍(OOP)

- 프로그램을 여러 개의 독립된 개체들과 그 객체들 간의 상호작용을 파악하는 프로그래밍 방법

### 객체

- *파이썬은 모두 객체(Object)로 이루어져 있다.*

- *플라톤의 이데아 = 객체 라고 생각해보자. 눈에 보이는 사물 = 인스턴스*

- 객체는 특정 타입의 인스턴스(Instance)다.

  - `123, 900, 5`는 모두 `int`의 인스턴스
  - `'hello', 'bye'`는 모두 `string`의 인스턴스
  - `[232, 89], []`는 모두 `list`의 인스턴스

- 특징

  - 타입: 어떤 연산자(operator)와 조작(method)이 가능한가?
  - 속성(attribute): 어떤 상태(`데이터`)를 가지는가?
  - 조작법(method): 어떤 행위(`함수`)를 할 수 있는가?
  - `객체 = 속성(attribute) + 기능(method)`

  예시) sorted() vs .sort() 비교 - 전자는 절차지향, 후자는 객체지향

```python
# 절차지향
a = [1, 2, 3]
a = sorted(a)
a = reversed(a)
# a는 계속 흘러다닐 수밖에 없음
def append(1, value):
    return 1 + [value]
a = append(a, 4)
```

```python
# 객체지향
a = [1, 2, 3]
a.sort()
a.reverse()
# a를 본인 스스로 변화시킬 수 있음
a.append(4)
```

```python
class Person:
    
    def greetiing(self):
        print('안녕, 난 ' + self.name + '이라고해~')
        
Jimin = Person()
jimin.name = '지민'
jimin.greeting()
# 안녕 난 지민이라고해~
```

```python
# 절차지향
def area(x, y):
    return x * y
def circumference(x, y):
    return 2 * (x + y)
a, b = 10, 30
c, d = 300, 20
sq1_area = area(a, b)
sq1_circumference = circumference(a, b)
sq2_area = area(c, d)
sq2_circumference = circumference(c, d)
```

```python
# 객체지향
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
    def circumference(self):
        return 2 * (self.x + self.y)
    
r1 = Rectangle(10, 30)
r1.area()
r1.circumference()

r2 = Rectangle(300, 20)
r2.area()
r2.circumference()
```

### OOP기초

#### 기본 문법

- 클래스 정의 `class Myclass:`
- 인스턴스 생성 `my_instance = Myclass()`
- 메소드 호출 `my_instace.my_method()`
- 속성 `my_instance.my_attribute` ex) `복소수.real, 복소수.imag`

#### 클래스와 인스턴스

- 클래스: 객체들의 분류
- 인스턴스: 하나하나의 실체/예

#### 속성

- 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미

#### 메소드

- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)

#### 객체 비교하기

- ==
  - 변수가 **참조하는** 객체가 동등한(내용이 같은) 경우 True
- is
  - 변수가 동일한 객체를 **가리키는** 경우 True

```python
a = [1, 2, 3]
b = [1, 2, 3]
a is b  # False
a == b  # True
```

```python
a = [1, 2, 3]
b = a
a is b  # True
a == b  # True
```

### 인스턴스

#### 인스턴스 변수

- 각 인스턴스들의 고유한 변수 
- 생성자 메소드에서 self.\<name>으로 정의
- 생성 이후, \<instance>.\<name>으로 접근 및 할당

#### 인스턴스 메소드

- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
- 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

##### self

- 인스턴스 자기자신
- 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 자기자신이 전달되게 설계
- self는 바꿀 수 있으나 바꾸지 말 것을 권장(암묵적인 규칙)

#### 생성자(constructor) 메소드

- 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
- 인스턴스 변수들의 초기값을 설정
  - 인스턴스 생성
  - `__init__` 메소드 자동호출

```python
class Person:
    def __init__(self, name, age):
        # 인스턴스 변수를 정의하기 위해 사용
        self.name = name
        self.age = age
p1 = Person('lee', 20)
print(p1.name, p1.age)
# lee 20        
```

#### 소멸자(desturctor) 메소드

- 인스턴스 객체가 소멸되기 직전에 호출되는 메소드
- `__del__`
- `del <instance>` 이후에는 instance에 부여한 값이 사라짐

#### 매직 메소드

- 특정 상황에 자동으로 불리는 메소드
- `__str__(self), __repr__(self), __gt__(self, other)` 등

### 클래스

#### 클래스 변수

- 한 클래스의 모든 인스턴스라도 똑같은 갑을 가지고 있는 속성
- 클래스 선언 내부에서 정의

#### 클래스 메소드

- 클래스가 사용할 메소드
- @(데코레이터)를 사용해 정의: `@classmethod`

#### 스태틱 메소드

- 클래스가 사용할 메소드
- @staticmethod
- 호출 시, **어떠한 인자도 전달되지 않음**(클래스 정보에 접근/수정 불가)

예시)

```python
class Myclass:
    # 인스턴스를 조작하고 싶다
    # 함수 내부에 인스턴스를 던져주도록 설계
    # 매서드를 정의할 때 self로 받도록
    def instance_method(self):
        return self
    
    var = '클래스변수'    
    # 클래스를 조작하고 싶다
    # 함수 내부에 클래스를 던져주도록 설계
    # 매서드를 정의할 때 cls로 받도록
    @classmethod
    def class_method(cls):
        print(cls.var)
        return cls
    
    # 클래스나 인스턴스를 조작할 생각은 없는데 함수를 쓰고 싶다
    @staticmethod
    def static_method():
        return ''
```



## 객체지향의 핵심개념

### 추상화

- 종(class)
- 종 내 여러 개체들(instance)
- 그 특징과 행동을 정의(method, attitude)

### 상속

- 두 클래스 사이에 부모-자식 관계를 정립하는 것
- 클래스는 상속이 가능함
- `class ChildClass(ParentClass):`

예시)

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
        
class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    
    def talk(self):
        print(f'아.. 네.. 저는 {self.name}이에요...')
    
p1 = Professor('아이유', 30, '실용음악과')
s1 = Student('이우현', 31, 4.5)

p1.talk()  # 반갑습니다. 아이유입니다.
s1.talk()  # 아.. 네.. 저는 이우현이에요...
isinstance(p1, Person)  # True
isinstance(p1, Student)  # False
issubclass(p1, Person)  # True
```

- `super()`
  - 자식클래스에서 부모클래스를 사용하고 싶은 경우

```python
class Person:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number

class Student(Person):
    def __init__(self, name, age, number, student_id):
        super().__init__(name, age, number)  # name, age, number 정보 가져오기
        self.student_id = student_id
```

#### 다중 상속

- 둘 이상의 클래스를 상속받는 경우
- 상속받은 모든 클래스의 요소 활용 가능
- 중복 속성 혹은 메소드가 있는 경우, 상속 순서에 의해 결정

예시)

```python
class Person():
    def __init__(self, name):
        self.name = name
        
    def greeting(self):
        return f'안녕, {self.name}'
    
class Mom(Person):
    gene = 'XX'
    def swim(self):
        return '엄마 수영'

class Dad(Person):
    gene = 'XY'
    def walk(self):
        return '아빠 걷기'
    
class Baby(Dad, Mom):
    def swim(self):
        return '아이 수영'
    def cry(self):
        return '아이 울음'
    
baby = Baby('아가')
baby.cry()  # 아이 울음
baby.swim()  # 아이 수영
baby.walk()  # 아빠 걷기
baby1.gene()  # XY
```

#### mro 메소드

- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메소드
- 기존 인스턴스 - 자식 클래스 - 부모 클래스 순으로 확장

```python
Baby.mro()
# [__main__.Baby, __main__.Dad, __main__.Mom, __main__.Person, object]
```

### 다형성(메소드 오버라이딩)

- 같은 메소드가 클래스에 따라 다른 행동을 할 수 있음
- 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 다른 방식으로 응답할 수 있음
- 상속받은 메소드를 재정의(덮어쓰기)

### 캡슐화

- 객체의 일부 구현 내용에 대해 외부로부터 직접적인 액세스를 차단 ex)주민등록번호
- 파이썬에서 암묵적으로 존재하지만 언어적으로는 존재하지 않음

#### 접근제어자

##### Public Access Modifier

- 언더바가 없이 시작하는 메소드나 속성
- 어디서나 호출이 가능
- 하위클래스 오버라이드 허용

##### Protected Access modifier

- 언더바 1개로 시작하는 메소드나 속성
- 부모 클래스와 자식 클래스에서만 호출 가능(암묵적 약속)
- 하위클래스 오버라이드 허용

##### Private Access Modifier

- 언더바 2개로 시작하는 메소드나 속성
- 본 클래스 내부에서만 사용 가능
- 하위클래스 상속 및 호출 불가능(오류)
- 외부 호출 불가능(오류)

##### getter 메소드와 setter 메소드

- 변수에 접근할 수 있는 메소드를 별도로 생성
  - getter 메소드: 변수의 값을 읽는 메소드
    - @property 
  - setter 메소드: 변수의 값을 설정하는 성격의 메소드
    - @변수.setter 

```python
# OOP2 파이썬 공통 자료 참고
class Person:
    def __init__(self, age):
        self.age = age
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self):
        self._age = self._age - 10
```

