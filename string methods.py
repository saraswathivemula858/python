Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string methods
>>> #len()
>>> a="python"
>>> len(a)
6
>>> b="python course"
>>> len(b)
13
>>> c=""
>>> len(c)
0
>>> d=" "
>>> len(d)
1
>>> #count()
>>> a="twinkle twinkle litter star"
>>> count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count("twinkle")
2
>>> a.count("t")
5
>>> a.count("a")
1
>>> a.count(" ")
3
>>> a.count("i")
3
>>> a.count("little")
0
>>> a="1234"
>>> a.count("3")
1
>>> a=1,2,3,4,5,6
>>> a.count(3)
1
>>> b=3,4,5,6,3,6,7
a.count(3)
1
b.count(3)
2
#find a string
a="code"
a[2]
'd'
a.find("d")
2
b="hello"
b.find("l")
2
b[2:4]
'll'
b.find("k")
-1
#escape sequences
#\n->new line
#\n->tab space
a="name\nmobileno\tmailid\ncollage\tbranch"
print(a)
name
mobileno	mailid
collage	branch
a="name:saraswathi\nmobileno:9505134858\tmailid:saraswathivemula80@gmail.com\ncollage:vitw\tbranch:cse
SyntaxError: unterminated string literal (detected at line 1)
a="name:saraswathi\nmoboleno:9505134858\tmailid:saraswathi@gmail.com\ncollage:vitw\tbranch:cse"
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a="python java"
a. replace("java","DSA")
'python DSA'
a="hi"
a.replace("h","a")
'ai'
