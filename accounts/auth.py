from django.shortcuts import render

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import User
from rest_framework.response import Response
from rest_framework import status


class CustomLoginView(APIView):

    def post(self, request):
        email = request.data.get('email')
        # phone = request.data.get('phone')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(request, email=email, password=password)

        if user:
            # Token payload
            payload = {
                'id': user.id,
                'email': user.email,
                'phone': user.phone,
                'first_name': user.first_name,
                'last_name': user.last_name,
                # Assuming avatar is an ImageField
                # 'avatar': user.avatar.url if user.avatar else None,
                'dob': user.dob.isoformat() if user.dob else None,
            }

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)

            access_token = RefreshToken.for_user(user)
            access_token['payload'] = payload
            access_token = str(access_token.access_token)
            refresh_token = str(refresh)

            return Response(
                {
                    'access_token': access_token,
                    'refresh_token': refresh_token
                },
                status=status.HTTP_200_OK
            )
        
        return Response({'error': 'Invalid credentials'}, status=401)
