import sys
import math
from datetime import datetime, timezone
import ed25519 as old_ed

sys.path.append("../")
import util
import connection

import encode_message


class Block:
    def __init__(
        self, level, predecessor, timestamp, operations_hash, state_hash, signature
    ):
        self.level = level
        self.predecessor = predecessor
        self.timestamp = timestamp
        self.operations_hash = operations_hash
        self.state_hash = state_hash
        self.signature = signature

    def verify_predecessor(self):
        print("- - - - - -")
        print("Verify predecessor")
        levelNumber = int.from_bytes(self.level, byteorder="big")
        b_pred = connection.get_block(levelNumber-1)
        b_pred_hash = util.hash(b_pred.get_block_value())

        if(self.predecessor == b_pred_hash):
            print("OK")
            return True
        else:
            print("FAILED")
            return False

    def verify_timestamp(self):
        print("- - - - - -")
        print("Verify timestamp")

        levelNumber = int.from_bytes(self.level, byteorder="big")
        state_block = connection.get_block_state(levelNumber)
        
        timestamp_pred = int.from_bytes(state_block.predecessor_timestamp, byteorder="big")
        if(int.from_bytes(self.timestamp, byteorder="big") >= timestamp_pred + 600):
            print("OK")
            return True
        else:
            print("FAILED")
            return False

    def verify_operations_hash(self):
        return

    def verify_state_hash(self):
        print("- - - - - -")
        print("Verify state hash")
        levelNumber = int.from_bytes(self.level, byteorder="big")
        state_block = connection.get_block_state(levelNumber)
        state_block_hash = util.hash(state_block.get_state_value())
        
        if(self.state_hash == state_block_hash):
            print("OK")
            return True
        else:
            print("FAILED")
            return False

    def verify_signature(self):
        print("- - - - - -")
        print("Verify signature")
        levelNumber = int.from_bytes(self.level, byteorder="big")
        state_block = connection.get_block_state(levelNumber)

        verifyingkeybin = state_block.dictator_pkey
        
        block_with_out_sign_value = self.level + self.predecessor + self.timestamp + self.operations_hash + self.state_hash
        block_without_sign_hash = util.hash(block_with_out_sign_value)

        
        verifying_key = old_ed.VerifyingKey(verifyingkeybin.hex(), encoding="hex")
        try:
            verifying_key.verify(self.signature.hex(), block_without_sign_hash, encoding='hex')
            print("OK")
            return True
        except old_ed.BadSignatureError:
            print("FAILED")
            return False
            

    def verify_all(self):
        print("- - - - - - - - - - - - - - - - - - - - - - - - -")
        if(self.verify_predecessor()):
            print("Bad predecessor")
            # Send message bad operation predecessor
        elif self.verify_timestamp():
            print("Bad timestamp")
            # Send message bad timestamp
        elif self.verify_operations_hash():
            print("Bad operation hash")
            # Send message bad operation hash
        elif self.verify_state_hash():
            print("Bad state hash")
            # Send message bad state hash
        elif self.verify_signature():
            print("Bad signature")
            # Send message bad signature
        print("- - - - - - - - - - - - - - - - - - - - - - - - -")
    def get_block_value(self):
        return (
            self.level
            + self.predecessor
            + self.timestamp
            + self.operations_hash
            + self.state_hash
            + self.signature
        )

    def print_block(self):
        levelNumber = int.from_bytes(self.level, byteorder="big")
        print("level :\t\t\t\t", levelNumber)
        print("predecessor :\t\t\t", self.predecessor.hex())
        date = datetime.utcfromtimestamp(int.from_bytes(self.timestamp, byteorder="big"))
        print("timestamp :\t\t\t", date)
        print("operation_hash :\t\t", self.operations_hash.hex())
        print("state_hash :\t\t\t", self.state_hash.hex())
        print("signature :\t\t\t", self.signature.hex())

    def print_block_hex(self):
        print("level :\t\t\t\t", self.level.hex())
        print("predecessor :\t\t\t", self.predecessor.hex())
        print("timestamp :\t\t\t", self.timestamp.hex())
        print("operation_hash :\t\t", self.operations_hash.hex())
        print("state_hash :\t\t\t", self.state_hash.hex())
        print("signature :\t\t\t", self.signature.hex())


# level = util.encode_int(44)
# predecessor = bytearray.fromhex(
#     "1c80203a30e5de4d980cc555131d1b4a4750edc82c0c443179d88de1ae4f6cdf"
# )

# date = datetime(2021, 10, 10, hour=15, minute=21, second=9, tzinfo=timezone.utc)
# ts = math.floor(date.timestamp())
# timestamp = util.encode_int(ts, size=8)

# operations_hash = bytearray.fromhex(
#     "0000000000000000000000000000000000000000000000000000000000000000"
# )
# state_hash = bytearray.fromhex(
#     "22a00d1c8c0fbaefedd71ddb83d455033efd259a8f0adf189b9f850a0d1945f2"
# )
# signature = bytearray.fromhex(
#     "cc3faffc696c86db13d50752fdb7edd0ee1ce19ab350f60899939fc139d58996419c13b812b7f005fafaf23924d2f1df555036bc61e7b67cb679375e5756b306"
# )

# b1 = Block(level, predecessor, timestamp, operations_hash, state_hash, signature)
# blockVal = b1.get_block_value()

# print(blockVal.hex())

# b1.print_block()
# # b1.print_block_hex()
# # print(timestamp)
# print("-----------------------")
# print(blockVal)