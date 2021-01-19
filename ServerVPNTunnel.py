import os
import subprocess

print("\n\nHi and Welcome to VPN Major Project")
print("You can now proceed to connect your LAN resources to the NAS\n")

connections=[]

def addconnection():
    command="ssh -f -N user1tunnel@ec2-54-85-197-99.compute-1.amazonaws.com -R "
    connection_port=int(input("Enter Network port to connect: "))
    nas_port=int(input("Enter NAS broadcast port: "))
    description=input("Enter description for this connection: ")

    for x in connections:
        if(x.count(str(connection_port))):
            print("Network Port already in use for: ", x[0])
            connection_port=int(input("Enter new Network port to connect: "))
            break
    connection=[description,connection_port, nas_port]
    connections.append(connection)
    command=command+ str(nas_port)+":localhost:"+str(connection_port)
#    password=input("Enter your login password: ")
    print(command)
    os.system(command)
#    output = ssh.read()
#    print(output)
    return


def display_connection():
    stream = os.popen("netstat -an | grep 54.85.197.99 | grep ESTABLISHED")
    output = stream.read()
#    print(output)
#    print (len(output))
    a=output.split("\n")
#    print(a)
    for i in range(0,len(a)-1):
        if(connections.count(a[i])==0):
            connections.append(a[i])
    l=len(connections)

    if (l==0):
        print("No present connections!")
        return
    for x in connections:
        print(x)


def system_stats():
    stream = os.popen("mpstat")
    output = stream.read()
    print(output)

def users_logged_in():
    stream = os.popen('last | grep "still logged in"')
    output = stream.read()
    print(output)



f='y'
while(f=='y'):
    print("Present Connections:")
    display_connection()
    print("Menu:\n1. Add another connection \n2. View present connections\n3. System Statistics \n4: Users Still logged in\n5: Exit\n")
    c=int(input())
    if (c==1):
        addconnection()
    elif(c==2):
        display_connection()
    elif(c==3):
        system_stats()
    elif(c==4):
        users_logged_in()
    elif(c==5):
        exit()
    else:
        print("Invalid option!")

    print("Do you wish to continue? y/n")
    f=input()



#ssh = os.popen('sshpass -p "ishaak15" ssh ubuntu@192.168.43.24')
#stream = os.popen('ls -al')
#output = stream.read()
#print(output)




