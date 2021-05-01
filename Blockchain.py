import hashlib

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

transactions.append(t0)

# Coin
ANUBIS = []

# Client
alice = Client()
bob = Client()
charlie = Client()

# Transactions
t1 = Transaction(sitdhibong, alice.identity, 4.0)
t1.sign_transaction()
transactions.append(t1)

t2 = Transaction(alice, sitdhibong.identity, 8.0)
t2.sign_transaction()
transactions.append(t2)

t3 = Transaction(bob, charlie.identity, 7.0)
t3.sign_transaction()
transactions.append(t3)

t4 = Transaction(sitdhibong, bob.identity, 10.0)
t4.sign_transaction()
transactions.append(t4)


def display_transaction(transaction):
  dic = transaction.to_dict()
  print('Sender:', dic['sender'])
  print('-' * 10)
  print('Recipient:', dic['recipient'])
  print('-' * 10)
  print('Value:', dic['value'])
  print('-' * 10)
  print('Time:', dic['time'])
  print('=' * 10)

def display_blockchain(coin):
  print('No. of block in the chain', len(coin))
  i = 0
  for block_tmp in coin:
    print('block #', i)
    i += 1
    for tx in block_tmp.verified_transactions:
      display_transaction(tx)

# Mining
def mine(message, difficulty = 1):
  assert difficulty >= 1
  prefix = '1' * difficulty
  digest = None
  for i in range(10_000):
    digest = sha256(str(message) + str(i))
    if digest.startswith(prefix):
      print('After', i, 'iteration, NONCE FOUND with', digest)
      break

  return digest

def sha256(message):
  return hashlib.sha256(message.encode('ascii')).hexdigest()

# Miner 1
block = Block()
for tx in transactions:
  block.verified_transactions.append(tx)

block.previous_block_hash = last_block_hash
block.Nonce = mine(block, 2)
digest = hash(block)
ANUBIS.append(block)

display_blockchain(ANUBIS)
