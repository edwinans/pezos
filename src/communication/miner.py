import communication.connection as c
from model.block import Block
from model.operation import print_operations


def mine():
    try:
        c.connect()
        while True:
            b = c.get_current_head_async()
            b.print_block()
            b.verify_all()
            c.get_block_state(b.get_level()).print_state()
    except:
        c.disconnect()
