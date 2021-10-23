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
    except:
        c.disconnect()