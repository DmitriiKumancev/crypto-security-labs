import hashlib
import random
import matplotlib

matplotlib.use('agg')  

import matplotlib.pyplot as plt

def generate_random_message(message_length):
    return bytearray(random.getrandbits(8) for _ in range(message_length))

def change_one_bit(message, bit_position):
    message[bit_position // 8] ^= (1 << (bit_position % 8))
    return message

def calculate_hash(message, algorithm):
    hash_object = hashlib.new(algorithm)
    hash_object.update(message)
    return hash_object.hexdigest()

def compare_hashes(original_message, modified_message, algorithm):
    original_hash = calculate_hash(original_message, algorithm)
    modified_hash = calculate_hash(modified_message, algorithm)

    num_different_bits = sum(c1 != c2 for c1, c2 in zip(original_hash, modified_hash))

    return num_different_bits

message_length = 64
rounds = 64

different_bits_md5 = []
different_bits_sha512 = []

for bit_position in range(message_length * 8):
    original_message = generate_random_message(message_length)

    different_bits_md5_round = []
    different_bits_sha512_round = []

    for round_num in range(rounds):
        modified_message = change_one_bit(original_message.copy(), bit_position)

        different_bits_md5_round.append(compare_hashes(original_message, modified_message, 'md5'))
        different_bits_sha512_round.append(compare_hashes(original_message, modified_message, 'sha512'))

    different_bits_md5.append(different_bits_md5_round)
    different_bits_sha512.append(different_bits_sha512_round)

# Построение графиков
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
for i in range(len(different_bits_md5)):
    plt.plot(range(rounds), different_bits_md5[i], label=f'Bit {i}')
plt.xlabel('Round')
plt.ylabel('Different Bits (MD5)')
plt.title('MD5 Hash - Number of Different Bits vs Round')
plt.legend()

plt.subplot(1, 2, 2)
for i in range(len(different_bits_sha512)):
    plt.plot(range(rounds), different_bits_sha512[i], label=f'Bit {i}')
plt.xlabel('Round')
plt.ylabel('Different Bits (SHA-512)')
plt.title('SHA-512 Hash - Number of Different Bits vs Round')
plt.legend()

plt.tight_layout()
plt.savefig('hash_comparison_plot.png')  