#!/usr/bin/env python3

import socket
from encode_message import encode_message
import encode_message as em
import util

HOST = '78.194.168.67'  
PORT = 1337        

def connect():
    pk, sk = util.read_keys()
    pk_bytes = util.encode_pk(pk)
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    seed = s.recv(1024)
    sig = util.encode_sig(seed, sk, pk)
    s.send(pk_bytes)
    s.send(sig)
    print('Received seed <- ', seed.hex())

def get_current_head():
    get_hd = encode_message.encode_get_currrent_head()
    s.send(get_hd)
    head = s.recv(1024)
    print('Received head <- ', head.hex())
    return head

def get_block(level):
    msg = encode_message(em.encode_get_block(level))
    s.send(msg)
    block = s.recv(1024)
    return block 



def disconnect():
    s.close()
