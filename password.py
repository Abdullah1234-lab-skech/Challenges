import random
def generate_password(length):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    all_chars = lowercase + uppercase + digits
    password = ''
    for _ in range(length):
        password += random.choice(all_chars)
    return password
password_length = 10-1000
print("Generated Password:", generate_password(password_length))
