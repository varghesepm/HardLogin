##### Main function #####
import inquirer
import subprocess
import json
import os

serverDetails = {}

def main():

    subprocess.call('clear',shell=True)
    print("")
    header = "Hard Login Interface"
    print("", header.upper())
    print("",'+'*len(header))
    print("")

    menu_list = [
      inquirer.List('selected_option',
                    message="Select an Option( use UP and DOWN keys)",
                    choices=['Add Server', 'List Servers', 'Quit'],
                ),
    ]
    answers = inquirer.prompt(menu_list)
    # print(answers["selected_option"])
    if answers["selected_option"] == "Add Server":
        add_servers()
    elif answers["selected_option"] == "List Servers":
        return 0
    elif answers["selected_option"] == "Quit":
        return 0
    else:
        print ("Unknown option Selected")


def add_servers():
    subprocess.call('clear',shell=True)
    print("")
    header = "Add Server Details"
    print("", header.upper())
    print("",'+'*len(header))
    print("")

    while True:
        try:
            host_name = str(input("Please enter your Host name : "))
        except:
            print("Invalid Host Name")
            continue
        break
    while True:
        try:
            host_ip = str(input("Please enter your Host IP : "))
        except:
            print("Invalid Host IP")
            continue
        break
    while True:
        try:
            host_user = str(input("Please enter your Host Username : "))
        except:
            print("Invalid Host Username")
            continue
        break
    while True:
        try:
            host_passwd = str(input("Please enter your Host Password : "))
        except:
            print("Invalid Host Password")
            continue
        break
    while True:
        try:
            host_port = str(input("Please enter your Host Port : "))
        except:
            print("Invalid Host Port")
            continue
        break
    while True:
        try:
            host_pubkey = str(input("Please enter your Host PubKey : "))
            # print("successfully addded")
        except:
            print("Invalid Host PubKey")
            continue
        break
    if host_name and host_ip and host_user and host_passwd and host_port and host_pubkey:
        fun_addTodict(name=host_name,ip=host_ip,user=host_user,passwd=host_passwd,port=host_port,pubkey=host_pubkey)
    else:
        print("Something went wrong")

def fun_addTodict(**kwargs):
    with open('serverlist.json','r') as json_format:
        serverDetails = json.load(json_format)

    name = kwargs['name']
    print(name)
    ip = kwargs['ip']
    user = kwargs['user']
    passwd = kwargs['passwd']
    port = kwargs['port']
    pubkey = kwargs['pubkey']
    lengofDict = len(serverDetails)
    #print(lengofDict)
    if lengofDict == 0:
        serverDetails[1] = {"host_name" : name, "host_ip":ip, "host_user":user, "host_passwd":passwd, "host_port":port, "host_pubkey":pubkey}
        print(serverDetails)
    else:
        #print(lengofDict)
        serverDetails[len(serverDetails) + 1] = {"host_name" : name, "host_ip":ip, "host_user":user, "host_passwd":passwd, "host_port":port, "host_pubkey":pubkey}
    with open('serverlist.json','w') as json_format:
        json.dump(serverDetails,json_format,indent=2)
    print("server with hostname :" + name + " added")
#
# def createFile():
#     if os.path.exists('./serverlist.json'):
#         pass
#     else:
#         subprocess.call('touch serverlist.json',shell=True)

if __name__ == '__main__':
    main()
