#!/usr/bin/env python3

import socket
import encode_message as em
import decode_message as dm
from model.operation import Operation
import util

HOST = '78.194.168.67'
PORT = 1337


def connect():
    global s, pk, sk, pk_bytes
    pk, sk = util.read_keys()
    pk_bytes = bytes(bytearray.fromhex(pk))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    seed = s.recv(1024)
    sig = util.encode_sig(seed, sk, pk)
    s.send(em.encode_message(pk_bytes))
    s.send(sig)
    print('Received seed <- ', seed.hex())


def get_current_head():
    get_hd = em.encode_get_currrent_head()
    s.send(get_hd)
    buf = s.recv(1024)
    print('Received head <- ', buf.hex())
    head_block = dm.decode_block(buf)
    return head_block

def get_current_head_async():
    buf = s.recv(1024)
    print('Received head <- ', buf.hex())
    head_block = dm.decode_block(buf)
    return head_block

def get_block(level):
    msg = em.encode_get_block(level)
    s.send(msg)
    buf = s.recv(1024)
    print('Received block <- ', buf.hex())
    block = dm.decode_block(buf)
    return block


def get_block_state(level):
    msg = em.encode_get_state(level)
    s.send(msg)
    buf = s.recv(1024)
    print('Received block_state <- ', buf.hex())
    state = dm.decode_state(buf)
    return state


def get_block_operations(level):
    msg = em.encode_get_block_operations(level)
    s.send(msg)
    buf = s.recv(1024)
    print('Received block_operations <- ', buf.hex())
    operations = dm.decode_operation_list(buf)
    return operations


def inject_operation(op):
    op_b = op.get_bytes()
    msg = em.encode_inject_operation(op_b)
    s.send(msg)
    print('operation {} injected: {}'.format(op.get_tag(), msg.hex()))
    return True


def inject_bad_predecessor(hash):
    op = Operation(tag=1, hash=hash, user_pk=pk_bytes, sk=sk)
    return inject_operation(op)


def inject_bad_timestamp(time):
    op = Operation(tag=2, time=time, user_pk=pk_bytes, sk=sk)
    return inject_operation(op)


def inject_bad_operations_hash(hash):
    op = Operation(tag=3, hash=hash, user_pk=pk_bytes, sk=sk)
    return inject_operation(op)


def inject_bad_context_hash(hash):
    op = Operation(tag=4, hash=hash, user_pk=pk_bytes, sk=sk)
    return inject_operation(op)


def inject_bad_signature():
    op = Operation(tag=5, user_pk=pk_bytes, sk=sk)
    return inject_operation(op)


def disconnect():
    s.close()
