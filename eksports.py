#!/usr/bin/env python
# coding: utf-8

# In[1]:


#trijsturis
class trijsturis():
    def __init__(self,mala1,mala2,mala3):
        self.perimetrs=mala1+mala2+mala3
        self.laukums=mala1*mala2/2
        
    def trperimetrs(self):
        print('📐 perimetrs={}'.format(self.perimetrs))
    
    def trlaukums(self):
        print('📐 laukums={}'.format(self.laukums))

#taisnst+kvadr
class taisnsturis():
    def __init__(self,mala1,mala2):
        self.mala1=mala1
        self.mala2=mala2
    
    def tsperimetrs(self):
        perm=self.mala1*2+self.mala2*2
        print('🧈 perimerts={}'.format(perm))
        
    def tslaukums(self):
        lauk=self.mala1*self.mala2
        print('🧈 laukums={}'.format(lauk))
        
    
class kvadrats(taisnsturis):
    def kvperimetrs(self):
        perm=self.mala1*4
        print('🕋 perimerts={}'.format(perm))
    
    def kvlaukums(self):
        lauk=self.mala1*self.mala1
        print('🕋 laukums={}'.format(lauk))
        

#ievade
mgarums1=10
mgarums2=12
mgarums3=13

tr=trijsturis(mgarums1,mgarums2,mgarums3)
ts=taisnsturis(mgarums1,mgarums2)
kv=kvadrats(mgarums1,mgarums2)

#izvade
tr.trperimetrs()
tr.trlaukums()

ts.tsperimetrs()
ts.tslaukums()

kv.kvperimetrs()
kv.kvlaukums()


# In[ ]:




