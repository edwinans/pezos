import connection as c
from model.block import Block

if __name__ == '__main__':
    c.connect()
    b1 = c.get_current_head()
    b1.print_block()
    s = c.get_block_state(1001)
    s.print_state()

    c.disconnect()
