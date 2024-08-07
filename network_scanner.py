import scapy.all as scapy 

def scan(ip):
    
    
    arp_request = scapy.ARP(pdst = ip) 
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose=False)[0]
    
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list
        
def print_result(result_list):
    print("\nIP\t\t\tMAC address\n----------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

scan_result = scan("192.168.1.1/24")
print_result(scan_result)
    
    #print(answered_list.summary())
    
    
#Observar que el gateway se obtiene haciendo uso del comando sudo route -n 
#Que es un gateway: Un gateway es una puerta de enlace que funciona como un protocolo de comunicacion para la conexion entre diferentes redes. 



#Utilizamos la funcion 
#Para poder identificar a todos los usuerios
#en una subred se coloca /24


