import struct
import socket 
import textwrap


def ethernet_frame(data):
    dest_mac,src_mac,proto=struct.unpack('! 6s 6s H',data[:14])
    return get_mac_addr(dest_mac),get_mac_addr(src_mac),socket.htons(proto),data[14:]

#Return properly formatted mac addres:
def get_mac_addr(data):
    bytes_str = map('{:02x}'.format,data)
    return ':'.join(bytes_str).upper()




def main():
    #conn = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.nto) 
    conn = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
    conn.bind(("127.0.0.1",15546))
    while True:
        raw_data = conn.recv(65536)
        dst_mac,src_mac,eth_proto,data = ethernet_frame(raw_data)

main()