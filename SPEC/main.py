#Lietotnes kods

#bibliotekas
import requests
from cryptography.fernet import Fernet
import mysql.connector
from decimal import Decimal
import os
import shutil
import ctypes
import json
from datetime import datetime
import pytz

#funkcijas
def dienasvidejais(vert,cipskaizkomata): #videja aprekinasana
    vertSk=24
    vertSum=0
    i=0
    while i<vertSk:
        vertSum=vertSum+vert[i]
        
        i=i+1
    vertVid=vertSum/vertSk
    vertVid=Decimal(str(vertVid))
    return round(vertVid,cipskaizkomata)

#datu apstrade
def sifresana(atrv, lat, long, tzona): #datu sifresanas funkcija
    global sifratslega
    global sifrs
    
    dati=[atrv,lat,long,tzona]
    sifrdati=[]
    sifrs=Fernet(sifratslega)
    
    for i in dati:
        i=str(i)
        i=i.encode('utf-8')
        sifrdati.append(sifrs.encrypt(i))

    return sifrdati

def atsifresana(nepsifrdati): #sifreto datu atsifresanas funkcija
    global sifrs
    # jsonsifrfails=open(dirsifrfails, 'rb')
    # sifrdatinofaila=jsonsifrfails.readlines()
    # atsifrdati=atsifresana(sifrdatinofaila)
    # jsonsifrfails.close()
    # print(atsifrdati)
    
    i=-1
    while len(nepsifrdati)/2>i:
        i=i+1
        nepsifrdati.pop(i)
        
    atsifrdati=[]
    i=0
    
    while len(nepsifrdati)>i:
        x=nepsifrdati[i]
        x=x.decode('utf-8')
        x=x.replace("b'",''); x=x.replace("'",'')
        x=sifrs.decrypt(x)
        atsifrdati.append(x.decode('utf-8'))
        
        i=i+1
    
    return atsifrdati

#datu saglabasana, atversana un papildinasana
def saglabasana(nosauk, atrv, lat , long, tzona, augs, augid, iestadlaiks, auglaiks): #saglaba datus json failos
    global auganr
    global dirmape
    
    #parastie
    dati={'nosaukums':nosauk,
          'augs':augs,
          'augaid': augid,
          'iestadisanaslaiks':iestadlaiks,
          'atlikusaisaugsanaslaiks':auglaiks
         }
    
    dirmapesast=sorted(os.listdir(dirmape), key=len)
    if len(dirmapesast)>0:
        num=[]
        pedfails=dirmapesast[-1]
        for i in pedfails:
            if i.isdigit():
                num.append(i)
        
        num=''.join(num)
        auganr=int(num)+1
        
    dirfails=os.path.join(dirmape, f'{auganr}augs.json')
    jsonfails=open(dirfails, 'w')
    jsondati=json.dumps(dati)
    jsonfails.write(jsondati)
    jsonfails.close()
    
    #sifretie
    sifrdatukopa=sifresana(atrv,lat,long,tzona)
    sifrdati=f'atrasanasvieta:\n{sifrdatukopa[0]}\nlatitude:\n{sifrdatukopa[1]}\nlongitude:\n{sifrdatukopa[2]}\nlaikazona:\n{sifrdatukopa[3]}'
    sifrdati=sifrdati.encode('utf-8')
    
    dirsifrfails=os.path.join(dirmape, f'{auganr}augslok.json')
    jsonsifrfails=open(dirsifrfails, 'wb')
    jsonsifrfails.write(sifrdati)
    jsonsifrfails.close()
    
    auganr=auganr+1

def papildinasana(): #papildina datus json failos
    pass

def atversana(): #iznem datus no saglabatajiem json failiem
    pass

#laikapstaklu datu iegusana un analize
def laikapstakli(lat,long,tzona): #tagadejo, un nakotnes prognozeto laikapstaklu datu ieguve
    
#tagadejo laikapstaklu datu iegusana
    Url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&daily=temperature_2m_min,precipitation_probability_mean,precipitation_hours,rain_sum&hourly=temperature_2m,windspeed_10m,soil_moisture_0_1cm,soil_moisture_1_3cm,soil_moisture_3_9cm,soil_moisture_9_27cm,soil_moisture_27_81cm&current_weather=true&timezone={tzona}"
    #https://api.open-meteo.com/v1/forecast?latitude=56.946&longitude=24.10589&daily=temperature_2m_min,precipitation_probability_mean,precipitation_hours,rain_sum&hourly=temperature_2m,windspeed_10m,soil_moisture_0_1cm,soil_moisture_1_3cm,soil_moisture_3_9cm,soil_moisture_9_27cm,soil_moisture_27_81cm&current_weather=true&timezone=Europe%2FRiga
    
    Dati=requests.get(Url)
    Dati=Dati.json()
    
    #stunda
    hDati=Dati['hourly']
    hTemp=hDati['temperature_2m'] #C
    hVejaatr=hDati['windspeed_10m'] #km/h
    hMitr0_1=hDati['soil_moisture_0_1cm'] #m^3/m^3
    hMitr1_3=hDati['soil_moisture_1_3cm'] #m^3/m^3
    hMitr3_9=hDati['soil_moisture_3_9cm'] #m^3/m^3
    hMitr9_27=hDati['soil_moisture_9_27cm'] #m^3/m^3
    hMitr27_81=hDati['soil_moisture_27_81cm'] #m^3/m^3
    
    #diena
    dDati=Dati['daily']
    dTempmin=dDati['temperature_2m_min'] #C
    dNokriesp=dDati['precipitation_probability_mean'] #%
    dNokrlaiks=dDati['precipitation_hours'] #h
    dLietussum=dDati['rain_sum'] #mm
    
    dTempvid=dienasvidejais(hTemp,1) #C
    dVejaatrvid=dienasvidejais(hVejaatr,1) #km/h
    dhMitr0_1vid=dienasvidejais(hMitr0_1,3) #m^3/m^3
    dhMitr1_3vid=dienasvidejais(hMitr1_3,3) #m^3/m^3
    dhMitr3_9vid=dienasvidejais(hMitr3_9,3) #m^3/m^3
    dhMitr9_27vid=dienasvidejais(hMitr9_27,3) #m^3/m^3
    dhMitr27_81vid=dienasvidejais(hMitr27_81,3) #m^3/m^3

