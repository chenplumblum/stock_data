# []:数组
# ():元组：长度和里面的值是不可变的
# {}:字典
# set():集合

# 循环：相互转换
# 字典(dict)
dict 用 {} 包围 
dict.keys(),dict.values(),dict.items() 
hash(obj)返回obj的哈希值，如果返回表示可以作为dict的key 
del 或 dict.pop可以删除一个item,clear清除所有的内容 
sorted(dict)可以吧dict排序 
dict.get()可以查找没存在的key，dict.[]不可以 
dict.setdefault() 检查字典中是否含有某键。 如果字典中这个键存在，你可以取到它的值。 如果所找的键在字典中不存在，你可以给这个键赋默认值并返回此值。 
{}.fromkeys()创建一个dict，例如: {}.fromkeys(('love', 'honor'), True) =>{'love': True, 'honor': True} 
不允许一个键对应多个值 
键值必须是哈希的，用hash()测试 
一个对象，如果实现_hash()_方法可以作为键值使用



# 集合(set)
集合是一个数学概念，用set()创建 
set.add(),set.update.set.remove，添加更新删除，-= 可以做set减法 
set.discard 和 set.remove不同在于如果删除的元素不在集合内，discard不报错，remove 报错 
< <= 表示 子集，> >=表示超集 
| 表示联合 & 表示交集 - 表示差集 ^ 差分集里啊


# 列表(list)
列表是序列对象，可包含任意的Python数据信息，如字符串、数字、列表、元组等。列表的数据是可变的，我们可通过对象方法对列表中的数据进行增加、修改、删除等操作。可以通过list(seq)函数把一个序列类型转换成一个列表。
append(x) 在列表尾部追加单个对象x。使用多个参数会引起异常。 
count(x) 返回对象x在列表中出现的次数。 
extend(L) 将列表L中的表项添加到列表中。返回None。 
Index(x) 返回列表中匹配对象x的第一个列表项的索引。无匹配元素时产生异常。 
insert(i,x) 在索引为i的元素前插入对象x。如list.insert(0,x)在第一项前插入对象。返回None。 
pop(x) 删除列表中索引为x的表项，并返回该表项的值。若未指定索引，pop返回列表最后一项。 
remove(x) 删除列表中匹配对象x的第一个元素。匹配元素时产生异常。返回None。 
reverse() 颠倒列表元素的顺序。 
sort() 对列表排序，返回none。bisect模块可用于排序列表项的添加和删除。 


# 元组(tuple)
tuple=(1,)，这是单个元素的元组表示，需加额外的逗号。
tuple=1，2，3，4，这也可以是一个元组，在不使用圆括号而不会导致混淆时，Python允许不使用圆括号的元组。
和列表一样，可对元组进行索引、分片、连接和重复。也可用len()求元组长度。  
元组的索引用tuple[i]的形式，而不是tuple(i)。 
和列表类似，使用tuple(seq)可把其它序列类型转换成元组。

------------------------------------------------------ 分割线 --------------------------------------------------------------------

相互之间的转换：

set 和list之间可以通过set(seq)和list(seq)两个函数之间快速转换，这两者转换最大的用处是去掉list中重复的元素值，方便做一些其它操作

list(seq)可以把所有的序列和可迭代的对象转换成一个list,元素不变，排序也不变。

tuple(seq)可以把所有可迭代的(iterable)序列转换成一个tuple, 元素不变，排序也不变


tuple("hello world")
('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')

zip函数和强大的集合操作可以方便的将两个list元素一一对应转换为dict


names = ['n1','n2','n3']
values = [1,2,3]
nvs = zip(names,values)
nvDict = dict( (name,value) for name,value in nvs)





python中Set和List的性能差距能有数百倍 

如果有需要求（集合，列表等）的并集和交集的时候，最好使用Set。

----------------------------------------------------

set转成list方法如下：                                                     list转成set方法如下：
s = set('12342212')                                                       l = ['12342212']
print s    # set(['1', '3', '2', '4'])                                       s = set(l[0])
l = list(s)                                                                         print s    # set(['1', '3', '2', '4'])
l.sort()    # 排序                                                             m = ['11','22','33','44','11','22']
print l    # ['1', '2', '3', '4']                                               print set(m)    # set(['11', '33', '44', '22'])

可见set和lsit可以自由转换，在删除list中多个/海量重复元素时，可以先转换成set，然后再转回list并排序(set没有排序)。此种方法不仅方便且效率较高。



## 1、字典（dict）

dict = {‘name’: ‘Zara’, ‘age’: 7, ‘class’: ‘First’}
1.1 字典——字符串
返回：
print type(str(dict)), str(dict)
1.2 字典——元组
返回：(‘age’, ‘name’, ‘class’)
print tuple(dict)
1.3 字典——元组
返回：(7, ‘Zara’, ‘First’)
print tuple(dict.values())
1.4 字典——列表
返回：[‘age’, ‘name’, ‘class’]
print list(dict)
1.5 字典——列表
print dict.values
## 2、元组
tup=(1, 2, 3, 4, 5)
2.1 元组——字符串
返回：(1, 2, 3, 4, 5)
print tup.__str__()
2.2 元组——列表
返回：[1, 2, 3, 4, 5]
print list(tup)
2.3 元组不可以转为字典
## 3、列表
nums=[1, 3, 5, 7, 8, 13, 20];
3.1 列表——字符串
返回：[1, 3, 5, 7, 8, 13, 20]
print str(nums)
3.2 列表——元组
返回：(1, 3, 5, 7, 8, 13, 20)
print tuple(nums)
3.3 列表不可以转为字典

## 4、字符串
4.1 字符串——元组
返回：(1, 2, 3)
print tuple(eval("(1,2,3)"))
4.2 字符串——列表
返回：[1, 2, 3]
print list(eval("(1,2,3)"))
4.3 字符串——字典
返回：
print type(eval("{'name':'ljq', 'age':24}"))
