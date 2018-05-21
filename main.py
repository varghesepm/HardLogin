##### Main function #####
import inquirer
import subprocess

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
            host_ip = int(input("Please enter your Host IP : "))
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
            host_pubkey = str(input("Please enter your Host PubKey : "))
            # print("successfully addded")
        except:
            print("Invalid Host PubKey")
            continue
        break
    if host_name && host_ip && host_user && host_passwd && host_pubkey:
        fun_addToDB()
    else:
        print("Something went wrong")

def fun_addToDB():


if __name__ == '__main__':
    main()
