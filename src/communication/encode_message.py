from utility import util


def encode_message(message):
    return util.encode_int(len(message), size=2) + message


def encode_get_currrent_head():
    return encode_message(util.encode_int(1, size=2))


def encode_get_block(level):
    level_b = util.encode_int(level, 4)
    return encode_message(util.encode_int(3, size=2) + level_b)


def encode_get_block_by_integer_level(level):
    return util.encode_int(3, nbBytes=2) + util.encode_int(level, nbBytes=4)


def encode_block(block):
    return util.encode_int(4, size=2) + block.get_block_value()


def encode_get_block_operations(level):
    level_b = util.encode_int(level)
    return encode_message(util.encode_int(5, size=2) + level_b)


def encode_get_block_operations_by_integer_level(level):
    return util.encode_int(5, nbBytes=2) + util.encode_int(level, nbBytes=4)


def encode_get_state(level):
    level_b = util.encode_int(level)
    return encode_message(util.encode_int(7, size=2) + level_b)


def encode_get_state_by_integer(level):
    return util.encode_int(7, nbBytes=2) + util.encode_int(level, nbBytes=4)


def encode_block_operations(operations):
    return encode_message(
        util.encode_int(6, size=2)
        + util.encode_int(len(operations), size=2)
        + operations
    )


def encode_block_state(state):
    return util.encode_int(8, size=2) + state


def encode_inject_operation(operation):
    return encode_message(util.encode_int(9, size=2) + operation)


def encode_signed_operation(operation, user_pkey, signature):
    return operation + user_pkey + signature


def encode_bad_predecessor(hash):
    return util.encode_int(1, size=2) + hash


def encode_bad_timestamp(time):
    return util.encode_int(2, size=2) + util.encode_int(time, size=8)


def encode_bad_operations_hash(hash):
    return util.encode_int(3, size=2) + hash


def encode_bad_context_hash(hash):
    return util.encode_int(4, size=2) + hash


def encode_bad_signature():
    return util.encode_int(5, size=2)


def encode_state(state):
    return (
        state.dictator_pkey
        + state.predecessor_timestamp
        + state.nb_bytes_in_next_sequence
        + state.accounts
    )


def encode_account(account):
    return (
        account.user_pkey
        + account.levelp
        + account.timestampp
        + account.operations_hashp
        + account.context_hashp
        + account.signaturep
    )
