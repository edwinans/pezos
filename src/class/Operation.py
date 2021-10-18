import sys
sys.path.append("../")
import util

class Operation:
    def __init__(
        self, tag, hash, time
    ):
        self.tag = tag
        self.hash = hash
        self.time = time
