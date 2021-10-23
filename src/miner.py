import connection as c
from model.block import Block
from model.operation import print_operations

def mine():
    try:
        c.connect()
        while(True):
            b = c.get_current_head_async()
            b.print_block()
            b.verify_all()

        # b = c.get_current_head()
        # b.print_block()
        # print_operations(c.get_block_operations(1490))
        # c.get_block_state(1490).print_state()
        # b.verify_all()
    except:
        c.disconnect()