#Arts Inarts Kubilis

from tabulate import tabulate #pip install tabulate

class Rasists:  # autokorekts
    def __init__(self):
        pass

    def Factorial(self, sk):
        i = sk
        atb = 1
        while i != 0:
            atb = atb * i
            i = i - 1

        print(f'{sk}! = {atb}')

    def Sum(self, sk):
        i = sk
        atb = 0
        while i != 0:
            atb = atb + i
            i = i - 1

        print(f'Skaitlu summa lidz skaitlim {sk} = {atb}')

    def testPrime(self, sk):
        ski = [2, 3, 4, 5, 6, 7, 8, 9]
        i = 0
        atb=1
        while i != 8:
            if sk!=ski[i]:
                if sk==1:
                    atb=0

                else:
                    atb = sk % ski[i]

                if atb==0:
                    print(f'Skaitlis {sk} nav pirmskaitlis')
                    break

                else:
                    print(f'Skaitlis {sk} ir pirmskaitlis')
                    break

            i = i + 1

    def TableMult(self, sk):
        top0=['']
        top1=[]
        top2=[]
        i=1
        while i<=sk:
            top0.append(i)

            i = i + 1

        i=1
        while i <= sk:
            top1=[]
            top1.append(i)
            l=1
            while l<=sk:
                darb=top0[i]*l
                top1.append(darb)

                l=l+1
            top2.append(top1)
            i=i+1
        table=top2
        print(f'Reizrekina tabula lidz skailim {sk}: ')
        print('')
        print(tabulate(table,headers=top0,tablefmt="plain"))
        print('')

    def listDiv(self):
        pass

    def listDivPrime(self):
        pass


x = Rasists()
#x.Factorial(5)
#x.Sum(5)
#x.testPrime(2)
x.TableMult(11)
