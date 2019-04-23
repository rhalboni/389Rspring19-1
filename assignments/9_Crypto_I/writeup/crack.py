#!/usr/bin/env python3

import hashlib
import string

def crack():
    hash_file = open('hashes.txt','r')
    passwords = open('passwords.txt', 'r')
    characters = list(string.ascii_lowercase)
    hashes = hash_file.read().splitlines()
    passwords = passwords.read().splitlines()
    for c in characters:
        for p in passwords:
            p = p.strip() 
            hash_pass = c + p
            h = hashlib.sha256(hash_pass.encode('utf-8')).hexdigest()
            if h in hashes:
                print(p + ':' + h)
           
if __name__ == "__main__":
    crack()
