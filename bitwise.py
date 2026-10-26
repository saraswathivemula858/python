Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#membership
a=2,3,4,5,6,7,8,9
9 in a
True
10 in a
False
10 not in a
True
#bitwise operators
a=3
b=7
a|b
7
>>> a=4
>>> b=8
>>> a|b
12
>>> a=3
>>> b=8
>>> a|b
11
>>> a=5
>>> ~a
-6
>>> b=-4
>>> ~b
3
>>> -(b+1)
3
>>> _(a+1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    _(a+1)
TypeError: 'int' object is not callable
>>> -(a+1)
-6
>>> a=4
>>> b=9
>>> a^b
13
>>> a=5
>>> b=10
>>> a^b
15
>>> a=6
>>> a<<2
24
>>> a=2
>>> a>>3
0
>>> a=8
>>> a>>2
2
