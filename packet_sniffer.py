import scapy.all as scapy
from scapy.layers import http
import pyfiglet
import argparse


banner = pyfiglet.figlet_format("PACKET SNIFFER", font="slant", justify="center", width=100)
print("\033[36m"+banner+"\033[39m")




def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Specify interface to sniff its data")
    arguments = parser.parse_args()
    return arguments.interface


def sniff_packets(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet, filter="tcp port 80", promisc=True)


def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        
        host = packet[http.HTTPRequest].Host.decode() if isinstance(packet[http.HTTPRequest].Host, bytes) else packet[http.HTTPRequest].Host
        path = packet[http.HTTPRequest].Path.decode() if isinstance(packet[http.HTTPRequest].Path, bytes) else packet[http.HTTPRequest].Path

        print(f"\n\033[31m[+] HTTP Request ->> {host}{path}\033[36m")
        
        if packet.haslayer(scapy.Raw):
        
            load = packet[scapy.Raw].load.decode(errors="ignore").lower()

            keys = [
                "username", "user", "userid", "user_id", "login", "email", "mail",
                "password", "pass", "pwd", "secret", "token"
            ]
            for key in keys:
                if key in load:
                    print(f"\033[31m[+] Possible sensitive data ->> {load}\033[39m\n")
                    break
    else:
        
        if packet.haslayer(scapy.IP):
            ip_src = packet[scapy.IP].src
            ip_dst = packet[scapy.IP].dst
            protocol = packet[scapy.IP].proto
            print(f"IP Packet: {ip_src} --> {ip_dst} Protocol: {protocol}")
            if packet.haslayer(scapy.TCP):
                src_port = packet[scapy.TCP].sport
                dst_port = packet[scapy.TCP].dport
                print(f"\033[36mTCP Segment: {ip_src} : {src_port} --> {ip_dst} : {dst_port}\033[39m")
            elif packet.haslayer(scapy.UDP):
                src_port = packet[scapy.UDP].sport
                dst_port = packet[scapy.UDP].dport
                print(f"\033[36mUDP Datagram: {ip_src} : {src_port} --> {ip_dst} : {dst_port}\033[39m")


# Replace 'eth0' with your network interface
iface = get_arguments()

# Start sniffing on the specified interface
print("\033[33m[*] Sniffer started...\n\033[39m")
sniff_packets(iface)
