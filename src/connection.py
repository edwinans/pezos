#!/usr/bin/env python3

import socket
from encode_message import encode_message
import encode_message as em
import decode_message as dm
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
    get_hd = em.encode_get_currrent_head()
    s.send(get_hd)
    buf = s.recv(1024)
    print('Received head <- ', buf.hex())
    head_block = dm.decode_block(buf)
    return head_block

def get_block(level):
    msg = encode_message(em.encode_get_block(level))
    s.send(msg)
    buf = s.recv(1024)
    print('Received block <- ', buf.hex())
    block = dm.decode_block(buf)
    return block

def get_block_state(level):
    msg = encode_message(em.encode_get_state(level))
    s.send(msg)
    buf = s.recv(1024)
    print('Received block_state <- ', buf.hex())
    state = dm.decode_state(buf)
    return state

def disconnect():
    s.close()
