# >>> def no_idea():
# ...     pass
# ...     return 'Huh?'
#  bestiary = defaultdict(no_idea)
#  from collections import defaultdict
# >>> periodi_table = defaultdict(int)
# >>> periodi_table['Hydrogen'] = 1
# >>> periodi_table['Lead']
# 0
# >>> periodi_table
# defaultdict(<class 'int'>, {'Hydrogen': 1, 'Lead': 0})
# >>> periodi_table = {'Hydrogen': 1, 'Helium': 2}
# >>> print(periodi_table)
# {'Hydrogen': 1, 'Helium': 2}
# >>> carbon = periodi_table.setdefault('carbon', 12)
# >>> carbon
# 12
# >>> periodi_table
# {'carbon': 12, 'Hydrogen': 1, 'Helium': 2}
# >>> helium = periodi_table.setdefault('Helium', 947)
# >>> helium
# 2
# >>> from collections import Counter
# >>> print(Counter(food_counter))
# Counter({'spam': 3, 'eggs': 1})
# >>> print(food_counter.most_common())
# >>> print(Counter(food_counter).most_common())
# [('spam', 3), ('eggs', 1)]
# >>> print(Counter(food_counter).most_common(1))
# [('spam', 3)]
# >>> print(Counter(food_counter).most_common(2))
# [('spam', 3), ('eggs', 1)]
# >>> print(Counter(food_counter).most_common(0))
# []
# >>> print(Counter(food_counter).most_common(1))
# [('spam', 3)]
# >>> breakfast_count = Counter(food_counter)
# >>> breakfast_count
# Counter({'spam': 3, 'eggs': 1})
# >>> lunch  = ['eggs', 'eggs', 'bacon']
# >>> lunch_counter = Counter(lunch)
# >>> lunch_counter
# Counter({'eggs': 2, 'bacon': 1})
# >>> breakfast_count + lunch_counter
# Counter({'spam': 3, 'eggs': 3, 'bacon': 1})
# >>> breakfast_count - lunch_counter
# Counter({'spam': 3})
# >>> lunch_counter - breakfast_count
# Counter({'bacon': 1, 'eggs': 1})
# >>> lunch_counter & breakfast_count
# Counter({'eggs': 1})
# >>> breakfast_count & lunch_counter
# Counter({'eggs': 1})
# >>> breakfast_count | lunch_counter
# Counter({'spam': 3, 'eggs': 2, 'bacon': 1})

from collections import OrderedDict
quotes = OrderedDict([
   ('Moe', 'A wise guy, huh?'),
   ('Larry', 'Ow!'),
   ('Curly', 'Nyuk nyuk!'),
   ])
for stooge in quotes:
   print(stooge)

# 데크는 스택과 큐의 기능을 모두 가진 출입구가 양 끝에 있는 큐다. 데크는 시퀀스의 양 끝으로부터
# 항목으로 추가하거나 삭제할 때 사용한다.
def palinedrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        # popleft함수는 데크로부터 왼쪽 끝의 항목을 제거한 후, 그 항목을 반환한다.
        # pop함수는 오른쪽 끝의 항목을 제거한 후, 그 항목을 반환한다.
        # 양쪽 끝에서부터 이 두 함수가 중간지점을 향해서 동작한다.
        # 양쪽문자가 서로 일치 한다면 단어 중간에 도달할 때까지 데크를 팝한다.
        if dq.popleft() != dq.pop():
             return False
    return True



print(palinedrome('a'))
print(palinedrome('racecar'))
print(palinedrome(''))
print(palinedrome('rader'))
print(palinedrome('halibut'))

# 파이썬은 문자열에 대한 reverse함수가 없지만, 다음과 같이 슬라이스로 문자열을 반전할 수 있다.
def another_palinedrome(word):
    return word == word[::-1]

print(another_palinedrome('radar'))
print(another_palinedrome('halibut'))

# itertools는 특수 목적의 이터레이터 함수를 포함하고 있다.
import itertools
for items in itertools.chain([1,2], ['a', 'b']):
    print(items)

# cycle은 인자를 순환하는 무한 이터레이터다.
# for items in itertools.cycle([1, 2]):
#     print(items)

# accumulate함수는 축적된 값을 계산한다. 기본적으로는 합계
for items in itertools.accumulate([1, 2, 3, 4]):
    print(items)

def multiply(a, b):
    return a * b

for items in itertools.accumulate([1, 2, 3, 4], multiply):
    print(items)

from pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Lary,', 'Ow'),
    ('Curly', 'Nyuk nyuk!')
])

print(quotes)
# pprint 함수는 가독성을 위해 요소들을 정렬하여 출력한다.
pprint(quotes)
