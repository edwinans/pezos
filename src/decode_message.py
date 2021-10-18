import util


from model.state import State
from model.block import Block
from model.operation import Operation


def decode_block(msg):
    block = decode_message(msg)
    return (
        Block(block[0:4], block[4:36], block[36:44], block[44:76], block[76:108], block[108:172])
    )

def decode_state(msg):
    state = decode_message(msg)
    pk = state[:32]
    pred_time = state[32:40]
    nb_bytes = state[40:44]
    accounts = state[44:]
    return State(pk, pred_time, nb_bytes, accounts)

def decode_operation_list(message):
    operations_list = []
    i = 0
    while i < len(message):
        tag = util.decode_entier(message[i:i+2])
        i+=2
        if tag == 1 or tag == 3 or tag == 4:
            operations_list.append(Operation(message[i-2:i], message[i:i+32], None))
            i += 32
        if tag == 2:
           operations_list.append(Operation(message[i-2:i],None, message[i:i+8]))
           i += 8
        if tag == 5:
            operations_list.append(Operation(message[i - 2:i], None, None))
    return operations_list


def decode_message(message):
    return (
        message[2:]
    )

def decode_applicative_message(message):
    tag = util.decode_entier(message[0:2])
    if tag == 2 or tag == 4:
        return decode_block(message[2:])
    if tag == 3 or tag == 5 or tag == 7:
        return message[2:]
    if tag == 6:
        return decode_operation_list[message[4:]]
    if tag == 8:
        return State(message[2:34], message[34:42], message[42:46], message[46:])
    if tag == 9:
        return message[2:]


def decode_operations(operation):
    tag = util.decode_entier(operation[0:2])
    if tag == 1 or tag == 2 or tag == 3 or tag == 4:
        return operation[2:]
