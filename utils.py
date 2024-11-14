import bcrypt

def hash_token(token: str):
    salt = bcrypt.gensalt()
    hashed_token = bcrypt.hashpw(token.encode(), salt)
    return hashed_token.decode('utf-8')

def verify_token(entered_token: str, stored_hashed_token: str) ->bool:
    return bcrypt.checkpw(entered_token.encode('utf-8'), stored_hashed_token.encode('utf-8'))

# Password hashing function
def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode('utf-8')

# Function to verify the password
def verify_password(entered_password: str, stored_hashed_password: str) -> bool:
    return bcrypt.checkpw(entered_password.encode('utf-8'), stored_hashed_password.encode('utf-8'))