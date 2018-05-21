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
                    choices=['Add server', 'Quit'],
                ),
    ]
    answers = inquirer.prompt(menu_list)
    # print(answers["selected_option"])
    if answers["selected_option"] is "Add server":
        print("yes")
        return add_servers()
    elif answers["selected_option"] is "Quit":
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
            host_name = input("Enter your Hostname :")
        except ValueError:
            print("Please enter a valid hostname")
            continue
        try:
            host_ip = int(input("Enter your Host IP :"))
        except ValueError:
            print("Please enter a valid hostIP")
            continue
        try:
            host_user = input("Host user name :")
        except ValueError:
            print("Please enter a valid User name")
            continue
        try:
            host_passwd = input("Enter Host Password :")
        except ValueError:
            print("Please enter a valid hostPassword")
            continue

if __name__ == '__main__':
    main()
