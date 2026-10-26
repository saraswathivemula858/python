Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a='i am good girl'
a[2]+a[3]
'am'
a[10]+a[11]+a[12]+a[13]
'girl'
a[5]+a[6]+a[7]+a[8]
'good'
a[0]
'i'
a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]+a[13]
' am good girl'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]+a[13]
'i am good girl'
b='i go to institute everyday'
a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'ood girl'
b[-8]+b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'everyday'
b[-18]+b[-17]+b[-16]+b[-15]+b[-14]+b-[13]+b[-12]+b[-11]+b[-10]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    b[-18]+b[-17]+b[-16]+b[-15]+b[-14]+b-[13]+b[-12]+b[-11]+b[-10]
TypeError: unsupported operand type(s) for -: 'str' and 'list'
a[-26]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[-26]
IndexError: string index out of range
b[-26]
'i'
>>> b[-24]+b[-23]
'go'
>>> b[-21]+b[-20]
'to'
>>> #slicing
>>> a='i am eating idly everyday'
>>> a[11:16]
' idly'
>>> a[16:24]
' everyda'
>>> a[4:11]
' eating'
>>> a[1:4]
' am'
>>> a[0:1]
'i'
>>> b='i like eating apple'
>>> b[-19:17]
'i like eating app'
>>> b[-19:-17]
'i '
>>> a[-18:-13]
'ting '
>>> a[-13:-6]
'idly ev'
>>> a[-6:-1]
'eryda'
>>> a[-17:-14]
'ing'
>>> #striding
>>> a='python full stack'
>>> a=[3:11:2]
SyntaxError: invalid syntax
>>> a[4:9:2]
'o u'
>>> a=[1:10:2]
SyntaxError: invalid syntax
>>> a=[1:10:2]
SyntaxError: invalid syntax
>>> a=[-10:-1:-2]
SyntaxError: invalid syntax
