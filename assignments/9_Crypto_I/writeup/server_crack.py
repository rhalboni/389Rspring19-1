#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
<<<<<<< HEAD
    i = 0
    hash_file = open('hashes.txt','r')
    hashes = hash_file.read().splitlines()
    pass_file =  open('passwords.txt', 'r')
    passwords = pass_file.read().splitlines()
    characters = list(string.ascii_lowercase)
    server_ip = '134.209.128.58'
    server_port = 1337
    password = '\n'
=======
    hashes = # open and read hashes.txt
    passwords = # open and read passwords.txt
    characters = string.ascii_lowercase
    server_ip = 'put_your_ip_here'
    server_port = 00000

>>>>>>> upstream/master
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    data = s.recv(1024).decode()
    print(data)
    data = data[26:len(data)-5]
    while i < 3:
        if  i == 1:
            data = s.recv(1024).decode()
            print(data)
            data = data[22:len(data)-5]
        if  i == 2:
            data = s.recv(1024).decode()
            print(data)
            data = data[16:len(data)-5]
        for c in characters:
            for p in passwords:
                p = p.strip() 
                hash_pass = c + p
                hashh = hashlib.sha256(hash_pass.encode('utf-8')).hexdigest()
                if hashh == data:
                    password = hash_pass + '\n'
                    print(password)
        s.send(password.encode())
        i += 1
    data = s.recv(1024).decode()
    print(data)
    # crack 3 times

if __name__ == "__main__":
    server_crack()
