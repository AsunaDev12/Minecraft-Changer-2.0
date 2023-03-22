import os
import requests
from colorama import init, Fore, Style

os.system('cls' if os.name == 'nt' else 'clear')

init()  

def validate_session(session_id):
    headers = {
        'Authorization': f'Bearer {session_id}'
    }

    response = requests.get('https://api.minecraftservices.com/minecraft/profile', headers=headers)

    if response.status_code == 200:
        return True
    else:
        return False

def change_username():
    session_id = input(Fore.CYAN + 'Enter your session ID: ' + Style.RESET_ALL)

    if not validate_session(session_id):
        print(Fore.RED + 'Invalid session ID.' + Style.RESET_ALL)
        return

    new_username = input(Fore.CYAN + 'Enter your new username: ' + Style.RESET_ALL)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {session_id}'
    }

    response = requests.put(f'https://api.minecraftservices.com/minecraft/profile/name/%7Bnew_username%7D', headers=headers, json={})

    if response.status_code == 200:
        print(Fore.GREEN + f'Username successfully changed to {new_username}!' + Style.RESET_ALL)
    elif response.status_code == 400:
        print(Fore.RED + 'Failed to change username. Minecraft name may not be changeable or Minecraft API may be down.' + Style.RESET_ALL)
        print(Fore.CYAN + 'Please try again at a later date.' + Style.RESET_ALL)
    else:
        print(Fore.RED + 'Failed to change username.' + Style.RESET_ALL)


def change_skin():
    session_id = input(Fore.CYAN + 'Enter your session ID: ' + Style.RESET_ALL)

    if not validate_session(session_id):
        print(Fore.RED + 'Invalid session ID.' + Style.RESET_ALL)
        return

    skin_path = input(Fore.CYAN + 'Enter the path to your skin file: ' + Style.RESET_ALL)

    with open(skin_path, 'rb') as f:
        skin_data = f.read()

    headers = {
        'Authorization': f'Bearer {session_id}'
    }

    files = {
        'variant': (None, 'classic'),
        'file': ('skin.png', skin_data, 'image/png')
    }

    response = requests.post('https://api.minecraftservices.com/minecraft/profile/skins', headers=headers, files=files)

    if response.status_code == 200:
        print(Fore.GREEN + 'Skin successfully changed!' + Style.RESET_ALL)
    else:
        print(Fore.RED + 'Failed to change skin. make sure the image is named skin.png' + Style.RESET_ALL)


while True:
    print(Fore.YELLOW + 'MINECRAFT CHANGER' + Style.RESET_ALL)
    print()
    print(Fore.YELLOW + 'Select an option:' + Style.RESET_ALL)
    print(Fore.YELLOW + '1. Change username' + Style.RESET_ALL)
    print(Fore.YELLOW + '2. Change skin' + Style.RESET_ALL)
    print(Fore.YELLOW + '3. Exit' + Style.RESET_ALL)
    print()
    option = input(Fore.GREEN + "[ > ] " + Style.RESET_ALL)

    if option == '1':
        change_username()
    elif option == '2':
        change_skin()
    elif option == '3':
        break
    else:
        print(Fore.RED + 'Invalid option selected.' + Style.RESET_ALL)

    input('Press enter to continue...')
    os.system('cls' if os.name == 'nt' else 'clear')
