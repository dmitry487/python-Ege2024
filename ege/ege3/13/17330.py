def ip_to_binary(ip):
    binary_ip = []
    octets = ip.split('.')
    for octet in octets:
        binary_ip.append(format(int(octet), '08b'))
    return binary_ip

def mask_length(mask):
    binary_mask = ''.join(ip_to_binary(mask))
    return binary_mask.find('0')

ip1 = "98.162.71.150"
ip2 = "98.162.71.140"
mask = "255.255.240.0"

print(mask_length(mask))