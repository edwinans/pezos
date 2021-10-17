#!/usr/bin/env python3

import socket
import encode_message
import util
import ed25519

HOST = '78.194.168.67'  # The server's hostname or IP address
PORT = 1337        # The port used by the server

pk = "e522991d21d463bad9b74498a22172ae22b133e486adcedbb3a56d982e6a31fd"
sk = "d"

pk_bytes = util.encode_pk(pk)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    seed = s.recv(1024)
    h_seed = util.hash(seed)
    sig = util.encode_sig(h_seed, sk, pk)
    s.sendall(pk_bytes)
    s.sendall(sig)
    get_hd = encode_message.encode_get_currrent_head()
    s.sendall(get_hd)
    data = s.recv(1024)


print('Received', repr(data))
