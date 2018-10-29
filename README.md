# RTR105
Datormācības kursa elektroniskā klade

python
ipython
idle

cd -- change directory
. -- current directory
ls -l -- parlukot visas mapes
pwd -- ta vieta, kur atrodies
sudo -- (SuperUser DO) dod administratora privilegijas
mv -- lauj parvietot failus
mkdir -- lauj izveidot jaunu direktoriju
rm -- izdzes specifisku failu
history -- parada komandu vesturi
echo -- attelo tekstu


PYTHON
vars() -- izprinte funkciju iespejas
__doc__ -- dokumente funkciju
print (..) -- izprinte tekstu
type (..) -- izprinte datu tipu
float -- peldosais tips (dalskaitli)
string -- simboli (teksts)
int -- veseli skaitli


UZDEVUMS
# This first line is provided for you

hrs = (float(input("Enter Hours:")))
rate = (float(input("Rate per hour")))
grosspay = hrs*rate
print("Pay:",grosspay)


Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properl

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate per hour:")
r = float(rate)
if h > 40 :
    print(40 * r + (h - 40) * r * 1.5)
if h < 40 :
    print(h * r)



funkcijas izveidošana izmantojot def, pēc kura ievada kādu parametru
def print_lyrics():
to var izmantot, cik grib
agruments big=max('hello world') - iekavās ir arguments

parametrs (lang)
def greet(lang):
if lang == 'es':
 print('hola')
elif lang == 'fr':
 print('bonjour')
else:
 print('labdien')

+ - atstarpe

IF vienmēr satur nosacījumu un : simbolu beigās

ELIF vienmēr pieder kādam IF
ELIF vienmēr satur nosacījumu un : simbolu beigās
ELIF var nebūt/var būt viens/ var būt vairāki

ELSE vienmēr pieder kādam IF
ELSE nesatur nosacījumus un satur : simbolu beigās
ELSE var nebūt/ var būt viens un vienmēr ir beigās

WHILE+saliktais nosacījums:
++++ vismaz viena darbība
++++ CONTINUE (pārtrauc cikla soli,atgriežamies pie nosacījuma)
++++ BREAK (pārtraucam cikla turpinājumu, atgriežamies pie nosacījuma)
FOR (cikla mainīgais ir saraksts):
++++ vismaz viena darbība
++++ CONTINUE (aizies pie cikla nākamās elementa)
