# ---<=> MODULOS <=>---
import os

# ---<=> FUNCIONES <=>---
def default_scan(Host, Ports):
    os.chdir("nmap")
    os.system(f"nmap.exe -sC -sV -n -T3 -p{Ports} {Host} -oX nmap_output.xml")
    os.system("move nmap_output.xml ../")
    os.chdir("../")

# ---<=> EJECUCION <=>---
if __name__ == '__main__':
    host = input('Host: ')
    ports = input('Ports: ')
    default_scan(host, ports)