#datu analize

    
def main(): #galvena dala
    global dirmape
    global cursors
    
    #saglabato augu sk parbaude
    dirmapesast=os.listdir(dirmape)
    
    #augu izvelne
    print('Opcijas: (ievadi nr)')
    print('1. Pievienot augu')
    if len(dirmapesast)>0:
        print('2. Augu izvelne')

    while 1>0:
        opcija=input('> ')
        if opcija=='1':
            break
        
        if opcija=='2' and len(dirmapesast)>0:
            break
    
    if opcija=='1': #pievienosana
        print('Ievadi nosaukumu: (lidz 200 rakstzimem)')
        while 1>0:
            nosaukums=input('> ')
            if len(nosaukums)<=200:
                break
    
        print('')
        print('Ievadi atrasanas vietu: (Valsts-Pilseta)')
        O=0
        while 1>O:
            #atrvieta=input('> ')
            atrvieta='Latvia-Riga'
            atrvietas=atrvieta.split('-')
            if len(atrvietas)==2:
                pilseta=atrvietas[1]
                valsts=atrvietas[0]
                geoUrl=f"https://geocoding-api.open-meteo.com/v1/search?name={pilseta}"
                Dati=requests.get(geoUrl)
                Dati=Dati.json()
                Dati=Dati['results']
                for i in Dati:
                    j=i['country']
                    if j==valsts:
                        latitude=i['latitude']
                        longitude=i['longitude']
                        laikazona=i['timezone']
                        O=1
                        print('ok')
                        break
        
        flaikazona=laikazona.split('/')
        flaikazona='%2F'.join(flaikazona)
        
        #datu ieguve no datubazes
        print('')
        print('Izvelies auga veidu: (ievadi nr)')
        sql='SELECT nosaukums FROM augi'
        cursors.execute(sql)
        dbdati=cursors.fetchall()
        
        auguskaits=[]
        augaveidi=[]
        j=0
        for i in dbdati:
            j=j+1
            auguskaits.append(str(j))
            augaveidi.append(i[0])
            print(f'{j}. {i[0]}')
        
        while 1>0:
            augaveids=input('> ')
            if augaveids in auguskaits:
                break
        
        augaveids=augaveidi[int(augaveids)-1]
        
        sql=f"SELECT id, augsanas_ilgums FROM augi WHERE nosaukums='{augaveids}'"
        cursors.execute(sql)
        augadati=cursors.fetchall()
        augadati=augadati[0]
        
        augaid=int(augadati[0])
        augilgums=int(augadati[1])*365
        iestadlaiks=str(datetime.now(pytz.timezone(laikazona)))
        
        laikapstakli(latitude, longitude, flaikazona)
        
        saglabasana(nosaukums, atrvieta, latitude, longitude, flaikazona, augaveids, augaid, iestadlaiks, augilgums)
    
    if opcija=='2': #atversana
        pass
        #turpinas no json


#globalie mainigie un kods
mapesnosauk='augi'
auganr=1

dir= os.getcwd()
dirsast=os.listdir(dir)
dirmape=os.path.join(dir, mapesnosauk)

dirsast=os.listdir(dir)
if mapesnosauk not in dirsast: #"augi" mapes izveide, ja ta nepastav
    os.makedirs(dirmape)
    ctypes.windll.kernel32.SetFileAttributesW(dirmape, 0x02)

dirmapesast=os.listdir(dirmape)

#datu sifresanas atslega
diratslega=os.path.join(dir, 'atslega.key')

if 'atslega.key' not in dirsast:
    sifratslega=Fernet.generate_key()
    
    failsatslega=open(diratslega, 'wb')
    failsatslega.write(sifratslega)
    failsatslega.close()
    
    ctypes.windll.kernel32.SetFileAttributesW(diratslega, 0x02)
    
    if len(dirmapesast)>0:
        shutil.rmtree(dirmape)
        os.makedirs(dirmape)
        ctypes.windll.kernel32.SetFileAttributesW(dirmape, 0x02)
        print(''); print(''); print('')
        print('!!!! VISI DATI IZDZESTI SIFRATSLEGAS KOMPROMIZACIJAS DEL !!!!')
        print(''); print(''); print('')

failsatslega=open(diratslega, 'rb')
sifratslega=failsatslega.read()
failsatslega.close()

dirfails=os.path.join(dirmape, 'augs.json')

#MySql datu bazes savienosana
datubaze = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Skola12dit",
  database="augudatubaze"
  
)

cursors=datubaze.cursor()


#galvenais loops
main()
