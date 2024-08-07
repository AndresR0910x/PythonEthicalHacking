import scapy.all as scapy 

def scan(ip):
    
    
    arp_request = scapy.ARP(pdst = ip) 
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1)[0]
    
    for element in answered_list:
        print(element[1].psrc)
        print(element[1].hwsrc)
        print("-------------------------------------------------------------------")
    
    #print(answered_list.summary())
    
    
#Observar que el gateway se obtiene haciendo uso del comando sudo route -n 
#Que es un gateway: Un gateway es una puerta de enlace que funciona como un protocolo de comunicacion para la conexion entre diferentes redes. 



#Utilizamos la funcion 
#Para poder identificar a todos los usuerios
#en una subred se coloca /24
scan("192.168.1.1/24")

