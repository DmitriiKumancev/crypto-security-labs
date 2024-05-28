from cryptography.hazmat.primitives import serialization 
from cryptography.hazmat.primitives.asymmetric import rsa 
from cryptography.hazmat.primitives import hashes 
from cryptography.hazmat.primitives.asymmetric import padding 

"""
реализвция использования асимметричного шифрования RSA для генерации ключей, подписи данных и верификации подписи.

Функции:
---------
1. generate_RSA_keys():
    функция генерирует пару ключей RSA (приватный и публичный).

2. sign_data(private_key, data):
    подписывает данные с использованием приватного ключа. Данные хэшируются с помощью SHA256, а затем используется 
    PSS (Probabilistic Signature Scheme) для добавления паддинга к данным перед подписью.

3. verify_signature(public_key, signature, data):
    Эта функция проверяет подпись данных с использованием публичного ключа. Она также использует SHA256 и PSS для верификации подписи.

"""


def generate_RSA_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_data(private_key, data):
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, signature, data):
    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False

if __name__ == "__main__":
    private_key, public_key = generate_RSA_keys()
    message = b"Hello, World!"
    signature = sign_data(private_key, message)
    print("Signature:", signature)
    print("Signature Verified:", verify_signature(public_key, signature, message))