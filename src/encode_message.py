import util


def encode_message(message):
    return (
            util.encode_entier(len(message), nbBytes=2)
            + message
    )


def encode_get_current_head_message():
    return util.encode_entier(1, nbBytes=2)


def encode_current_head(block):
    return (
            util.encode_entier(2, nbBytes=2)
            + block.get_block_value()
    )


def encode_get_block(level):
    return (
            util.encode_entier(3, nbBytes=2)
            + level
    )


def encode_block(block):
    return (
            util.encode_entier(4, nbBytes=2)
            + block.get_block_value()
    )


def encode_get_block_operations(level):
    return (
            util.encode_entier(5, nbBytes=2)
            + level
    )


def encode_get_state(level):
    return (
        util.encode_entier(7, nbBytes=2)
        + level
    )


def encode_block_operations(operations):
    return (
        util.encode_entier(6, nbBytes=2)
        + util.encode_entier(len(operations), nbBytes=2)
        + operations
    )


def encode_block_state(state):
    return (
        util.encode_entier(8, nbBytes=2)
        + state
    )


def encode_inject_operation(operation):
    return (
        util.encode_entier(8, nbBytes=2)
        + operation
    )


def encode_signed_operation(operation, user_pkey, signature):
    return (
        operation
        + user_pkey
        + signature
    )


def encode_bad_predecessor(hash):
    return (
        util.encode_entier(1, nbBytes=2)
        + hash
    )


def encode_bad_timestamp(time):
    return (
        util.encode_entier(2, nbBytes=2)
        + util.encode_entier(time, nbBytes=8)
    )


def encode_bad_operations_hash(hash):
    return (
        util.encode_entier(3, nbBytes=2)
        + hash
    )


def encode_bad_context_hash(hash):
    return (
        util.encode_entier(4, nbBytes=2)
        + hash
    )


def encode_bad_signature():
    return (
        util.encode_entier(5, nbBytes=2)
    )


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