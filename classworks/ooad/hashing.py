import bcrypt

password = b"banana"
password2 = b"banana"

hash = bcrypt.hashpw(password, bcrypt.gensalt() ) 
hash2 = bcrypt.hashpw(password2, bcrypt.gensalt() ) 

print(hash)
print(hash2)
print(bcrypt.checkpw(b"banana", hash2))