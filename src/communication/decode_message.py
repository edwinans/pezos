from utility import util

from model.state import State
from model.block import Block
from model.operation import Operation

"""
Decode byte messages and wrap it to the corresponding class.
"""

def decode_block(msg):
    block = decode_message(msg)
    return Block(
        block[0:4],
        block[4:36],
        block[36:44],
        block[44:76],
        block[76:108],
        block[108:172],
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
    tag = util.decode_int(message[:2])
    size = util.decode_int(message[2:4])
    assert size == len(message) - 4
    assert tag == 6
    i = 4
    while i < len(message):
        tag = util.decode_int(message[i: i + 2])
        if tag == 1 or tag == 3 or tag == 4:
            operations_list.append(
                Operation(
                    tag=tag,
                    hash=message[i + 2: i + 34],
                    user_pk=message[i + 34: i + 66],
                    signature=message[i + 66: i + 130],
                )
            )
            i += 130
        if tag == 2:
            operations_list.append(
                Operation(
                    tag=tag,
                    time=message[i + 2: i + 10],
                    user_pk=message[i + 10: i + 42],
                    signature=message[i + 42: i + 106],
                )
            )
            i += 106
        if tag == 5:
            operations_list.append(
                Operation(
                    tag=tag,
                    user_pk=message[i + 2: i + 34],
                    signature=message[i + 34: i + 98],
                )
            )
            i += 98

    return operations_list


def decode_message(message):
    return message[2:]


def decode_applicative_message(message):
    tag = util.decode_int(message[0:2])
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
    tag = util.decode_int(operation[0:2])
    if tag == 1 or tag == 2 or tag == 3 or tag == 4:
        return operation[2:]