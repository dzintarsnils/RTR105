Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> str = "Hello"
>>> str1 = "Hello"
>>> str2 = "there"
>>> bob = str1 + str2
>>> print(bob)
Hellothere
>>> str3 = "123"
>>> str3 = str3 + 1
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    str3 = str3 + 1
TypeError: must be str, not int
>>> x = int(str3) + 1
>>> print(x)
124
>>> name = input('Enter:')
Enter:Nils
>>> print(name)
Nils
>>> apple = input('Enter:')
Enter:100
>>> x = apple - 10
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x = apple - 10
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> x = int(apple) - 10
>>> print(x)
90
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> x = 3
>>> w = fruit[x - 1]
>>> print(w)
n
>>> fruit = 'banana'
>>> print(len(fruit))
6
>>> fruit = 'banana'
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(index, letter)
	index = index + 1

	
0 b
1 a
2 n
3 a
4 n
5 a
>>> fruit = 'abols'
>>> for letter in fruit:
	print(letter)

	
a
b
o
l
s
>>> anus = 'janis'
>>> for letter in anus:
	print(letter)

	
j
a
n
i
s
>>> fruit = 'banana'
>>> for letter in fruit:
	print(letter)

	
b
a
n
a
n
a
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
b
a
n
a
n
a
>>> 
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count + 1
		print(count)

		
1
2
3
>>> for letter in 'banana':
	print(letter)

	
b
a
n
a
n
a
>>> s = 'Monty Python'
>>> print(s[0:4])
Mont
>>> print(s[6:7])
P
>>> print(s[6:20])
Python
>>> s = 'Monty Python'
>>> print(s[:2])
Mo
>>> print(s[8:])
thon
>>> print(s[:])
Monty Python
>>> a = 'hello'
>>> b = a + 'there'
>>> print(b)
hellothere
>>> c = a + ' ' + 'there'
>>> print(c)
hello there
>>> fruit = 'banana'
>>> 'n' in fruit
True
>>> 'm' in fruit
False
>>> 'nan' in fruit
True
>>> if 'a' in fruit:
	print('found it')

	
found it
>>> if word == 'banana':
	print('all right, bananas')

	
all right, bananas
>>> if word < 'banana':
	print('your word,' + word + ',comes before bananas')
    elif word > 'banana':
	    
SyntaxError: unindent does not match any outer indentation level
>>> 
