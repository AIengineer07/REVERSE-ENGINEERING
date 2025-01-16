# Termux Custom Banner

Create a custom banner for Termux that displays personalized text or ASCII art whenever you open the terminal.

---

## Prerequisites
Make sure you have Termux installed on your device.

---

## Steps to Create a Custom Banner

### 1. Install Required Packages
Run the following command to install `figlet` and `toilet` for creating ASCII art:
```bash
pkg update && pkg upgrade -y
pkg install figlet toilet -y
nano ~/.bashrc
# Custom Banner Script
clear
echo -e "\033[1;32mWelcome to Termux, SALMAN!"
figlet SALMAN | lolcat
echo -e "\033[1;34mType \033[1;36mhelp \033[1;34mfor a list of commands.\033[0m"
Welcome to Termux, SALMAN!

_____       _                                 
 / ____|     | |                                
| (___   __ _| | ___ _ __ ___   __ _ _ __ _   _ 
 \___ \ / _` | |/ _ \ '_ ` _ \ / _` | '__| | | |
 ____) | (_| | |  __/ | | | | | (_| | |  | |_| |
|_____/ \__,_|_|\___|_| |_| |_|\__,_|_|   \__, |
                                           __/ |
                                          |___/
     


toilet SALMAN --metal
 figlet SALMAN | lolcat
