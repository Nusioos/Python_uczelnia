x = 2;y = 3;
if x > y:
    result = x;
else:
    result = y;
#dziala poniewaz w pythonei sredniki nie sa zakazane nawiasy sa dozwolone sredniki pomimo zbednosci nie sa bledem
######  for i in "axby": if ord(i) < 100: print(i) 
# nie zadziala bo nie mozan dac ifa w naglowku petli for poprawna wersja:
for i in "axby":
    if ord(i) < 100:
        print(i)
#to zadziala

for i in "axby": print(ord(i) if ord(i) < 100 else i)
#python pozwala na tak zwazne isntrukcje proste w tym samymm wierszu np print a ze if znajduje sie w tym princie to python nie wdizi problemu