
import util
import sys

sys.path.append("./class")
import State
import Block


def decode_block(block):
    return (
        Block(block[0:4], block[4:36], block[36:44], block[44:76], block[76:108], block[108:172])
    )


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
        return message[4:]
    if tag == 8:
        return State(message[2:34], message[34:42], message[42:46], message[46:])
    if tag == 9:
        return message[2:]


def decode_operations(operation):
    tag = util.decode_entier(operation[0:2])
    if tag == 1 or tag == 2 or tag == 3 or tag == 4:
        return operation[2:]