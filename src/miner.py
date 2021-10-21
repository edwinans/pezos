import connection as c
from model.block import Block
from model.operation import print_operations

def mine():
    c.connect()
    b = c.get_current_head()
    b.print_block()
    # print_operations(c.get_block_operations(1475))
    # b.verify_all()
    c.disconnect()