#!/usr/bin/env python

#Permite correr comandos 
import subprocess 

#La siguiente libreria permite crear comando 
import optparse
import re

def get_arguments():
    #Se crea el objeto de tipo optparser 
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest= "interface", help= "Interface to change MAC address!")
    parser.add_option("-m", "--mac", dest= "new_mac", help= "Change MAC address!")
    (options, arguments) = parser.parse_args()
    
    if not options.interface:
        parser.error("[-] Pls enter the interface, use --help for more inf")
    elif not options.new_mac: 
        parser.error("[-] Pls enter MAC direction, use --help for more inf")
    
    return options

def change_mac(interface, new_mac): 
    print("[+] Change MAC direction for " + interface + " to " + new_mac)
    #Sec form
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_res = subprocess.check_output(["ifconfig", options.interface]).decode('utf-8')
    mac_address_srch_res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_res)
    
    if mac_address_srch_res:
        return mac_address_srch_res.group(0)
    else:
        print("[-] MAC address could not be read")
    
    
    
options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + current_mac)

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] Address MAC successfully changed to "+ current_mac)
else:
    print("[-] Address MAC was not changed!")

#change_mac(options.interface, options.new_mac)




#Forma no tan segura de hacerlo ya que la terminal se encuentra activada 
#subprocess.call("ifconfig " + interface + " down", shell=True)
#subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
#subprocess.call("ifconfig " + interface + " up ", shell=True)


