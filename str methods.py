Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string methods
>>> #upper()
>>> a="code"
>>> a.upper()
'CODE'
>>> b="python"
>>> b.upper()
'PYTHON'
>>> #lower()
>>> c="HELLO"
>>> c.lower()
'hello'
>>> a=="python"
False
>>> a="python"
>>> a.upper()
'PYTHON'
>>> a[0].upper()
'P'
>>> #capitalize()
>>> a.capitalize()
'Python'
>>> b="python course"
>>> b.title()
'Python Course'
>>> c="i am in class"
>>> c.title()
'I Am In Class'
>>> c. capitalize()
'I am in class'
>>> a="hello"
>>> a.isupper()
False
>>> a.islower()
True
>>> a.isalpha()
True
>>> b="hello world"
>>> b.isalpha()
False
c="helloworld"
c.isalpha()
True
a.isdigit()
False
b=12345
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
c="12345"
c.isdigit()
True
a="python"
a="python"
a="python course"
a.startswith("p")
True
a.endswith("e")
True
b="python COURSE"
b.isupper()
False
c="saraswathi123"
c.isalnum()
True
#strip
#rstrip()a="  saraswathi  "
a.strip()
'python course'
a="  saraswathi  "
a.strip()
'saraswathi'
a.lstrip()
'saraswathi  '
a.rstrip()
'  saraswathi'
#split
a="python java c++
SyntaxError: unterminated string literal (detected at line 1)
a."python java c++"
SyntaxError: invalid syntax
a="python java c++"
a.split()
['python', 'java', 'c++']
b="i am learning"
b().split
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    b().split
TypeError: 'str' object is not callable
b.split()
['i', 'am', 'learning']
c=b.split()

c
['i', 'am', 'learning']
c[1].upper()
'AM'
#join()
a="apple","banana","grapes"
"".join(a)
'applebananagrapes'
" ".join(a)
'apple banana grapes'
"k".join(a)
'applekbananakgrapes'
b="hello"
"k".join(b)
'hkeklklko'
#concatination()
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
fname="saraswathi"
lname="devi"
print(fname+lname)
saraswathidevi
print(fname+" "+lname)
saraswathi devi
print(fname.title()+" "+lname.title())
Saraswathi Devi
print((fname+" "+lname).title())
Saraswathi Devi
#formatting
a=5
b=7
print(a+b)
12
print("the sum is",a+b)
the sum is 12
print("the sum is a+b")
the sum is a+b
city="vij"
print("city is",city)
city is vij
a="motu"
b="pathlu
SyntaxError: unterminated string literal (detected at line 1)
a="motu"
b="pathulu"
#format()
print("hello {}{}".format(a,b))
hello motupathulu
print9"hello {} {}".format(a,b))
SyntaxError: unmatched ')'
print9"hello {} {}".format(a,b))
SyntaxError: unmatched ')'
#fstring
a="sweety"
b="cuty"
print(f"hello {a}{b}")
hello sweetycuty
print(f"hello {a} {b})
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(f"hello {a} {b}")
      
hello sweety cuty
print(f"hello {a} hello {b}")
      
hello sweety hello cuty
