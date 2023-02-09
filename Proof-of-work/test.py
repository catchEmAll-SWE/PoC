#!/usr/bin/python
import hashlib

username = input("Username: ")
password = input("Password: ")
nonce = "000000"
cnonce = 0

print("Looking for nonce " + nonce)

hash = hashlib.sha256(username.encode('utf-8') + password.encode('utf-8') + str(cnonce).encode('utf-8')).hexdigest()
while not hash.startswith(nonce):
	cnonce += 1
	hash = hashlib.sha256(username.encode('utf-8') + password.encode('utf-8') + str(cnonce).encode('utf-8')).hexdigest()

print ("Found hash : " + str(hash))
print ("Correct cnonce is " + str(cnonce))