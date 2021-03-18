from django.shortcuts import render
from rest_framework.views import APIView, Response
from jose import jws
from rest_framework import status,exceptions
from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

# For Creating Password Hash
def get_password_hash(password):
    return password_context.hash(password)

# For verifying Password Hash
def verify_password(plain_password, hash_password):
    return password_context.verify(plain_password, hash_password)

# Creating Token for API Request
def create_token(dict_data):
    token = jws.sign(dict_data, 'MY_SECRET_KEY', algorithm='HS256')
    return token
# Decoding the Received token to verify the user
def decode_token(token):
    data = jws.verify(token, 'MY_SECRET_KEY', algorithms='HS256')
    return data.decode()

# Create your views here.
class LoginView(APIView):
    def get(self, request, format=None):
        return Response({"detail": "'GET' method not allowed for SignIn..."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def post(self, request, format=None):
        data = request.data
        username = data['username']
        password = data['password']

        hashed_password = get_password_hash(str(password))

        encoded_token = create_token({ 'user_name': username, 'password': hashed_password })

        return Response({ 'token': encoded_token, 'detail': 'Request Failed...' })
