from datetime import datetime
from model.operation import operations_hash

from utility import util, config
from communication import connection as ct

"""
Block representation.
"""

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

    def get_level(self):
        return util.decode_int(self.level)

    """
    Verify the hash of the predecessor block,
    if invalid, return false and the valid hash.
    """

    def verify_predecessor(self, debug=False):
        print("- - - - - -")
        print("Verify predecessor")
        level = int.from_bytes(self.level, byteorder="big")
        b_pred = ct.get_block(level - 1)
        b_pred_hash = util.hash(b_pred.get_block_value())
        if debug:
            print("Block predecessor : ", self.predecessor.hex())
            print("Block predecessor verification : ", b_pred_hash.hex())
        if self.predecessor == b_pred_hash:
            print("-> PREDECESSOR OK")
            return True, self.predecessor
        else:
            print("-> BAD PREDECESSOR")
            return False, b_pred_hash

    """
    Compare time with the predecessor,
    If larger than the TIME_OUT return False, and a valid timestamp.
    """

    def verify_timestamp(self, debug=False):
        print("- - - - - -")
        print("Verify timestamp")

        level = self.get_level()
        state_block = ct.get_block_state(level)

        timestamp_pred = util.decode_int(state_block.predecessor_timestamp)
        ts = util.decode_int(self.timestamp)
        if debug:
            print("Block timestamp : ", datetime.utcfromtimestamp(timestamp_pred))
            print("Block timestamp verification : ",
                  datetime.utcfromtimestamp(ts))
        if ts >= timestamp_pred + config.TIME_OUT:
            print("TIMESTAMP OK")
            return True, self.timestamp
        else:
            print("-> BAD TIMESTAMP")
            return False, util.encode_int(timestamp_pred + 600, 8)

    """
    Check operations hash,
    if invalid return true and the valid hash.
    """

    def verify_operations_hash(self, debug=False):
        level = self.get_level()
        ops = ct.get_block_operations(level)
        ops_hash = operations_hash(ops)
        if debug:
            print("Block predecessor : ", self.operations_hash.hex())
            print("Block predecessor verification : ", ops_hash.hex())
        if self.operations_hash == ops_hash:
            print("-> OPERATIONS_HASH OK")
            return True, self.operations_hash
        else:
            print("-> BAD OPERATIONS_HASH")
            return False, ops_hash

    """
    Verify current state hash,
    if invalid, return false and the valid hash.
    """

    def verify_state_hash(self, debug=False):
        print("- - - - - -")
        print("Verify state hash")
        level = self.get_level()
        state_block = ct.get_block_state(level)
        state_block_hash = util.hash(state_block.get_state_value())
        if debug:
            print("Block predecessor : ", self.state_hash.hex())
            print("Block predecessor verification : ", state_block_hash.hex())
        if self.state_hash == state_block_hash:
            print("-> STATE_HASH OK")
            return True, self.state_hash
        else:
            print("-> BAD STATE_HASH")
            return False, state_block_hash

    """
    Verify the hash of signature of the block,
    if invalid, return false and the valid hash.
    """

    def verify_signature(self):
        print("- - - - - -")
        print("Verify signature")
        level = self.get_level()
        state_block = ct.get_block_state(level)

        verifyingkeybin = state_block.dictator_pkey

        block_with_out_sign_value = (
            self.level
            + self.predecessor
            + self.timestamp
            + self.operations_hash
            + self.state_hash
        )

        block_without_sign_hash = util.hash(block_with_out_sign_value)
        if util.verify_signature(self.signature, verifyingkeybin, block_without_sign_hash):
            print("-> SIGNATURE OK")
            return True
        else:
            print("-> BAD SIGNATURE")
            return False

    """
    Run all verifier and injects corresponding operation.
    """

    def verify_all(self, debug=False):
        print("- - - - - - - - - - - - - - - - - - - - - - - - -")
        check, hash = self.verify_predecessor(debug)
        if not check:
            return ct.inject_bad_predecessor(hash)
        check, time = self.verify_timestamp(debug)
        if not check:
            return ct.inject_bad_timestamp(time)
        check, hash = self.verify_operations_hash(debug)
        if not check:
            return ct.inject_bad_operations_hash(hash)
        check, hash = self.verify_state_hash(debug)
        if not check:
            return ct.inject_bad_context_hash(hash)
        check = self.verify_signature()
        if not check:
            return ct.inject_bad_signature()
        print("- - - - - - - - - - - - - - - - - - - - - - - - -")
        return False

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
        level = self.get_level()
        print("level :\t\t\t\t", level)
        print("predecessor :\t\t\t", self.predecessor.hex())
        date = util.decode_time(self.timestamp)
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
