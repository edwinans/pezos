import connection as c
from model.block import Block

if __name__ == '__main__':
    c.connect()
    b1 = c.get_current_head()
    b1.print_block()
    b1.verify_all()
    c.disconnect()
