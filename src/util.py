import pyblake2 as blake
import binascii
import ed25519

# Encode int into big endian binary on 4 bytes
def encode_entier(i, nbBytes=4):
    return i.to_bytes(nbBytes, 'big')


# Decode bytes into int
def decode_entier(b):
    return int.from_bytes(b, 'big')

def count_zero_prefix(val):
    cpt = 1
    for i in val:
        if i == "1":
            break;
        cpt = cpt + 1
    return cpt


# - - - - - - - - - - - - - - - - - - - Hash functions - - - - - - - - - - - - - - - - -

def hash_string(string):
    return blake.blake2b(string.encode(), digest_size=32).digest()

def concat_hash(hash1, hash2):
    newHash = hash1 + hash2
    return blake.blake2b(newHash, digest_size=32).digest()


# - - - - - - - - - - - - - - - - - - - Key encryption - - - - - - - - - - - - - - - - - - -

def create_keypair():
    privKey, pubKey = ed25519.create_keypair()
    # print("Private key (32 bytes):", privKey.to_ascii(encoding='hex'))
    # print("Public key (32 bytes): ", pubKey.to_ascii(encoding='hex'))
    return privKey, pubKey

def create_signature(privateKey, message):
    signature = privateKey.sign(message, encoding='hex')
    return signature;

def verify_signature(publicKey, messageToVerify, signature):
    try:
        publicKey.verify(signature, messageToVerify, encoding='hex')
        return True
    except ed25519.BadSignatureError:
        return False


# Example to verify signature from key encoded in hex
""" 

verifying_key = ed25519.VerifyingKey(pubkey.hex(), encoding="hex")
    try:
        print("Line : ", cpt, " | Good signature")
        verifying_key.verify(sign.hex(), msg, encoding='hex')
    except ed25519.BadSignatureError:
        print("Line : ", cpt, " | Bad signature")
        badSignatureLines.append(cpt) 

"""