# utils.py

from django.core.mail import send_mail
from django.conf import settings
import random
import string

# Function to generate a random verification code
def generate_verification_code():
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))  # 6-character code
    return code

# Function to send verification email
def send_verification_email(email, verification_code):
    verification_link = f'https://yourwebsite.com/verify?code={verification_code}'  # Your verification link
    subject = 'Matrimony Website Email Verification'
    message = f'Hello,\n\nYour verification code is: {verification_code}\n\nPlease click the following link to verify your email: {verification_link}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
