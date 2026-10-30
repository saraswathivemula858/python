Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #sets()
>>> a={3,6.7,"python",7+9j,True,False}
>>> print(a)
{False, True, (7+9j), 3, 6.7, 'python'}
>>> type(a)
<class 'set'>
>>> b={5,7,9,10,12,14,15}
>>> print(b)
{5, 7, 9, 10, 12, 14, 15}
>>> #add9
>>> #add()
>>> a={4,5,6,7,8,9}
>>> a.add(10)
>>> a
{4, 5, 6, 7, 8, 9, 10}
>>> #issubset()
>>> a={1,2,3,4,5,6}
>>> b={4,5,6}
>>> b.issubset(a)
True
>>> a.issubset(b)
False
>>> #superset()
>>> a={2,3,4,5,6,7,8,9}
>>> b={6,7,8,9}
>>> a.issubset(b)
False
>>> b.issubset(a)
True
>>> a.issuperset(a)
True
>>> b.issuperset(b)
True
>>> #union()
>>> a={5,6,7,8,9,10}
>>> b={6,7,8,9,10,11,12}
>>> a.union(b)
{5, 6, 7, 8, 9, 10, 11, 12}
>>> b.union(a)
{5, 6, 7, 8, 9, 10, 11, 12}
#intersection()
a={4,5,6,7,8,9}
b={7,8,9,10,11,12}
a.intersection(b)
{8, 9, 7}
#update()
a={4,5,6,7,8,9}
b={7,8,9,10,11,12}
a.update(b)
a
{4, 5, 6, 7, 8, 9, 10, 11, 12}
b
{7, 8, 9, 10, 11, 12}
b.update(a)
b
{4, 5, 6, 7, 8, 9, 10, 11, 12}
#difference()
a={3,4,5,6,7,8}
b={8,9,10,11,12}
a.difference(b)
{3, 4, 5, 6, 7}
b.difference(a)
{9, 10, 11, 12}
#symetric_difference()
a={10,11,12,13,14,15}
b={13,14,15,16,17,18}
a.symetric_difference(b)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.symetric_difference(b)
AttributeError: 'set' object has no attribute 'symetric_difference'. Did you mean: 'symmetric_difference'?
#intersection_update()
a={8,9,10,11,12}
b={11,12,13,14,15}
a.intersection_update(b)
a
{11, 12}
a
{11, 12}
b.intersection_update(a)
b
{11, 12}
b
{11, 12}
#difference_update()
a={10,20,30,40,50}
b={30,40,50,60,70}
a.difference_update(b)
a
{20, 10}
b.difference_update(a)
b
{50, 70, 40, 60, 30}
#symmetric_difference()
a={10,11,12,13,14,15}
b={13,14,15,16,17,18}
a.symmetric_difference(b)
{10, 11, 12, 16, 17, 18}
b.symmetric_difference(a)
{10, 11, 12, 16, 17, 18}
#symmetric_difference_update()
a={3,4,5,6,7,8,9}
b={1,2,3,4,5,6}
a.symmetric_difference_update(b)
a
{1, 2, 7, 8, 9}
a
{1, 2, 7, 8, 9}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8, 9}
#pop()
a={7,8,9,10,11,12}
a.pop()
7
a.pop(3)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.pop(3)
TypeError: set.pop() takes no arguments (1 given)
a
{8, 9, 10, 11, 12}
#remove()
a.remove(10)
a
{8, 9, 11, 12}
a.discard(11)
a
{8, 9, 12}
#copy()
a={10,20,30,40,50}
a.copy()
{50, 20, 40, 10, 30}
b=a.copy()
b
{50, 20, 40, 10, 30}
#clear()
a.clear()
a
set()
b=set()
b.add
<built-in method add of set object at 0x00000222B1599D20>
b.add(30)
b
{30}
#index()
a=
SyntaxError: invalid syntax
a={5,6,7,8,9,10}
a.index(5)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a.index(5)
AttributeError: 'set' object has no attribute 'index'
#length()
len(a)
6
a.count(10)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.count(10)
AttributeError: 'set' object has no attribute 'count'
#isdisjoint()
a={4,5,6,7,8}
b={9,10,11,12}
a.isdisjoint(b)
True
a={3,4,5,6,7}
b={7,8,9,10}
a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
False
