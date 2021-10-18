from datetime import datetime


def print_operations(ops):
    print("- - - Operations - - -")
    for op in ops:
        op.print_operation()


class Operation:
    def __init__(
        self, tag, hash, time, user_pk, signature
    ):
        self.tag = tag
        self.hash = hash
        self.time = time
        self.user_pk = user_pk
        self.signature = signature

    def print_operation(self):
        print("tag :\t\t\t", self.tag.hex())
        if self.hash:
            print("hash :\t\t\t", self.hash.hex())
        if self.time:
            date = datetime.utcfromtimestamp(
                int.from_bytes(self.time, byteorder="big"))
            print("time :\t\t\t", date)
        print("user_pk :\t\t", self.user_pk.hex())
        print("signature :\t\t", self.signature.hex())
