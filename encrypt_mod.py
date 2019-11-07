import codes # set of dictionarys used in encrypting the passwords
import secrets # Module for random numbers

# encrypts the password with random codes if they are not otherwise specified
def encrypt(password, code_1="", code_2=""):
    first_half, second_half = split_pw(password)
    first_half = encryptor(first_half, code_1)
    second_half = encryptor(second_half, code_2)
    encrypted_password = first_half + second_half
    return encrypted_password

# Split the password into two even pieces to encrypt seperatly
def split_pw(password):
	first_half = password[0:4]
	second_half = password[4:8]
	return first_half, second_half

# Takes one half of the password and encrypts it with a random codes
def encryptor(half, code): # grabs the coder used and the coder number(encoder key)
	if code == "":
		coder, code = generate_code() # Checks if a value has been entered for code, if not generate code
	else:
		coder = codes.codes[code]     # If there is a value entered for code, then grab that code
	
	encrypted = "" # Sets up an empty string to put the encrypted half into 
	for char in half:
	 	encrypted = encrypted + coder[char]
	encrypted = code + encrypted
	return encrypted # Displays the half of the encrypted password with the encoder key

def generate_code():
	code = str(secrets.randbelow(3))  # Generates a random number from 0-3 to choose a code
	coder = codes.codes[code]         # Grabs the code from the dictionary based on the generated number
	return coder, code
