import communication.connection as c

"""
Miner loop
block and waits for the current head to verify it.
"""


def mine(argumentWithNoValue,argumentWithValue):
    try:
        c.connect()
        while True:
            b = c.get_current_head_async()
            b.print_block()
            if("timestamp" in argumentWithValue):
                b.verify_all(timestamp_min=int(argumentWithValue["timestamp"]))
            else:
                b.verify_all()
            c.get_block_state(b.get_level()).print_state()
    except:
        c.disconnect()
