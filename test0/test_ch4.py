from time import localtime, strftime, sleep

def start_end(func):
    def testFunc(*args, **kwargs):
        nowTime = strftime("%Y/%m/%d-%A %H.%M.%S", localtime())
        print("\n" + func.__name__ + " start " + nowTime)
        func(*args, **kwargs)
        nowTime = strftime("%Y/%m/%d-%A %H.%M.%S", localtime())
        print(func.__name__ + " end " + nowTime)
    return testFunc


@start_end
def guess():
    guess_me = 7
    if guess_me < 7:
        print("too low")
    elif guess_me > 7:
        print("too high")
    else:
        print("just right")

guess()

@start_end
def guessStart():
    guess_me = 7
    start = 1
    while start < 10:
        if guess_me == start:
            print("found it!")
            break
        elif guess_me > start:
            print("too low")
        elif guess_me < start:
            print("oops")
        start += 1

guessStart()

@start_end
def forLoopExam():
    list0 = []
    for i in range(4, -1, -1):
        list0.append(i)
    print(list0)
forLoopExam()

@start_end
def rangeListLoop():
    list1 = [num for num in range(10) if num % 2 == 0]
    print(list1)

rangeListLoop()

@start_end
def squaresDic():
    squares = {num: num * num for num in range(10)}
    print(squares)

squaresDic()

@start_end
def generaComp():
    for i in range(10):
        print(("Got", i))
generaComp()

def good():
    goodList = ['Hanrray', 'Ron', 'Hermione']
    return goodList

print("")
print(good())

def get_odds():
    list0 = [i for i in range(10) if i % 2 == 1]
    return list0

@start_end
def threeReturn():
    list1 = []
    for j in get_odds():
        list1.append(j)
    print(list1[2])

threeReturn()

class oopsExcepton(Exception):
    pass

@start_end
def generaComp1():
    try:
        for i in range(10):
            print(("Got", i))
            if i > 5:
                raise oopsExcepton("Caught an oops")
    except oopsExcepton as str:
        print(str)
generaComp1()

print("")

title = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon stre', 'A haunted yarn shop']

zipToList = dict(zip(title, plots))
print(zipToList)
