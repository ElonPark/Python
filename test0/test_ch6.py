# 객체와 클래스
class Person():
    def __init__(self, name):
        self.name = name

hunter = Person("Elmer Fudd")
print('The mighty hunter: ', hunter.name)


class Car():
    def exclaim(self):
        print("I'm a Car!")



# class Yugo(Car):
#     pass

# Car 클래스 상속
class Yugo(Car):
    #exclaim 메소드 오버라이딩
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here?")


give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
give_me_a_yugo.need_a_push()

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Docter " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"


person = Person('Fudd')
docter = MDPerson('Fudd')
lawyer = JDPerson('Fudd')

print(person.name)
print(docter.name)
print(lawyer.name)

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)

# self 인자 사용
car = Car()
Car.exclaim(car)

# get/set 속성값과 프로퍼티
# 파이썬에서 모든 속성과 메소드는 public이다. 속성에 접근하는 것이 부담스럽다면 getter, setter 메소드를 작성할 수 있다.
# 그러나 파이써닉하게 프로퍼티를 사용하자
# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     def get_name(self):
#         print('inside the getter {0}'.format(self.hidden_name))
#         return self.hidden_name
#     def set_name(self, input_name):
#         print('inside hte setter {0}'.format(input_name))
#         self.hidden_name = input_name
#     # property의 첫번째 인자는 getter, 두번째는 setter이다.
#     # Duck객체의 naem을 참조할 때 get_name()메소드를 호출해서 hidden_name값을 반환한다.
#     name = property(get_name, set_name)
#
# fowl = Duck('Howard')
# print(fowl.name)
#
# fowl.get_name()
# fowl.name = 'Daffy'
# print(fowl.name)
# fowl.set_name('Daffy')
# print(fowl.name)


# 프로퍼티를 정의하는 다른 방법은 데커레이터를 사용하는 것이다.
# 각 메소드는 name()이지만, 서로 다른 데커레이터를 사용한다.
# getter 메소드 앞에 @property 데커레이터를 쓴다.
# setter 메소드 앞에 @name.setter 데커레이터를 쓴다
# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     @property
#     def name(self):
#         print('inside the getter {0}'.format(self.hidden_name))
#         return self.hidden_name
#     @name.setter
#     def name(self, input_name):
#         print('inside hte setter {0}'.format(input_name))
#         self.hidden_name = input_name
#
# fowl = Duck('Howard')
# print(fowl.name)
# fowl.name = 'Donald'
# print(fowl.name)

# 프로퍼티는 계산된 값을 참조할 수 있다.
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 7
# 속성에 대한 setter 프로퍼티를 명시하지 않는다면 외부로부터 이 속성을 설정할 수 없다.
# 이것은 read-only 속성이다.
print(c.diameter)

# 직접 속성을 접근하는 것보다 프로퍼티를 통해서 접근하면 큰 이점이있다.
# 만약 속성의 정의를 바꾸려면 모든 호출자를 수정할 필요없이 클래스 정의에 있는 코드만 수정하면 된다.

# private 네임 맹글링
# 파이썬은 클래스 정의 외부에서 볼 수 없도록 하는 속성에 대한 네이밍 컨벤션이 있다.
# 속성 이름 앞에 두 언더스코어(__)를 붙이면 된다.
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter {0}'.format(self.__name))
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside hte setter {0}'.format(input_name))
        self.__name = input_name


fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)
# 아무 문제도 없어 보이지만 __name속성을 바로 접근하지는 못한다.
# print(fowl.__name)
# 이 네이밍 컨벤션은 속성을 private로 만들지는 않지만, 파이썬은 이 속성이 우연히 외부 코드에서
# 발견할 수 없도록 이름을 맹글링(mangling)했다.

print(fowl._Duck__name)
# inside the getter를 출력하지 않았다. 이것이 속성을 완벽하게 보호할 수 없지만,
# 네임 맹글링은 속성의 의도적인 직접 접근을 어렵게 만든다.



# 클래스 정의에서 메소드의 첫 번째 인자가 self라면 이 메소드는 인스턴스 메소드이다.
# 이것은 일반적인 클래스를 생성할 때의 메소드 타입이다. 인스턴스 메소드의 첫 버째 매개변수는 self고,
# 파이썬은 이 메소드를 호출할 때 객체를 전달한다.

# 이와 반대로 클래스 메소드는 클래스 전체에 영향을 미친다.
# 클래스 정의에서 함수에 @classmethod 데커레이터가 있다면 이것은 클래스 메소드이다.
# 이 메소드의 첫 번째 매개 변수는 클래스 자신이다.
# 파이썬에서는 보통 이 클래스의 매개변수를 cls로 쓴다.
# class는 예약어이기 때문에 사용할 수 없다.
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()



# 덕 타이핑
# 파이썬은 다형성을 느슨하게 구현했다. 이것은 클래스에 상관없이 같은 동작을 다른 객체에 적용할 수 있다는 것을 의미한다.
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'say:', hunter.says())

hunter1 =  QuestionQuote('Bugs Bunny', "What's up Doc")
print(hunter1.who(), 'say:', hunter1.says())

hunter2  = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunter2.who(), 'say:', hunter2.says())



class BabbingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabbingBrook()


def who_says(obj):
    print(obj.who(), 'say:', obj.says())


who_says(hunter)
who_says(hunter1)
who_says(hunter2)
who_says(brook)


# 특수 메소드
class Word():
    def __init__(self, text):
        self.text = text

    # def equals(self, word2):
    #     return self.text.lower() == word2.text.lower()

    # __eq__는 파이썬의 특수 메소드이다.
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return "Word('" +  self.text + "')"


first = Word('ha')
second = Word('HA')
third = Word('eh')

# first.equals(second)
# first.equals(third)
first == second
first == third

first
print(first)


# 컴포지션
class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length


class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', self.bill.description, 'bill a', self.tail.length, 'tail')

tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()



# 네임드 튜플
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck  =  Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

# 딕셔너리에서 네임드 튜플 만들기
parts = {'bill' : 'wide orange', 'tail' : 'long'}
duck2 = Duck(**parts)
print(duck2)
# **parts는 키워드 인자다. parts 딕셔너리에서 키와 값을 추출하여 Duck()의 인자로 제공한다.
duck2 = Duck(bill = 'wide orange', tail = 'long')
# 네임드 튜플은 불변한다. 하지만 필드를 바꿔서 또 다른 네임드 튜플을 반환할 수 있다.
duck3 = duck2._replace(tail = 'magnificent', bill = 'crushing')
print(duck3)

duck_dict = {'bill' : 'wide orange', 'tail' : 'long'}
print(duck_dict)

duck_dict['color'] = 'green'
print(duck_dict)

# 딕셔너리는 네임드 튜플이 아니다
# duck.color = 'green'

 # -  네임드 튜플의 특징
 # 불변하는 객체처럼 행동한다.
 # 객체보다 공간 효율성과 시간 효율성이 더 좋다.
 # 딕셔너리 형식의 괄호([]) 대신, 점(.)표기법으로 속성을 접근할 수 있다.
 # 네임드 튜플을 딕셔너리의 키처럼 쓸 수 있다.






















# End
