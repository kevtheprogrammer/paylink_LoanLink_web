from django.shortcuts import render

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from account.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class CustomLoginView(TokenObtainPairView):
    
    def post(self, request):
        email = request.data.get('email')
        # phone = request.data.get('phone')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(request, email=email, password=password)
        
        
        if user:
            profile_pic_url = user.profile_pic.url if user.profile_pic else None
            full_profile_pic_uri = request.build_absolute_uri(profile_pic_url) if profile_pic_url else None
            # print('Profile',full_profile_pic_uri)

            # Check if user has a client profile
            if hasattr(user, 'client_profile'):
                payload = {
                    'id': user.id,
                    'email': user.email,
                    'phone_number': user.phone_number,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'profile_pic':full_profile_pic_uri,
                    'is_verified': user.is_verified,
                    'balance': user.client_profile.balance,
                    'empolyee_number': user.client_profile.empolyee_number,
                    'dob': user.dob.isoformat() if user.dob else None,
                }
            else:
                # Handle case where user does not have a client profile
                payload = {
                    'id': user.id,
                    'email': user.email,
                    'profile_pic':full_profile_pic_uri,
                    'phone_number': user.phone_number,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'is_verified': user.is_verified,
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
    
 