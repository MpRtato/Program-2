class Rasists: #autokorekts
    def __init__(self):
        pass

    def Factorial(self,sk):
        i=sk
        atb=1
        while i!=0:
            atb=atb*i
            i=i-1
            
        return atb
    
    def Sum(self,sk):
        i=sk
        atb=0
        while i!=0:
            atb=atb+i
            i=i-1
            
        return atb
        
    def testPrime(self,sk):
        ski=[1,2,3,4,5,6,7,8,9]
        i=0
        while i!=9:
            atb=sk % ski[i]
            print('a: '+str(ski[i]))
            print(atb)
            i=i+1
        
        
    def TableMult(self):
        pass
    
    def listDiv(self):
        pass
        
    def listDivPrime(self):
        pass
    
x=Rasists()
#x.Factorial(5)
#x.Sum(5)
x.testPrime(2)
