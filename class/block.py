import sys
import math
from datetime import datetime, timezone

sys.path.append('../')
import util;


class Block:
    def __init__(self, level, predecessor, timestamp, operations_hash, context_hash, signature):
        self.level = level
        self.predecessor = predecessor
        self.timestamp = timestamp
        self.operations_hash = operations_hash
        self.context_hash = context_hash
        self.signature = signature
    
    def verify_predecessor(self):
        return
    
    def verify_timestamp(self):
        return

    def verify_operations_hash(self):
        return
    
    def verify_context_hash(self):
        return
    
    def verify_signature(self):
        return

    def getBlockValue(self):
        return self.level + self.predecessor + self.timestamp + self.operations_hash + self.context_hash + self.signature

    def printBlock(self):
        print(level.hex())
        print(predecessor.hex())
        print(timestamp.hex())
        print(operations_hash.hex())
        print(context_hash.hex())
        print(signature.hex())

level = util.encode_entier(44)
predecessor = bytearray.fromhex("1c80203a30e5de4d980cc555131d1b4a4750edc82c0c443179d88de1ae4f6cdf")

date = datetime(2021, 10, 10, hour=15, minute=21, second=9, tzinfo=timezone.utc)
ts = math.floor(date.timestamp())
timestamp = util.encode_entier(ts,nbBytes=8)

operations_hash = bytearray.fromhex("0000000000000000000000000000000000000000000000000000000000000000")
context_hash = bytearray.fromhex("22a00d1c8c0fbaefedd71ddb83d455033efd259a8f0adf189b9f850a0d1945f2")
signature = bytearray.fromhex("cc3faffc696c86db13d50752fdb7edd0ee1ce19ab350f60899939fc139d58996419c13b812b7f005fafaf23924d2f1df555036bc61e7b67cb679375e5756b306")

b1 = Block(level,predecessor,timestamp,operations_hash,context_hash,signature)
blockVal = b1.getBlockValue()

print(blockVal.hex())

# print(timestamp)