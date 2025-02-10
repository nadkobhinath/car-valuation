import random
import string

def generate_random_email(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))+'@mailinator.com'
