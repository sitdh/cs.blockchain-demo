import datetime
import collections
import binascii

from Cryptodome.Hash import SHA
from Cryptodome.Signature import PKCS1_v1_5

class Transaction:
  def __init__(self, sender, recipient, value):
    self.sender = sender
    self.recipient = recipient
    self.value = value
    self.time = datetime.datetime.now()

  def to_dict(self):
    identity = 'Genesis' if self.sender == 'Genesis' else self.sender.identity

    return collections.OrderedDict({
      'sender': identity,
      'recipient': self.recipient,
      'value': self.value,
      'time': self.time,
    })

  def sign_transaction(self):
    private_key = self.sender._private_key
    signer = PKCS1_v1_5.new(private_key) #v2 recommended
    hash_message = SHA.new(str(self.to_dict()).encode('utf8'))
    
    return binascii.hexlify(signer.sign(hash_message)).decode('ascii')
