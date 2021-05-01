from Client import Client
from Transaction import Transaction
from Block import Block 

transactions = []
last_block_hash = []

sitdhibong = Client()
t0 = Transaction('Genesis', sitdhibong.identity, 500)
block0 = Block()
block0.previous_block_hash = None
Nonce = None
block0.verified_transactions.append(t0)
last_block_hash = hash(block0)
