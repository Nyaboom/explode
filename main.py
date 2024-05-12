import colorama
from colorama import Back, Fore, Style
import time

def print_explode():
    print(Back.YELLOW + Fore.BLACK + "explode" + Style.RESET_ALL)

if __name__ == "__main__":
    colorama.init()
    try:
        while True:
            print_explode()
        time.sleep(2)  # Wait for 2 seconds
    finally:
        colorama.deinit()
