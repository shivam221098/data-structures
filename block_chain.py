import hashlib


class Block:
    def __init__(self, previous_hash, transaction):
        self.transactions = transaction
        self.previous_hash = previous_hash
        str_to_hash = "".join(transaction) + previous_hash
        self.block_hash = hashlib.sha256(str_to_hash.encode()).hexdigest()

    def __str__(self):
        return self.block_hash


if __name__ == '__main__':
    genesis_block = Block("my first block", ["transaction 1", "transaction 2", "transaction 3", "transaction 4"])
    # type of genesis_block is 'class'
    # typecasting as a string to use it.
    second_block = Block(str(genesis_block), "abcd1")

    print(genesis_block)
    print(second_block)
