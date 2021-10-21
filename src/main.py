import connection as c
from model.block import Block
from model.operation import print_operations

if __name__ == '__main__':
    c.connect()
    b1 = c.get_current_head()
    b1.print_block()
    ops = c.get_block_operations(1400)
    print_operations(ops)

    c.disconnect()
