##### Main function #####
import inquirer
import subprocess

def head_main():

    subprocess.call('clear',shell=True)
    print("")
    header = "Hard Login Interface"
    print("", header.upper())
    print("",'+'*len(header))
    print("")

    menu_list = [
      inquirer.List('selected_option',
                    choices=['Host Managent', 'Parallel Shell Tool', 'Quit'],
                    message="Select an Option( use UP and DOWN keys)",
                ),
    ]
    answers = inquirer.prompt(menu_list)

head_main()
