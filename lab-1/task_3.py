# не получилось не фартануло

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Загрузка открытого ключа из файла public.pem
with open('public.pem', 'r') as f:
    public_key = RSA.import_key(f.read())

# Инициализация объекта шифрования с открытым ключом
cipher_rsa = PKCS1_OAEP.new(public_key)

# Дешифрование зашифрованного сообщения crypt
with open('crypt', 'rb') as f:
    encrypted_message = f.read()
    decrypted_message = cipher_rsa.decrypt(encrypted_message)

print(decrypted_message.decode())