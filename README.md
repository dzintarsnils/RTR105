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
