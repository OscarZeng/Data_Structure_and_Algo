class  WuZhangmeng(object):
    """docstring for  WuZhangmeng"""
    def __init__(self, uni, gender):
        theUni = uni
        theGender = gender
    def dance(self, style):
        print("I am dancing "+style +"gracefully! Yeah~~~")
    def eat(self, food):
        print("I am eating ", food)


def  test(s):
    print("Hello World! ",s)
    b = [1,2,3,4,"Wu Zhangmeng"]
    for  i in b:
        if type(i) == int:
            print(i)
    # for i in range(10, -1, -1):
    #     print(i)

def myMax(a,b):
    if a==b:
        print("Same iaoshduahalue")
        return a
    if a > b:
        print(a)
        return a
    else:
        print(b)
        return b

# a = 100
# b = 12
# ans = myMax(a, b)
# print("The ans is:", ans)

# s = "Zhangmeng"
# test(s)
uni = "HKU"
gender ="F"
food = "喜茶"
style = "Hiphop"
a = WuZhangmeng(uni, gender)
a.dance(style)
a.eat(food)