import sys
import math
from datetime import datetime, timezone

sys.path.append("../")
import util

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
        return

    def verify_timestamp(self):
        return

    def verify_operations_hash(self):
        return

    def verify_state_hash(self):
        return

    def verify_signature(self):
        return

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