# Arts Inarts Kubilis

#dalītāji var būt pozitīvi un negatīvi, kaut gan bieži dalītāja jēdziens tiek attiecināts tikai uz pozitīviem skaitļiem (https://lv.wikipedia.org/wiki/Dal%C4%ABt%C4%81js)
from tabulate import tabulate  # pip install tabulate

class Rekinatajs:

    def __init__(self):
        pass

    def Factorial(self, sk):
        if isinstance(sk,int)==False or sk<0:
            print('Faktorialim ir nepieciesams naturals skaitlis vai 0!')

        else:
            i = sk
            atb = 1
            while i != 0:
                atb = atb * i
                i = i - 1

            print(f'{sk}! = {atb}')

    def Sum(self, sk, *check):
        if isinstance(sk,int)==False or sk<=0:
            print('Summai lidz skaitlim ir nepieciesams naturals skaitlis!') #ja nebus naturals skaitlis, tad nestradas sakariba: summa lidz 3 ir 1+2+3, un bus -∞ + -∞+1 + ... lidz dotajam

        else:
            i = sk
            atb = 0
            if sk>=0:
                while i != 0:
                    atb = atb + i
                    i = i - 1

            print(f'Skaitlu summa lidz skaitlim {sk} ir {atb}')

    def testPrime(self, sk, *check):
        if isinstance(sk,int)==False or sk<=0:
            print('Pirmskaitli ir naturali skaitli!')

        else:
            global psk
            psk=''
            ski = [2, 3, 4, 5, 6, 7, 8, 9]
            skatb=[]
            i = 0
            atb = 1
            while i != 8:
                if sk != ski[i]:
                    if sk == 1:
                        atb = 0

                    else:
                        atb = sk % ski[i]

                skatb.append(atb)

                i = i + 1

            if 0 in skatb:
                if 'noklusejums' not in check:
                    print(f'Skaitlis {sk} nav pirmskaitlis')

            else:
                psk=sk

                if 'noklusejums' not in check:
                    print(f'Skaitlis {sk} ir pirmskaitlis')

    def TableMult(self, sk):
        if isinstance(sk, int) == False or sk<=0:
            print('Reizrekina tabulas izveidei nepieciesams naturals skaitlis!') #jo ja nav naturals tad ir -∞ lidz dotajam

        else:
            skpoz=+abs(sk)
            top0 = ['']
            top1 = []
            top2 = []
            i = 1
            while i <= skpoz:
                isk=i

                top0.append(isk)

                i = i + 1

            i = 1
            while i <= skpoz:
                top1 = []
                isk=i

                top1.append(isk)

                l = 1
                while l <= skpoz:
                    darb = +abs(top0[i]) * l

                    top1.append(darb)

                    l = l + 1

                top2.append(top1)
                i = i + 1
            table = top2

            print(f'Reizrekina tabula no 1 lidz skailim {sk}: ')
            print('')
            print(tabulate(table, headers=top0, tablefmt="presto"))
            print('')

    def listDiv(self, sk, *check):
        if isinstance(sk, int) == False or sk==0:
            print('Dalitaju atrasanai ir nepieciesams vesels skaitlis kas nav 0!')

        else:
            ski = []
            atb = 1
            global atbsk
            atbsk = []

            i = 1
            while i <= +abs(sk):
                ski.append(i)

                i = i + 1

            i = 0
            while i != +abs(sk):
                if sk == 1:
                    atb = 0

                else:
                    atb = sk % ski[i]

                if atb == 0:

                    if 'tikaipoz' not in check:
                        atbsk.append(-abs(ski[i]))

                    atbsk.append(ski[i])

                i = i + 1

            atbsk.sort()

            if 'noklusejums' not in check:
                print(f'Skaitla {sk} dalītāji ir: {atbsk}')

    def listDivPrime(self, sk):
        if isinstance(sk,int)==False or sk<=0:
            print('Pirmskaitlu dalitaju atrasanai ir nepieciesami naturali skaitli!')

        else:
            global atbsk
            global psk
            atbpsk=[]
            self.listDiv(sk,'noklusejums','tikaipoz')
            for x in atbsk:
                self.testPrime(x,'noklusejums')
                atbpsk.append(psk)

            atbpsk[:] = (x for x in atbpsk if x != '')
            print(f'Visi skaitla {sk} pirmskaitlu dalitaji ir: {atbpsk}')


#ievade
print('Ievadi vertibu:')
inp=input('>')

try:
    inp = float(inp)

    if inp.is_integer() == True:
        inp = int(inp)

    elif inp.is_integer() == False:
        inp = float(inp)

except(ValueError):
    inp=str(inp)

print('')

#funkciju palaisana
x = Rekinatajs()
x.Factorial(inp)
print('')
x.Sum(inp)
print('')
x.testPrime(inp)
print('')
x.TableMult(inp)
print('')
x.listDiv(inp)
print('')
x.listDivPrime(inp)