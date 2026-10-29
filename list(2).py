Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=["apple","mango","kiwi"]
a.index("mango")
1
a.copy()
['apple', 'mango', 'kiwi']
b=a.copy()
b
['apple', 'mango', 'kiwi']
a=["vja","vza","hyd"]
a.pop(1)
'vza'
a
['vja', 'hyd']
a.pop("vja")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.pop("vja")
TypeError: 'str' object cannot be interpreted as an integer
a
['vja', 'hyd']
a.pop(0)
'vja'
#remove()
a=["hi","hello","how"]
a.remove("how")
a
['hi', 'hello']
a.remove(1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
a=['java","ai","ml"]
   
SyntaxError: unterminated string literal (detected at line 1)
a=["java","ai","ml"]
   
a.clear()
   
a
   
[]
b=[]
   
b.append("saraswathi")
   
b
   
['saraswathi']
a=['banana","grapes","apple","mango","kiwi"]
   
SyntaxError: unterminated string literal (detected at line 1)
a=["banana","grapes","apple","mango","kiwi"]
   
a.sort()
   
a
   
['apple', 'banana', 'grapes', 'kiwi', 'mango']
b=[7,0,2,5,10,8,1]
   
b.sort()
   
b
   
[0, 1, 2, 5, 7, 8, 10]
c=[5+9j,2+4,6+9]
   
c.sort
   
<built-in method sort of list object at 0x0000016479EAFAC0>
c=[4.5,8.9,2.3]
   
c.sort()
   
c
   
[2.3, 4.5, 8.9]
d=[True,False,True]
   
d.sort()
   
d
   
[False, True, True]
k=[2.3.4,21.4]
   
SyntaxError: invalid syntax. Perhaps you forgot a comma?
k.sort()
   
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    k.sort()
NameError: name 'k' is not defined
>>> a=["black","red","white"]
...    
>>> a.reverse()
...    
>>> a
...    
['white', 'red', 'black']
>>> b=[5,8,0,1,6,9]
...    
>>> b.reverse()
...    
>>> b
...    
[9, 6, 1, 0, 8, 5]
>>> a=["java","ai","ml"]
...    
>>> len(a)
...    
3
>>> b="java"
...    
>>> len(b)
...    
4
>>> c=["java"]
...    
>>> len(c)
...    
1
>>> a.count("ai")
...    
1
>>> a.count("a")
...    
0
>>> b=["java","ai","a","ml"]
...    
>>> b.count("a")
...    
1
