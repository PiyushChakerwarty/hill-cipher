'''============================================================================
| Assignment: pa01 - Encrypting a plaintext file using the Hill cipher
|
| Author: Your name here
| Language: c, c++, Java, go, python
|
| To Compile: javac pa01.java
| gcc -o pa01 pa01.c
| g++ -o pa01 pa01.cpp
| go build pa01.go
|
| To Execute: java -> java pa01 kX.txt pX.txt
| or c++ -> ./pa01 kX.txt pX.txt
| or c -> ./pa01 kX.txt pX.txt
| or go -> ./pa01 kX.txt pX.txt
| or python -> python3 pa01.py kX.txt pX.txt
| where kX.txt is the keytext file
| and pX.txt is plaintext file
| Note:
| All input files are simple 8 bit ASCII input
| All execute commands above have been tested on Eustis
|
| Class: CIS3360 - Security in Computing - Fall 2023
| Instructor: McAlpin
| Due Date: per assignment
+==========================================================================='''


import sys
import numpy as np

def read_key_file(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        matrix = [list(map(int, f.readline().split())) for _ in range(n)]
    return n, np.array(matrix)

def read_and_process_plaintext(filename, block_size):
    with open(filename, 'r') as f:
        text = f.read().lower()
    filtered_text = ''.join(filter(str.isalpha, text))
    padded_text = filtered_text + 'x' * ((block_size - len(filtered_text) % block_size) % block_size)
    return padded_text

def encrypt_block(block, key_matrix):
    vector = np.array([ord(char) - ord('a') for char in block])
    encrypted_vector = np.dot(key_matrix, vector) % 26
    encrypted_text = ''.join(chr(num + ord('a')) for num in encrypted_vector)
    return encrypted_text

def encrypt_text(plaintext, key_matrix, block_size):
    return ''.join(encrypt_block(plaintext[i:i+block_size], key_matrix) for i in range(0, len(plaintext), block_size))

def print_matrix(matrix):
    max_width = max(max(map(len, map(str, row))) for row in matrix)
    for row in matrix:
        for num in row:
            padding = ' ' * (max_width - len(str(num)) + 1)
            print(padding + str(num), end='')
        print()



def main():
    key_file, plaintext_file = sys.argv[1], sys.argv[2]
    block_size, key_matrix = read_key_file(key_file)
    plaintext = read_and_process_plaintext(plaintext_file, block_size)
    ciphertext = encrypt_text(plaintext, key_matrix, block_size)

    print("Key matrix:")
    print_matrix(key_matrix)
    print("Plaintext:")
    for i in range(0, len(plaintext), 80):
        print(plaintext[i:i+80])
    print("Ciphertext:")
    for i in range(0, len(ciphertext), 80):
        print(ciphertext[i:i+80])

if __name__ == "__main__":
    main()



'''=============================================================================
| I [your name] ([your NID]) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+============================================================================='''