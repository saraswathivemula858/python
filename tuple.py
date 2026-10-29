Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a=(6,8.9,"python",2+9j,True,False)
>>> print(a)
(6, 8.9, 'python', (2+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.index(2+9j)
3
>>> a.count(True)
1
>>> len(a)
6
