class MyList(object):
    def list(selfs):
        num = []
        for x in range(1,10):
            num.append(x);
        print(num)
        # 删除最后一个元素
        num.pop()
        print(num)
        # 删除最后一个元素
        del num[-1]
        print(num)
        for x in num:
            print(num[x-1])
class MySet(object):
    def set(self):
        num = {}
        num.add(1)
        num.add(12)
        num.add(13)
        for x in range(1,11):
            num.add(x)
        print(num)
        # 移出指定的数字
        num.remove(12)
        print(num);
class MyMap(object):
    def map(self):
        num ={}
        for x in range(1,11):
            num[str(x)+"test"] = x+10
        print(num)
        # 移出不存在的key会报错 del num['1test']
        if num.__contains__('1test'):
            del num['1test']
        print(num);









