#!/usr/bin/python
#
# Paramiko
#
import paramiko
import sys
import subprocess
import os
from scp import SCPClient
import getpass 

#
# We start with the first hop connection establishment!
#

#Connection to the NAS using paramiko
vm = paramiko.SSHClient()
vm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vm.connect('54.85.197.99', username='user1tunnel', password='shaksham')

#Accepting username and password
print("\n\nWelcome to VPN Server\n\n")
usern=input("Enter username: ")
passwd=getpass.getpass(prompt='Enter password: ')

#Connection establishment
vmtransport = vm.get_transport()
#Connection to LAN on the Localhost
dest_addr = ('127.0.0.1', 12345) 
#Connection to NAS on the Cloud
local_addr = ('54.85.197.99', 22) 
vmchannel = vmtransport.open_channel("direct-tcpip", dest_addr, local_addr)

#
jhost = paramiko.SSHClient()
jhost.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#jhost.load_host_keys('/home/osmanl/.ssh/known_hosts') #disabled#
jhost.connect('localhost', username=usern, password=passwd, sock=vmchannel)
#
stdin, stdout, stderr = jhost.exec_command("pwd") #edited#
#
print ((stdout.read()).decode("utf-8")) #edited#

stdin, stdout, stderr = jhost.exec_command("ls -l") #edited#
#
print (stdout.read().decode("utf-8")) #edited#

#
def present_directory():
    #filename=input()
    stdin, stdout, stderr = jhost.exec_command("ls") #edited#
    print (str(stdout.read().decode("utf-8")))

def change_directory():
    filename=input("Enter directory name: ")
#    stream = os.popen("cd "+filename+" | ls")
    stdin, stdout, stderr = jhost.exec_command("cd Testfolder") #edited#
    #n
    # print (str(stdout.read().decode("utf-8")))
    present_directory()

def previous_directory():
    #filename=input()
    #stream = os.popen("cd .. | ls")
    #filename=input()
    stdin, stdout, stderr = jhost.exec_command("cd .. ") #edited#
    stdin, stdout, stderr = jhost.exec_command("ls ")
    print (str(stdout.read().decode("utf-8")))

def display_file():
    filename=input("Enter file name: ")
    stdin, stdout, stderr = jhost.exec_command("cat "+filename) #edited#
    #stdin, stdout, stderr = jhost.exec_command("ls ")
    print (str(stdout.read().decode("utf-8")))

def download_file():
    filename=input("Enter file name: ")
    with SCPClient(jhost.get_transport()) as scp:
        #scp.put('test.txt')
        scp.get(filename)
    print("\nFile download complete! Check your present working directory\n\n")

def upload_file():
    filename=input("Enter file name: ")
    with SCPClient(jhost.get_transport()) as scp:
        #scp.put('test.txt')
        scp.put(filename)
        print("\nFile upload complete! Check your home directory\n\n")

ch='y'
while(ch!='n'):
    print("\nMenu:\n1. View files in local directory\n2: Change directory\n3: Previous directory\n4: View text file\n5: Download File\n6: Upload File\n7: Exit\n\n")
    choice=int(input('>>>'))
    #filename=input()
    #stdin, stdout, stderr = jhost.exec_command("cat "+filename) #edited#
    #print (stdout.read())

   
    if (choice==1):
        present_directory()
    elif(choice==2):
        change_directory()
    elif(choice==3):
        previous_directory()
    elif(choice==4):
        display_file()
    elif(choice==5):
        download_file()
    elif(choice==6):
        upload_file()
    elif(choice==7):
        break
    else:
        print("Invalid option!")

    print("Do you wish to continue? y/n")
    ch=input()


print("Proceeding to logout!!\nThank you!\n")
jhost.close()

vm.close()
# End
