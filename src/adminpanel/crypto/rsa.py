from os.path import join

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256


class Rsa:
    def __init__(self, key_size=2048):
        self.key = RSA.generate(key_size)
        self.pub_key = None
        self.prv_key = None

    async def save_key(self, path='./'):
        async with open(join(path, 'pub_key.pem'), 'wb') as f:
            await f.write(self.key.public_key().export_key())
        async with open(join(path, 'prv_key.pem'), 'wb') as f:
            await f.write(self.key.export_key())

    def load_key(self, path='./'):
        self.pub_key = RSA.import_key(
            open(join(path, 'pub_key.pem'), 'rb').read())
        self.prv_key = RSA.import_key(
            open(join(path, 'prv_key.pem'), 'rb').read())

    def encrypt(self, message):
        cipher = PKCS1_OAEP.new(self.pub_key)
        return cipher.encrypt(message)

    def decrypt(self, ciphertext):
        cipher = PKCS1_OAEP.new(self.prv_key)
        return cipher.decrypt(ciphertext)

    def sign(self, message):
        signer = PKCS1_v1_5.new(self.prv_key)
        digest = SHA256.new()
        digest.update(message)
        return signer.sign(digest)

    def verify(self, message, signature):
        signer = PKCS1_v1_5.new(self.pub_key)
        digest = SHA256.new()
        digest.update(message)
        return signer.verify(digest, signature)


if __name__ == '__main__':
    rsa = Rsa()
    message = b'Hello World'

    # rsa.save_key()
    rsa.load_key()
    encrypted_message = rsa.encrypt(message)
    decrypted_message = rsa.decrypt(encrypted_message)
    print(encrypted_message)
    print(decrypted_message)
    signature = rsa.sign(message)
    print(rsa.verify(message, signature))