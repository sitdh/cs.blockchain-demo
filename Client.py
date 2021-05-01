import Cryptodome.Random
from Cryptodome.PublicKey import RSA
import binascii

class Client:
  def __init__(self):
    random = Cryptodome.Random.new().read
    self._priviate_key = RSA.generate(1024, random)
    self._public_key = self._private_key.publickey()

  def identity(self):
    return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

