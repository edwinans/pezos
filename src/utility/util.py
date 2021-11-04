import pyblake2 as blake
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.exceptions import InvalidSignature
from datetime import datetime
import os

def encode_pk(pk):
    pk_b = bytes(bytearray.fromhex(pk))
    return encode_int(32, 2) + pk_b


def read_keys():
    keysFile = (os.path.join(os.path.dirname(os.path.dirname(__file__)),"utility/keys"))
    f = open(keysFile)
    pk = f.readline()
    sk = f.readline()
    return pk, sk


# Encode int into big endian binary on 4 bytes
def encode_int(i, size=4):
    return i.to_bytes(size, "big")


# Decode bytes into int
def decode_int(b):
    return int.from_bytes(b, "big")


def decode_time(b):
    date = datetime.utcfromtimestamp(decode_int(b))
    return date

# - - - - - - - - - - - - - - - - - - - Signing - - - - - - - - - - - - - - - - -


def encode_sig(data, sk):
    sk_b = bytes(bytearray.fromhex(sk))
    h_data = hash(data)
    private_key = ed25519.Ed25519PrivateKey.from_private_bytes(sk_b)
    sig = private_key.sign(h_data)
    return encode_int(64, 2) + sig


def sign(data, sk):
    sk_b = bytes(bytearray.fromhex(sk))
    h_data = hash(data)
    private_key = ed25519.Ed25519PrivateKey.from_private_bytes(sk_b)
    sig = private_key.sign(h_data)
    return sig


def verify_signature(sig, pk, data):
    public_key = ed25519.Ed25519PublicKey.from_public_bytes(pk)
    try:
        public_key.verify(sig, data)
        return True
    except InvalidSignature:
        return False


# - - - - - - - - - - - - - - - - - - - Hash functions - - - - - - - - - - - - - - - - -


def hash(b):
    return blake.blake2b(b, digest_size=32).digest()


def hash_string(string):
    return blake.blake2b(string.encode(), digest_size=32).digest()


def concat_hash(hash1, hash2):
    newHash = hash1 + hash2
    return blake.blake2b(newHash, digest_size=32).digest()
