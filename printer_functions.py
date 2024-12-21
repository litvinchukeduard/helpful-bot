from colorama import Fore, Back, Style, init

def print_error(message: str):
    print(Fore.RED + message + Style.RESET_ALL)

def print_success(message: str):
    print(Fore.GREEN + message + Style.RESET_ALL)

def input_colored(message: str):
    return input(Fore.BLUE + message + Fore.YELLOW)
