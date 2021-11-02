import connection as c
from model.block import Block
from model.operation import print_operations
import util


def mine():
    try:
        c.connect()
        b = c.get_current_head()
        b.verify_all()
        c.get_block_state(b.get_level()).print_state()

        while(True):
            b = c.get_current_head_async()
            b.print_block()
            b.verify_all()
            c.get_block_state(b.get_level()).print_state()

        # c.get_current_head().verify_all()
        # b = c.get_block(1742)
        # f,t = b.verify_timestamp()
        # print(util.decode_time(t))
        # print_operations(c.get_block_operations(1743))

    except Exception as e:
        print(e)
        c.disconnect()
