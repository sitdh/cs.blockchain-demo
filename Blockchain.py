from Client import Client
from Transaction import Transaction
ffrom Block import Block 

transactions = []
last_block_hash = []

sitdhibong = Client()
t0 = Transaction('Genesis', sitdhibong.identity, 500)
block0 = Block()
