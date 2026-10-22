Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatypes
>>> a=10
>>> type(a)
<class 'int'>
>>> b=5.6
>>> type(b)
<class 'float'>
>>> c='python'
>>> type(c)
<class 'str'>
>>> d="codenan"
>>> type(d)
<class 'str'>
>>> e='''course'''
>>> type(e)
<class 'str'>
>>> f=4+9j
>>> type(f)
<class 'complex'>
>>> g=21+9j
>>> type(g)
<class 'complex'>
>>> x=2j
>>> type(x)
<class 'complex'>
>>> y=4j+7
>>> type(y)
<class 'complex'>
>>> a=2+8i
SyntaxError: invalid decimal literal
>>> b=j
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    b=j
NameError: name 'j' is not defined
>>> c=True
>>> type(c)
<class 'bool'>
>>> d=False
>>> type(d)
<class 'bool'>
