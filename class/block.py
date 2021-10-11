
class Block:
    def __init__(self, level, predecessor, timestamp, operations_hash, context_hash, signature):
        self.level = level
        self.predecessor = predecessor
        self.timestamp = timestamp
        self.operations_hash = operations_hash
        self.context_hash = context_hash
        self.signature = signature
    
    def verify_predecessor():
        return
    
    def verify_timestamp():
        return

    def verify_operations_hash():
        return
    
    def verify_context_hash():
        return
    
    def verify_signature():
        return
    
    def printBlock():
        return