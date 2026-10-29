Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,4.5,"python",8+9j,True,False]
print(a)
[2, 4.5, 'python', (8+9j), True, False]
type(a)
<class 'list'>
b=4.6
4
4
type(b)
<class 'float'>
>>> c=[4.6]
>>> type(c)
<class 'list'>
>>> a=["python","java","c++","c"]
>>> a.append("ai")
>>> a
['python', 'java', 'c++', 'c', 'ai']
>>> a.append("ml","dsa")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ml","dsa")
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(["ml","dsa"])
>>> a
['python', 'java', 'c++', 'c', 'ai', ['ml', 'dsa']]
>>> #extend()
>>> a=["dsa","ai","ml"]
>>> a.extend(["python","java"])
>>> a
['dsa', 'ai', 'ml', 'python', 'java']
>>> #insert()
>>> b=['black","white"]
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> b=["black","white"]
...    
>>> b.insert(1,"red")
...    
>>> b
...    
['black', 'red', 'white']
>>> a=["apple","mango","kiwi"]
...    
>>> a=["apple","mango","kiwi"]
...    
>>> a.index("mang")
...    
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.index("mang")
ValueError: list.index(x): x not in list
