import socket
import queue
import threading
from colour import Color
import matplotlib.pyplot as plt
from colorama import Fore, x
import matplotlib.pyplot as plt
from lolpython import lol_py
name = """

									 ██▀███   ▒█████   █    ██  ███▄    █ ▓█████▄   ██████ 
									▓██ ▒ ██▒▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▀ ██▌▒██    ▒ 
									▓██ ░▄█ ▒▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒░██   █▌░ ▓██▄   
									▒██▀▀█▄  ▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒░▓█▄   ▌  ▒   ██▒
									░██▓ ▒██▒░ ████▓▒░▒▒█████▓ ▒██░   ▓██░░▒████▓ ▒██████▒▒
									░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░
									  ░▒ ░ ▒░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ▒  ▒ ░ ░▒  ░ ░
									  ░░   ░ ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░  ░ ░  ░ ░  ░  ░  
									   ░         ░ ░     ░              ░    ░          ░  
									                                       ░               

"""
print(Fore.RED + name)
ipTarget = input("[+] | " + "Target: ")


printtxt = f"{ipTarget}"



text = f"""
	 ╔══════════════════════════╗ 
	 ║						             	║
	 ║       ({ipTarget})		    ║
	 ║						            	║
	 ╠══════════════════════════╣
	 ║						            	║									
	 ║ 							            ║
	 ║						            	║ 
	 ╚══════════════════════════╝
"""
text.center(20, '$')

print(Fore.RED + text)
