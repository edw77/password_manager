from hashlib import sha256
import hashlib

def password_gen(): 

    password = input("Enter your password: ").encode()

    compile_factor_together = hashlib.sha256(password).hexdigest()

    print("Password: " + str(compile_factor_together))

password_gen()