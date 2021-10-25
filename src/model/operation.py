from datetime import datetime
from utility import util

def print_operations(ops):
    print("- - - Operations - - -")
    for op in ops:
        op.print_operation()


def operations_hash(ops):
    size = len(ops)
    if (size == 0):
        return bytes(32)
    elif (size == 1):
        return util.hash(ops[0].get_bytes())
    else:
        return util.hash(operations_hash(ops[:size-1]) + util.hash(ops[size-1].get_bytes()))

class Operation:
    def __init__(self, tag, user_pk, hash=None, time=None, signature=None, sk=None):
        self.tag = util.encode_int(tag, 2)
        self.hash = hash
        self.time = time
        self.user_pk = user_pk
        if signature:
            self.signature = signature
        else:
            data = self.tag
            if hash:
                data += hash
            if time:
                data += time
            data += user_pk
            self.signature = util.sign(data, sk)

    def get_tag(self):
        return util.decode_int(self.tag)
        
    def get_bytes(self):
        res = self.tag
        if self.hash:
            res += self.hash
        if self.time:
            res += self.time
        res += self.user_pk
        res += self.signature
        return res

    def print_operation(self):
        print("tag :\t\t\t", self.tag.hex())
        if self.hash:
            print("hash :\t\t\t", self.hash.hex())
        if self.time:
            date = util.decode_time(self.time)
            print("time :\t\t\t", date)
        print("user_pk :\t\t", self.user_pk.hex())
        print("signature :\t\t", self.signature.hex())
