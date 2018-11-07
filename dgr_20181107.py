Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> stuff = "hello\nworld"
>>> stuff
'hello\nworld'
>>> print(stuff)
hello
world
>>> stuff = "x\ny"
>>> print(stuff)
x
y
>>> #\n (newline) parada, kur beidzas line
>>> 
>>> len(stuff)
3
>>> xfile = open('mbox.txt')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    xfile = open('mbox.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox.txt'
>>> xfile = open('teksts.txt')
>>> for cheese in xfile
SyntaxError: invalid syntax
>>> 
>>> for cheese in xfile:
	print(cheese)

	
rtu

rigas tehniska utilizacija

>>> fhand = open('teksts.txt')
>>> count = 0
>>> for line in fhand:
	count = count + 1
    print('line count:', count)
    
SyntaxError: unindent does not match any outer indentation level
>>> count = 0
>>> for line in fhand:
	count = count + 1
	print('line count:', count)

	
line count: 1
line count: 2
>>> $ python open.py
SyntaxError: invalid syntax
>>> # ar count saskaita dotaja faila rindinu skaitu
>>> 
>>> inp = fhand.read()
>>> print(len(inp))
0
>>> fhand = open('teksts.txt')
>>> inp = fhand.read()
>>> print(len(inp))
31
>>> print(inp[:20])
rtu
rigas tehniska u
>>> #we can read the whole file (newlines and all) into a single string
>>> 
>>> fhand = open('teksts.txt')
>>> for line in fhand:
	if line.startswith('rigas'):
		print(line)

		
rigas tehniska utilizacija

>>> #ar for un if var atrast specifisku rindinu, dodot vienu vardu
>>> 
>>> fhand = open('teksts.txt')
>>> for line in fhand:
	line = line.rstrip()
	if line.startswith('rigas'):
		print(line)

		
rigas tehniska utilizacija
>>> fhand = open('teksts.txt')
>>> for line in fhand:
	line = line.rstrip()
	if not 'rtu' in line:
		continue
	print(line)

	
rtu
>>> #sadi var atrast sevis vajadzigo vardu jebkur teksta
>>> 
>>> fname = input('ievadiet faila nosaukumu: ')
ievadiet faila nosaukumu: 
>>> fhand = open(fname)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    fhand = open(fname)
FileNotFoundError: [Errno 2] No such file or directory: ''
>>> fname = input('ievadiet faila nosaukumu: ')
ievadiet faila nosaukumu: teksts.txt
>>> fhand = open(fname)
>>> count = 0
>>> for line in fhand:
	if line.startswith('subject:'):
		count = count + 1

		
>>> print ('there were', count, 'subject lines in', fname)
there were 0 subject lines in teksts.txt
>>> fname = input('enter the file name: ')
enter the file name: teksts.txt
>>> try
SyntaxError: invalid syntax
>>> try:
	fhand = open(fname)
	except:
		
SyntaxError: invalid syntax
>>> except:
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> fname = input('enter the file name: ')
enter the file name: teksts.txt
>>> try:
	fhand = open(fname)


    except:
	    
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> except:
	
SyntaxError: invalid syntax
>>> 
