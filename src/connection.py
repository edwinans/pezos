#!/usr/bin/env python3

import socket
import encode_message
import util

HOST = '78.194.168.67'  
PORT = 1337        

pk, sk = util.read_keys()

pk_bytes = util.encode_pk(pk)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    seed = s.recv(1024)
    sig = util.encode_sig(seed, sk, pk)
    s.send(pk_bytes)
    s.send(sig)
    get_hd = encode_message.encode_get_currrent_head()
    s.send(get_hd)
    head = s.recv(1024)

print('Received seed <- ', seed.hex())
print('Received head <- ', head.hex())
