#!/usr/bin.python3
import os
print("		:'######:::'#######::'##::::'##:'##::::'##::::'###::::'##::: ##:'########:::'######::")
print("		'##... ##:'##.... ##: ###::'###: ###::'###:::'## ##::: ###:: ##: ##.... ##:'##... ##:")
print("		 ##:::..:: ##:::: ##: ####'####: ####'####::'##:. ##:: ####: ##: ##:::: ##: ##:::..::")
print("		 ##::@::: ##:@ ##: ## ### ##: ## ### ##:'##::@ ##: ## ## ##: ##:@: ##:. ######::")
print("		 ##::::::: ##:::: ##: ##. #: ##: ##. #: ##: #########: ##. ####: ##:::: ##::..... ##:")
print("		 ##::: ##: ##:::: ##: ##:@:: ##: ##:@:: ##: ##.... ##: ##:. ###: ##::@: ##:'##:@: ##:")
print("		 ######::. #######:: ##:::: ##: ##:::: ##: ##:::: ##: ##:@. ##: ########::. ######::")
print("		:......::::.......:::..:::::..::..:::::..::..:::::..::..::::..::........::::......:::")
print("                       @youtube@:",    "https://www.youtube.com/channel/UCuVdwrJjf9kbWf-DGtrYX6A")
print(" \nUPDATE:(1)\n-----------\nVPN:(3)\n-----------\ngufw:(4)\n----------- \nwine:(2)\n-----------\nBrowser chromium(22)\n-----------\nExit:(99)\n----")
def update():
    import os
    os.system('sudo apt-get update')
def wine():
    import os
    os.system('sudo apt-get install wine')
def vpn():
    import os
    os.system('sudo apt-get -y install  network-manager-openvpn network-manager-openvpn-gnome  network-manager-pptp network-manager-pptp-gnome  network-manager-strongswan network-manager-vpnc  network-manager-vpnc-gnome')
def gufw():
    import os
    os.system('sudo apt-get -y install gufw')
def exit():
    import os
    os.system('exit')
def Browser():
    import os
    os.system('sudo apt-get -y install chromium') 
while True:
    nmbers=input('Enter a number  :')
    if nmbers=='1':
       update()
    elif nmbers=='2':
         wine()
    elif nmbers=='22':  
         Browser
    elif nmbers=='3':   
         vpn()
    elif nmbers=='4':
         gufw()
    elif nmbers=='99':
     break   
     
    else:
         print('intr yur nambr')
