from datetime import datetime
from utility import util

class State:
    def __init__(
        self, dictator_pkey, predecessor_timestamp, nb_bytes_in_next_sequence, accounts
    ):
        self.dictator_pkey = dictator_pkey
        self.predecessor_timestamp = predecessor_timestamp
        self.nb_bytes_in_next_sequence = nb_bytes_in_next_sequence
        self.accounts_binaries = accounts
        self.accounts = []

        cpt = 0
        while(cpt < int.from_bytes(nb_bytes_in_next_sequence, byteorder="big")):

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

            acc = Account(userpkey, predecessorpez, timestamppez,
                          operationhashpez, contexthashpez, signaturepez)
            self.accounts.append(acc)

    def print_state(self):
        print("dictator_pkey :\t\t\t\t", self.dictator_pkey.hex())
        date = util.decode_time(self.predecessor_timestamp)
        print("predecessor timestamp :\t\t\t\t", date)

        print("- - - Accounts - - -")
        for acc in self.accounts:
            acc.print_account()
            print(" - - - ")
    def get_state_value(self):
        return self.dictator_pkey + self.predecessor_timestamp + self.nb_bytes_in_next_sequence + self.accounts_binaries

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

    def print_account(self):
        print("user_pkey :\t\t\t", self.user_pkey.hex())
        print("predecessor_pez :\t\t", util.decode_int(self.predecessorp))
        print("timestamp_pez :\t\t\t", util.decode_int(self.timestampp))
        print("operations_hash_pez :\t\t", util.decode_int(self.operations_hashp))
        print("context_hash_pez :\t\t", util.decode_int(self.context_hashp))
        print("signature_pez :\t\t\t", util.decode_int(self.signaturep))
