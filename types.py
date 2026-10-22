Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int()
int(9)
9
int(7.8)
7
int("hi")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(6+8j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(6+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> int(True)
1
>>> int(False)
0
>>> #float
>>> float(8.1)
8.1
>>> float(7.1)
7.1
>>> float(3)
3.0
>>> float("3.2")
3.2
>>> #string
>>> str('saraswathi')
'saraswathi'
>>> str("saraswathi")
'saraswathi'
>>> str('''saraswathi''')
'saraswathi'
>>> str(saraswathi)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    str(saraswathi)
NameError: name 'saraswathi' is not defined
>>> #complex
>>> complex(5+3j)
(5+3j)
>>> complex(3j+4)
(4+3j)
>>> #boolean
>>> bool(True)
True
>>> bool(False)
False
