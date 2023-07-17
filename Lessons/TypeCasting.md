Defn
----
    Typecasting generally meens to conversion of one type of data to anther type of
    data 
    Typecasting also known as the typecoresion

* Python has the inbuilt functions like
    int()
    float()
    bool()
    str()



int
--------------
int(10)4
SyntaxError: invalid syntax

int(0o99)
SyntaxError: invalid digit '9' in octal literal

int(0o88)
SyntaxError: invalid digit '8' in octal literal

int(0o34)
28

int(0xabc)
2748

int(0B1111)
15

int(10)
10

int(True)
1

int(False)
0

int("10")
10

int("10.4")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    int("10.4")
ValueError: invalid literal for int() with base 10: '10.4'

int(10.3)
10

int("Ten")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int("Ten")
ValueError: invalid literal for int() with base 10: 'Ten'

int(None)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    int(None)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'

int(10+6j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int(10+6j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

* Note
------
    ->We can convert any data type to the int type except Complex and the None data type
    ->We can convert string to the int when it is in the base 10 value
        like 1,2,3 but 10.3,40.3 cannot be converted