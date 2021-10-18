class State:
    def __init__(
        self, dictator_pkey, predecessor_timestamp, nb_bytes_in_next_sequence, accounts
    ):
        self.dictator_pkey = dictator_pkey
        self.predecessor_timestamp = predecessor_timestamp
        self.nb_bytes_in_next_sequence = nb_bytes_in_next_sequence
        self.accounts = []

        while(cpt < nb_bytes_in_next_sequence):
            cpt = 0

            userpkey = accounts[cpt:cpt+32]
            cpt += 32

            predecessorpez = accounts[cpt:cpt+4]
            cpt += 4
            
            timestamppez = accounts[cpt:cpt+4]
            cpt += 4

            operationhashpez = accounts[cpt:cpt+4]
            cpt += 4

            contexthashpez = accounts[cpt:cpt+4]
            cpt += 4
            
            signaturepez = accounts[cpt:cpt+4]
            cpt += 4

            acc = Account(userpkey, predecessorpez, timestampez, operationhashpez, contexthashpez, signaturepez)
            self.accounts.append[acc]

class Account:
    def __init__(
        self, user_pkey, predecessorp, timestampp, operations_hashp, context_hashp, signaturep
    ):
        self.user_pkey = user_pkey
        self.predecessorp = predecessorp
        self.timestampp = timestampp
        self.operations_hashp = operations_hashp
        self.context_hashp = context_hashp
        self.signaturep = signaturep
