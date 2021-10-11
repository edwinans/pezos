
class State:
    def __init__(self, dictator_pkey, predecessor_timestamp, nb_bytes_in_next_sequence, accounts):
        self.dictator_pkey = dictator_pkey
        self.predecessor_timestamp = predecessor_timestamp
        self.nb_bytes_in_next_sequence = nb_bytes_in_next_sequence
        self.accounts = accounts


class Account:
    def __init__(self, user_pkey, levelp, timestampp, operations_hashp, context_hashp,signaturep):
        self.user_pkey = user_pkey
        self.levelp = levelp
        self.timestampp = timestampp
        self.operations_hashp = operations_hashp
        self.context_hashp = context_hashp
        self.signaturep = signaturep
    