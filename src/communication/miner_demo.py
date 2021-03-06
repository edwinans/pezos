import communication.connection as c

"""
Interactive demo version of the miner to debug & test.
"""


def mine_demo():
    try:
        c.connect()
        exit = False
        block = None
        while not exit:
            if block is not None:
                print()
                print("Current block : ")
                block.print_block()
                input("\n - - - PRESS ENTER TO CONTINUE - - - \n")

            print()
            print("Menu : ")
            print("- Get current block : GCB")

            if block is not None:
                print("- Verify predecessor : VP")
                print("- Verify timestamp : VT")
                print("- Verify operation hash : VOH")
                print("- Verify state hash : VSH")
                print("- Verify signature : VS")
                print("- Verify all : VALL")

                print("- Print state : PS")
            print("- Exit : E")

            command = input("... : ")
            if command == "GCB":
                block = c.get_current_head()
            elif command == "VP":
                block.verify_predecessor(debug=True)
            elif command == "VT":
                block.verify_timestamp(debug=True)
            elif command == "VOH":
                block.verify_operations_hash(debug=True)
            elif command == "VSH":
                block.verify_state_hash(debug=True)
            elif command == "VS":
                block.verify_signature()
            elif command == "VALL":
                block.verify_all(debug=True)
            elif command == "PS":
                c.get_block_state(block.get_level()).print_state()
            elif command == "E":
                exit = True

    except Exception as e:
        print(e)
        c.disconnect()
    c.disconnect()
